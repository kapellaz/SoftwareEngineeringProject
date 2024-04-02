from django.http import Http404
from django.shortcuts import render, redirect
from users.models import KahUCUser
from quiz.models import Quiz, Option, Tag
from .forms import EditQuizzForms
from users.models import KahUCUser
from django.contrib.auth.decorators import login_required
from review_quiz.models import Comment, CommentOption
from django.db.models import Q
from django.db import connection


@login_required()
# http://127.0.0.1:8000/historic_quiz/
def list_quizzs(request):
    """Função que mostra os Quizz's criados por um utilizador"""

    pk = request.user.id

    quiz_obj = Quiz.objects.filter(creator=pk).order_by('id')

    context = {
        'quizzs': quiz_obj
    }

    return render(request, 'Listar_Quizzs.html', context)


@login_required()
# http://127.0.0.1:8000/historic_quiz/quiz=<str:pk>
def details_quiz(request, pk_quiz):
    """Função que mostra os detalhes de um Quiz criado por um dado utilizador"""

    pk = request.user.id

    exist = Quiz.objects.filter(id=pk_quiz)
    options = []
    quiz_obj = Quiz.objects.filter(creator=pk, id=pk_quiz)
    edited = False
    if quiz_obj:
        for quiz in quiz_obj:
            option_obj = Option.objects.filter(quiz_id=quiz.id).order_by('id')
            options.append(option_obj)

        if (quiz.approval_state == 'Reprovado'):
            edited = True
    else:
        if exist:
            # se o quiz existir e o quiz_obj nao, nao foi este user que criou o quiz
            # logo nao pode editar este quiz
            return render(request, 'UserNotQuiz.html')
        return render(request, 'QuizNotFound.html')
    context = {
        'quizzs': quiz_obj, 'Opcoes': options, 'edit': edited,
    }

    return render(request, 'Quiz_Detalhes.html', context)


@login_required()
# http://127.0.0.1:8000/historic_quiz/quiz=<str:pk>/edit
def edit_quiz(request, pk_quiz):
    """Função que permite editar um quiz"""

    pk = request.user.id

    exist = Quiz.objects.filter(id=pk_quiz)
    quiz_obj = Quiz.objects.filter(creator=pk, id=pk_quiz)

    if (len(quiz_obj) != 0):
        quiz_obj = quiz_obj[0]

    if ((quiz_obj.approval_state == 'Aprovado') or (quiz_obj.approval_state == 'À espera de revisão' and quiz_obj.num_rejections <= 0)):
        raise Http404("Nao pode editar este Quiz!")

    quiz_form = EditQuizzForms()

    options = []

    if quiz_obj:
        options = Option.objects.filter(quiz_id=pk_quiz).order_by('id')

    else:
        if exist:
            # se o quiz existir e o quiz_obj nao, nao foi este user que criou o quiz
            # logo nao pode editar este quiz
            return render(request, 'UserNotQuiz.html')
        return render(request, 'QuizNotFound.html')

    dic = {
        'question': quiz_obj.question,
        'description': quiz_obj.description,
        'option1': options[0].text,
        'description1': options[0].justification,
        'field1': options[0].selection,
        'option2': options[1].text,
        'description2': options[1].justification,
        'field2': options[1].selection,
        'option3': options[2].text,
        'description3': options[2].justification,
        'field3': options[2].selection,
        'option4': options[3].text,
        'description4': options[3].justification,
        'field4': options[3].selection,
        'option5': options[4].text,
        'description5': options[4].justification,
        'field5': options[4].selection,
        'option6': options[5].text,
        'description6': options[5].justification,
        'field6': options[5].selection,
        'tag': quiz_obj.tags.id
    }
    aprovadores = [quiz_obj.approver1_id,
                   quiz_obj.approver2_id, quiz_obj.approver3_id]
    # Coloca comentarios finais dos quizzs que foram reprovados por ordem dos revisores que reprovaram o quiz
    comments_final = Comment.objects.filter(
        approver_id__in=aprovadores, quiz_id=pk_quiz).order_by('approver')
    count = comments_final.count()
    # print(count)
    # print(comments_final)
    # Coloca comentarios das opcoes por ordem dos revisores que reprovaram o quiz por ordem do id deles e por ordem das opcoes
    if (count == 1):
        comments_options = CommentOption.objects.filter(
            option=(comments_final[0].id)).order_by('approver', 'id')
    elif (count == 2):
        comments_options = CommentOption.objects.filter(Q(option=(comments_final[0].id))
                                                        | Q(option=(comments_final[1].id))).order_by('approver', 'id')
    else:
        comments_options = CommentOption.objects.filter(Q(option=(comments_final[0].id))
                                                        | Q(option=(comments_final[1].id))
                                                        | Q(option=(comments_final[2].id))).order_by('approver', 'id')
    # print(comments_options)
    # count=comments_options.count()
    # print(count)
    options1 = []
    options2 = []
    options3 = []
    options4 = []
    options5 = []
    options6 = []
    options1.append(comments_options[0])
    options1.append(comments_options[6])
    options1.append(comments_options[12])
    options2.append(comments_options[1])
    options2.append(comments_options[7])
    options2.append(comments_options[13])
    options3.append(comments_options[2])
    options3.append(comments_options[8])
    options3.append(comments_options[14])
    options4.append(comments_options[3])
    options4.append(comments_options[9])
    options4.append(comments_options[15])
    options5.append(comments_options[4])
    options5.append(comments_options[10])
    options5.append(comments_options[16])
    options6.append(comments_options[5])
    options6.append(comments_options[11])
    options6.append(comments_options[17])
    error = ""
    # Chamar o metodo POST para
    if request.method == 'POST':
        quiz_form = EditQuizzForms(request.POST or None)

        # Este valid e necessario por alguma razao - https://www.youtube.com/watch?v=a6k4AemUHQA&ab_channel=CodeShika
        if quiz_form.is_valid():
            quiz_form = quiz_form.cleaned_data
            Option1 = options[0]
            Option2 = options[1]
            Option3 = options[2]
            Option4 = options[3]
            Option5 = options[4]
            Option6 = options[5]

            # Atualizar os quiz e opcoes com os novos valores
            quiz_obj.question = quiz_form['question']
            quiz_obj.description = quiz_form['description']
            Option1.text = quiz_form['option1']
            Option1.justification = quiz_form['description1']
            Option1.selection = quiz_form['field1']
            Option2.text = quiz_form['option2']
            Option2.justification = quiz_form['description2']
            Option2.selection = quiz_form['field2']
            Option3.text = quiz_form['option3']
            Option3.justification = quiz_form['description3']
            Option3.selection = quiz_form['field3']
            Option4.text = quiz_form['option4']
            Option4.justification = quiz_form['description4']
            Option4.selection = quiz_form['field4']
            Option5.text = quiz_form['option5']
            Option5.justification = quiz_form['description5']
            Option5.selection = quiz_form['field5']
            Option6.text = quiz_form['option6']
            Option6.justification = quiz_form['description6']
            Option6.selection = quiz_form['field6']
            quiz_obj.approval_state = 'À espera de revisão'
            quiz_obj.edited = True
            tag = Tag.objects.get(id=quiz_form['tag'])
            quiz_obj.tags = tag

            rever = Comment.objects.filter(
                approver_id__in=aprovadores, quiz_id=pk_quiz)

            count = rever.count()
            if count != 3:
                raise Http404

            quiz_obj.save()
            Option1.save()
            Option2.save()
            Option3.save()
            Option4.save()
            Option5.save()
            Option6.save()

            Comment.objects.filter(quiz_id=pk_quiz).update(version=False)

            return redirect(f"/historic_quiz/")
        error = quiz_form.errors['__all__'][0]
        context = {
            'quiz': quiz_obj,
            'form': quiz_form,
            'errors': error,
            'comments_final': comments_final,
            'options1': options1,
            'options2': options2,
            'options3': options3,
            'options4': options4,
            'options5': options5,
            'options6': options6,
        }
        print(context['errors'])
    quiz_form = EditQuizzForms(initial=dic)

    if quiz_form.is_valid():
        quiz_form.save()
    context = {
        'quiz': quiz_obj,
        'form': quiz_form,
        'errors': error,
        'comments_final': comments_final,
        'options1': options1,
        'options2': options2,
        'options3': options3,
        'options4': options4,
        'options5': options5,
        'options6': options6,
    }

    return render(request, 'Editar_Quiz.html', context)
