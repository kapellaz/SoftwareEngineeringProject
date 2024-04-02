from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect
# models
from create_test.models import Teste
from .models import Answer


@login_required
@permission_required('users.can_solve_test', raise_exception=True)
def test_results(request):
    """Mostra a página de ver resultados do quiz

    Para aceder à pagina usar results/viewresults

    Args:
        request (HttpRequest): o HttpRequest feito

    Returns:
        HttpResponse: Uma resposta Http com a página html
    """

    # buscar a ultima resposta dada pelo user
    user_last_answer = Answer.objects.filter(user_id=request.user.id).last()

    # ter a certeza que o utilizador tem respostas
    if user_last_answer is not None:
        user_last_test = Teste.objects.filter(id=user_last_answer.test_id).last()
    else:
        user_last_test = None

    # definir as variaveis de score
    test_max_score = 0
    user_test_score = 0

    # calcular o max score possivel e o score do user
    if user_last_test is not None:

        # iterar pelos quiz do ultimo teste do user
        for quiz in user_last_test.quizzes.all():

            # filtrar a resposta e verificar se é a correta na tabela Opcao
            user_answer = Answer.objects.filter(quiz_id=quiz.id, user_id=request.user.id, test_id=user_last_test.id).last()

            # verificar se o user respondeu ao quiz
            if user_answer.option:

                # adicionar a pontuacao do quiz
                test_max_score += quiz.score

                # adicionar o score ao user
                if user_answer.option and user_answer.option.selection:
                    user_test_score += quiz.score

    if user_last_test:
        if test_max_score != 0:
            perc_score = (user_test_score / test_max_score) * 100
        else:
            perc_score = 0
        # variaveis de contexto do html
        context = {
            'user': request.user,  # contem a info do user logado
            'test': user_last_test,  # ultimo teste feito pelo user logado
            # respostas dos quizes do ultimo teste feito pelo user
            'answers': Answer.objects.filter(user=request.user.id, test_id=user_last_test.id).distinct("quiz_id").order_by("quiz_id", "-id"),
            'test_max_score': test_max_score,  # pontuacao maxima possivel no teste
            'score': user_test_score,  # pontuacao do user no teste
            'perc_score': int(perc_score)  # pontuacao do user no teste
        }
        return render(request, "test_results.html", context)

    return redirect("/home/")
