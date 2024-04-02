from django.contrib.auth.decorators import login_required, permission_required
from django.core import serializers
from django.http import Http404
from django.shortcuts import render, redirect
from quiz.models import Quiz, Option
from create_test.models import Teste
from test_results.models import Answer
from users.models import KahUCUser


@login_required
@permission_required('users.can_solve_test', raise_exception=True)
def select_test_view(request):
    """Mostra todos os testes disponíveis para resolver.

    **Template:**
    :template:`solve_test/select_test.html`
    """

    all_tests = Teste.objects.values('id', 'name')

    context = {
        'all_tests': all_tests,
    }

    return render(request, "select_test.html", context)


@login_required
@permission_required('users.can_solve_test', raise_exception=True)
def test_redirect_view(request, test_id):
    """Encontra os quizzes de um teste e redireciona para a resolução."""
    # quiz_index = 0 #ira servir para navegar entre quizzes num teste

    try:
        test = Teste.objects.get(id=test_id)
    except Teste.DoesNotExist:
        raise Http404

    try:
        quizzes = [quiz['id'] for quiz in Quiz.objects.filter(teste=test_id).values('id')]
    except Quiz.DoesNotExist:
        raise Http404

    request.session['quiz_list'] = quizzes
    request.session['test_choices'] = [0 for _ in request.session['quiz_list']]  # lista para Answers
    request.session['choices_ids'] = [0 for _ in request.session['quiz_list']]  # lista para Answers ids

    #print(request.session['quiz_list'])
    #print(request.session['test_choices'])
    #print(request.session['choices_ids'])

    return redirect(f"../../{test_id}/{request.session['quiz_list'][0]}/")


@login_required
@permission_required('users.can_solve_test', raise_exception=True)
def test_page_view(request, test_id, quiz_id):
    """Mostra um :model:`quiz.Quiz` individual.

    **Template:**
    :template:`solve_test/test_page.html`
    """

    """
    print(request.session['quiz_list'])
    print(request.session['test_choices'])
    print(request.session['quiz_list'].index(int(quiz_id)))
    """

    try:
        current_test = Teste.objects.get(id=test_id)
    except Teste.DoesNotExist:
        raise Http404

    try:
        current_quiz = Quiz.objects.get(id=quiz_id)
    except Quiz.DoesNotExist:
        raise Http404

    quiz_index = request.session['quiz_list'].index(int(quiz_id))

    if request.method == "POST":

        if "quit" in request.POST:
            return redirect("/solve_test/")

        item_list = request.POST.getlist('item_checkbox')
        user_id = KahUCUser.objects.get(id=request.user.id)

        try:
            selection = serializers.deserialize('xml', request.session['test_choices'][quiz_index])
            # update da resposta selecionada
            if item_list:
                opt = Option.objects.get(id=item_list[0])
                selection.update(option=opt)
                request.session['choices_ids'][quiz_index] = item_list[0]
            else:
                selection.update(option=None)
                request.session['choices_ids'][quiz_index] = 0

        except AttributeError:  # user ainda nao tinha respondido ao quiz
            if item_list:
                opt = Option.objects.get(id=item_list[0])
                selection = Answer(test=current_test, quiz=current_quiz, user=user_id, option=opt)
                request.session['choices_ids'][quiz_index] = item_list[0]
            else:
                selection = Answer(test=current_test, quiz=current_quiz, user=user_id)
                request.session['choices_ids'][quiz_index] = 0

        request.session['test_choices'][quiz_index] = serializers.serialize('xml', [selection])
        #print(serializers.serialize('xml', [selection]))
        #print(request.session['test_choices'])

        if 'next-quiz' in request.POST:
            return redirect(f"../../{test_id}/{request.session['quiz_list'][quiz_index + 1]}/")
        elif 'prev-quiz' in request.POST:
            return redirect(f"../../{test_id}/{request.session['quiz_list'][quiz_index - 1]}/")

        elif 'submit-test' in request.POST:
            for submission in request.session['test_choices']:
                for obj in serializers.deserialize('xml', submission):
                    obj.save()

            return redirect('/results/')

    # else:  # user entrou na página
    opcoes = Option.objects.filter(quiz_id=quiz_id).values
    info_quiz = Quiz.objects.filter(id=quiz_id).values('id', 'description', 'question')

    # print(request.session['choices_ids'])

    context = {
        'opcoes': opcoes,
        'info_quiz': info_quiz,
        'previous_quiz': request.session['quiz_list'].index(int(quiz_id)) - 1,
        'next_quiz': request.session['quiz_list'].index(int(quiz_id)) + 1,
        'last_quiz': len(request.session['quiz_list']),
        'temp_choice': int(request.session['choices_ids'][quiz_index])
    }

    return render(request, "test_page.html", context)
