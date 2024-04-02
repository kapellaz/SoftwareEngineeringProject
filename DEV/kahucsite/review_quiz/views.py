"""This file have all views about user-story: review quiz."""
# pylint: disable=E1101
from django.db import connection
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect
from django.contrib import messages as msgs
from django.http import Http404
from quiz.models import Quiz, Option
from review_quiz import forms
from users.models import KahUCUser
from review_quiz.models import Comment,CommentOption
from django.db.models import Q,F
from django.contrib.auth.models import Group
HOME_PAGE_URL = "/review_quiz/list_quizzes_waiting_for_approval"


@login_required
@permission_required('users.can_review_quiz', raise_exception=True)
def review_one_quiz(request, quiz_id):
    """View response to review a quiz."""
    # verificar se o quiz existe na base de dados
    try:
        quiz = Quiz.objects.get(id=quiz_id)
    except Quiz.DoesNotExist as exc:
        raise Http404 from exc
    user_id = request.user.id

    queri = Comment.objects.filter(approver=user_id,quiz=quiz_id,version=True)

    if len(queri) != 0:
        msgs.warning(request, "Já reveu este quiz")
        return redirect(HOME_PAGE_URL)

    # verificar se pode rever este quiz
    aprovadores = [quiz.approver1_id, quiz.approver2_id, quiz.approver3_id]
    if user_id not in aprovadores:
        msgs.warning(request, "Não tem permissões para rever este quiz")
        return redirect(HOME_PAGE_URL)
    # verificar se está à espera de revisão ou não
    if quiz.approval_state != 'À espera de revisão':
        msgs.warning(request, "O quiz especificado não aguarda revisão")
        return redirect('/review_quiz/list_quizzes_waiting_for_approval/')
    all_options = Option.objects.filter(quiz_id=quiz_id)
    comment = forms.ReviewForm()

    context = {
        'allOptions': all_options,
        'quiz': quiz,
        'form': comment,

    }
    if request.method == "POST":
        comment = forms.ReviewForm(request.POST)
        if comment.is_valid():
            comentario = comment.cleaned_data.get("comentario")
            comentarios_opcoes = []
            for i in range(6):
                key = "comentarioop" + str(i + 1)
                comentarios_opcoes.append(comment.cleaned_data.get(key))
            if comment.cleaned_data.get("aprovado"):
                aprovado = "True"
            else:
                aprovado = "False"
            edited = quiz.edited
            conta_aprovados = 0
            conta_reprovados = 0
            with connection.cursor() as cursor:
                if not edited:
                    max = Comment.objects.all().order_by("-id")[0]
                    max_id_comentario = max.id

                    if max_id_comentario is None:
                        max_id_comentario = 0
                    max_id_op = CommentOption.objects.all().order_by("-id")[0]
                    max_id_comentarioopcao = max_id_op.id

                    if max_id_comentarioopcao is None:
                        max_id_comentarioopcao = 0

                    Comment.objects.create(id=max_id_comentario + 1,comment=comentario,approval=aprovado,approver_id=user_id,version=True,quiz_id=quiz_id)



                    for i in range(6):
                        com = CommentOption()
                        com.id = max_id_comentarioopcao+1+i
                        com.comment = comentarios_opcoes[i]
                        com.approver_id = user_id
                        com.option_id = max_id_comentario + 1
                        com.save()





                else:
                    # query que retorna o objeto com o approvador, quiz e versao a false.(Versao antiga)
                    queri2 = Comment.objects.get(approver=user_id, quiz=quiz_id, version=False)


                    tipo_apro = queri2.approval         #tipo de aprovação antiga
                    max_id_comentarioopcao = queri2.id  #max_id_comentario final
                    print(tipo_apro,max_id_comentarioopcao)
                    if cursor.rowcount != 0:
                        # decrementa o conta_reprovados se este, rejeitou o quiz na versão passada
                        if not tipo_apro:
                            conta_reprovados -= 1
                            Comment.objects.filter(quiz=quiz_id,approver=user_id).update(version=True,approval=False)

                        else:
                            # decrementa o conta_aprovados se este,
                            # rejeitou o quiz na versão passada
                            conta_aprovados -= 1
                            Comment.objects.filter(quiz=quiz_id, approver=user_id).update(version=True, approval=True)

                    # update do comentario final do quiz
                    Comment.objects.filter(quiz=quiz_id,approver=user_id).update(version=True,approval=aprovado,comment=comentario)


                    for i in range(6):
                        if i == 5:
                            i = -1
                        # update dos comentarios das opções final do quiz
                        CommentOption.objects.annotate(id10=(F('id') % 6 - 1)).filter(id10=i,approver=user_id,option=max_id_comentarioopcao).update(comment=comentarios_opcoes[i])



                # verificação do tipo de revisão(aprovado, rejeitado) incrementar no quiz
                if aprovado == "True":
                    conta_aprovados += 1
                else:
                    conta_reprovados += 1
                num_a = quiz.num_approvals + conta_aprovados
                num_r = quiz.num_rejections + conta_reprovados

                # Update ao nº de aprovações e Rejeições
                Quiz.objects.filter(id=quiz_id).update(num_approvals=num_a)
                Quiz.objects.filter(id=quiz_id).update(num_rejections=num_r)


                aprovador1 = quiz.approver1_id
                aprovador2 = quiz.approver2_id
                aprovador3 = quiz.approver3_id

                # verifica se os 3 aprovadores já reveram o quiz editado
                q = Comment.objects.filter(Q(approver=aprovador1,quiz_id=quiz_id,version=True)
                                           | Q(approver=aprovador2,quiz_id=quiz_id,version=True)
                                           | Q(approver=aprovador3,quiz_id=quiz_id,version=True)).values()

                # Se não for um quiz editado ou se os 3 aprovadores ja reveram o quiz editado
                # Update consoante o numero de aprovações/rejeições
                               
                if len(q) == 3 or not edited:
                    if num_a == 3:
                        #
                        Quiz.objects.filter(id=quiz_id).update(approval_state='Aprovado')

                    elif num_r > 0 and num_r + num_a == 3:
                        Quiz.objects.filter(id=quiz_id).update(approval_state='Reprovado')

                    else:
                        Quiz.objects.filter(id=quiz_id).update(approval_state='À espera de revisão')


                # verifica permissões aos revisores
                verificapermissoes(aprovador1)
                verificapermissoes(aprovador2)
                verificapermissoes(aprovador3)
                mudapermissao(quiz_id=quiz_id)

        return redirect(HOME_PAGE_URL)
    return render(request, "review_quiz.html", context)


def mudapermissao(quiz_id):
    """Function to update creator permission to reviewer"""
    #Query que mostra o numero de quizzes ja aprovados de um certo criador

    QuizAproved = Quiz.objects.get(id=quiz_id)

    QuizesAprovados = Quiz.objects.filter(creator_id=QuizAproved.creator_id,approval_state='Aprovado')

    #se o criador ja tiver aprovados 3 quizzes criados por ele, recebe permissao de reviewer

    user = KahUCUser.objects.get(id=QuizAproved.creator_id)
    if len(QuizesAprovados) == 3:
        user.groups.clear()
        rev = Group.objects.get(name='Reviewer')
        user.groups.add(rev)




def verificapermissoes(reviewer_id):
    """Function to update permissions of a reviewer"""
    # Query que tem as linhas de todos os quizzes aprovado a que um revisor reveu.
    QuizGeral = Quiz.objects.filter(Q(approver1=reviewer_id, approver2=reviewer_id, approver3=reviewer_id, _connector=Q.OR),
                                    approval_state='Aprovado')
    user = KahUCUser.objects.get(id=reviewer_id)
    if len(QuizGeral)==3:
        user.groups.clear()
        rev = Group.objects.get(name='Solver')

        user.groups.add(rev)


@login_required
@permission_required('users.can_review_quiz', raise_exception=True)
def listar_quizzes_a_aprovar_asc(request):
    """View to list quizzes to pass in ascending order"""
    user_id = request.user.id

    query_list_asc = Quiz.objects.filter(
        Q(approver1=user_id, approver2=user_id, approver3=user_id, _connector=Q.OR),
        edited=False, approval_state='À espera de revisão').order_by('-creation_date')
    QuizzesQueReveu = Comment.objects.filter(approver=user_id).values('quiz')

    listaQuizzesPorRever = list()
    contador = 0
    # verificação se já editou ou não
    for q in query_list_asc:
        for que in QuizzesQueReveu:
            if q.id == que['quiz']:
                contador += 1

        if contador == 0 and q not in listaQuizzesPorRever:
            listaQuizzesPorRever.append(q)
        contador = 0

    context = {
        'all': listaQuizzesPorRever,
        'length': len(listaQuizzesPorRever),
        'oldest': 0,
        'id': user_id,
    }
    return render(request, "listar_quizzes_a_aprovar.html", context)


@login_required
@permission_required('users.can_review_quiz', raise_exception=True)
def listar_quizzes_a_aprovar_ordenados_desc(request):
    """View to list quizzes to aprove in descending order"""
    user_id = request.user.id

    query_list_desc = Quiz.objects.filter(
        Q(approver1=user_id, approver2=user_id, approver3=user_id, _connector=Q.OR),
        edited=False, approval_state='À espera de revisão').order_by('creation_date')
    QuizzesQueReveu = Comment.objects.filter(approver=user_id).values('quiz')


    listaQuizzesPorRever = list()
    contador = 0
    # verificação se já editou ou não
    for q in query_list_desc:
        for que in QuizzesQueReveu:
            if q.id == que['quiz']:
                contador+=1

        if contador == 0 and q not in listaQuizzesPorRever:
            listaQuizzesPorRever.append(q)
        contador = 0








    context = {
        'all': listaQuizzesPorRever,
        'length': len(listaQuizzesPorRever),
        'oldest': 1,
        'id': user_id,
    }
    return render(request, "listar_quizzes_a_aprovar.html", context)


@login_required
@permission_required('users.can_review_quiz', raise_exception=True)
def listar_quizzes_editados(request):
    """View to list quizzes edited by creator in state 'Waiting to review' """
    user_id = request.user.id

    QuizzesPorEdit = Comment.objects.filter(approver=user_id,version=False).values('quiz','approval').order_by('quiz')
    listaQuizzes = list()
    for quizPorEdit in QuizzesPorEdit:
        QueryEdited = Quiz.objects.get(id=quizPorEdit['quiz'],edited=True)
        quiz = Quiz(id=quizPorEdit['quiz'],description=QueryEdited.description,
                    num_approvals=QueryEdited.num_approvals,num_rejections=QueryEdited.num_rejections,
                    tags=QueryEdited.tags)
        quiz.approval = quizPorEdit['approval']
        listaQuizzes.append(quiz)


    context = {
        'all': listaQuizzes,
        'length': len(listaQuizzes),
        'aproved': 0,
        'id': user_id,
    }
    return render(request, "listar_quizzes_a_aprovar.html", context)


@login_required
@permission_required('users.can_review_quiz', raise_exception=True)
def listar_quizzes_aprovados(request):
    """View to list quizzes in state approved, (approved by reviewer)"""
    user_id = request.user.id

    all_quizzes = Quiz.objects.filter(Q(approver1=user_id,approver2=user_id,approver3=user_id,_connector=Q.OR),approval_state='Aprovado')
    context = {
        'all': all_quizzes,
        'length': len(all_quizzes),
        'aproved': 1,
        'id': user_id,
    }
    return render(request, "listar_quizzes_a_aprovar.html", context)

#--------------------------------------------