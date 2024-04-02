"""Vista do hall of fame para as quizzes e para os testes
é possível passar uma tag como query parameter e os resultados irão ser
filtrados
"""

# utilities
from django.shortcuts import render
from django.db.models import Count
from django.http import Http404

# user models
from users.models import KahUCUser
from quiz.models import Quiz, Tag, Option
from test_results.models import Answer
from create_test.models import Teste



# Create your views here.

def quiz_hall_of_fame(request):
    '''View da pagina de hall of fame relativamente a quiz

    Args:
        request (HTTPRequest): o pedido HTTP

    Raises:
        Http404: caso a tag passada como query param não exista ou um query param nao seja suportado

    Returns:
        HTTPResponse: a página de hall of fame dos quiz
    '''

    # parametros de query
    query_params = request.GET

    # verificar se foi passada uma tag
    if 'tags' in query_params:

        # caso seja passado um query param desconhecido
        if len(query_params) > 1:
            raise Http404('Página não encontrada')

        # caso a tag seja ALL nao filtrar os quizes
        if query_params['tags'] == 'ALL':
            tag_id = None
        else:
            # procurar a tag
            tag_id = Tag.objects.filter(
                name=query_params['tags']
            ).values_list('id', flat=True).first()

            # caso a tag nao exista
            if tag_id is None:
                raise Http404('Tag #' + query_params['tags'] + ' não existe.')

    else:

        # caso seja passado um query param desconhecido
        if len(query_params) > 0:
            raise Http404('Página não encontrada')

        tag_id = None


    # buscar os quizzes marcados com a tag pedida
    quizzes = Quiz.objects.filter(tags_id=tag_id).values_list('id', flat=True)

    # buscar as respostas certas
    options = Option.objects.filter(
        selection=True, quiz_id__in=quizzes
    ).values_list('id', flat=True)

    # buscar as respostas do user que estão certas e que pertencem a um quiz com a tag pedida
    answers = Answer.objects.filter(option_id__in=options).values_list('user_id', flat=True)


    # caso nao seja pedida uma tag
    if tag_id is None:
        # query para encontrar os users que tem quizes corretos
        users = KahUCUser.objects.all().exclude(number_of_correct_quizzes = 0)

        # query para encontrar os users com quizzes certos
        users_answers = users.order_by('-number_of_correct_quizzes').values_list(
            'username', 'number_of_correct_quizzes'
        )

    # caso contrario
    else:
        # users serao os que tem uma resposta certa dada
        users_ordered = KahUCUser.objects.filter(id__in=answers).values_list('username', flat=True)

        # agrupar as respostas
        grouped_answers = answers.values('user_id').annotate(
            num_answers=Count('user_id')
        ).values_list('num_answers', flat=True)

        users_answers = sorted(
            zip(users_ordered[:10], grouped_answers[:10]),
            key=lambda x: x[1],
            reverse=True
        )

    exist_ans = True if len(users_answers) else False

    # obter uma lista de tags
    tags = Tag.objects.all()

    context = {
        # para usar a mesma página de hall of fame
        'isTestHF': False,

        'tags': tags,

        'tag_id': tag_id,

        # os 10 users com mais quizzes acertados
        'users_answers': users_answers[:10],

        'exist_ans': exist_ans,
    }

    return render(request, 'hall_of_fame.html', context)




def test_hall_of_fame(request):
    '''View da pagina de hall of fame relativamente a testes completados

    Args:
        request (HTTPRequest): o pedido HTTP

    Raises:
        Http404: caso a tag passada como query param não exista ou um query param nao seja suportado

    Returns:
        HTTPResponse: a página de hall of fame dos testes
    '''


    # parametros de query
    query_params = request.GET

    # verificar se foi passada uma tag
    if 'tags' in query_params:

        # caso seja passado um query param desconhecido
        if len(query_params) > 1:
            raise Http404('Página não encontrada')

        # caso a tag seja ALL nao filtrar os quizes
        if query_params['tags'] == 'ALL':
            tag_id = None
        else:
            # procurar a tag
            tag_id = Tag.objects.filter(
                name=query_params['tags']
            ).values_list('id', flat=True).first()

            # caso a tag nao exista
            if tag_id is None:
                raise Http404('Tag #' + query_params['tags'] + ' não existe.')

    else:

        # caso seja passado um query param desconhecido
        if len(query_params) > 0:
            raise Http404('Página não encontrada')

        tag_id = None


    # caso a tag nao tenha sido passada ou seja ALL os
    # testes sao calculados pelo number_of_tests_done
    if tag_id is None:
        # query para encontrar os users que tem testes resolvidos
        users = KahUCUser.objects.all().exclude(number_of_tests_done = 0)

        # query para encontrar os testes feitos
        users_completed = users.order_by('-number_of_tests_done').values_list(
            'username', 'number_of_tests_done'
        )

    # caso contrário tem que ser feita outra query
    else:
        tests = Teste.objects.filter(tags=tag_id).values_list('id', flat=True)

        answers = Answer.objects.filter(test_id__in=tests)

        users = KahUCUser.objects.filter(
            id__in=answers.values_list('user_id', flat=True)
        ).values_list('username', flat=True)

        grouped_answers = answers.values('user_id').annotate(
            completed=Count('test_id')/20
        ).values_list('completed', flat=True)

        grouped_answers = grouped_answers.filter(completed__gt=0)

        # ordenar os objetos por numero de testes completados
        users_completed = sorted(
            zip(users[:10], grouped_answers[:10]),
            key=lambda x: x[1],
            reverse=True
        )

    exist_ans = True if len(users_completed) else False

    # obter uma lista de tags
    tags = Tag.objects.all()

    context = {
        # para usar a mesma página de hall of fame
        'isTestHF': True,

        'tags': tags,

        'tag_id': tag_id,

        # os 10 users com mais testes feitos
        'users_completed': users_completed,

        'exist_ans': exist_ans,
    }

    return render(request, 'hall_of_fame.html', context)
