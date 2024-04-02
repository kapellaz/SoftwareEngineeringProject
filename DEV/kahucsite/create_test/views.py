"""This file have all views about user-story: create test."""
# pylint: disable=E1101
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from django.contrib import messages as msgs
from quiz.models import Tag, Quiz
from create_test import forms
from create_test.models import Teste

HOME_PAGE_URL = "/home/"

@login_required
#@permission_required('users.can_create_test', raise_exception=True)
@permission_required('users.can_review_quiz', raise_exception=True)
def create_test(request):
    """Função que permite a criação dos testes"""
    user_id = request.user.id
    mensagem = ""
    number_quest = 20

    test_form = forms.CreateTestForm()

    tags_names = list(Tag.objects.values_list('name',flat=True))
    tags_ids = list(Tag.objects.values_list('id',flat=True))

    test_form.labels(tags_names)

    context = {
        'test_form': test_form,
        'tags':Tag.objects.all()
    }

    if request.method == "POST":
        test_form = forms.CreateTestForm(request.POST)
        if test_form.is_valid():
            title = test_form.cleaned_data.get("title")
            if len(title) > 200:
                mensagem+='Erro, o titulo demasiado longo 😨. \n'
                msgs.warning(request,mensagem)
                return render(request, "create_test.html", context)
            selecionados = {}
            for i in range(len(tags_names)):
                name = "tag"+str(i+1)
                result = test_form.cleaned_data.get(name)
                if result:
                    selecionados[tags_names[i]] = tags_ids[i]
        teste_nome = Teste.objects.filter(name = title)
        num_rep = len(teste_nome)
        if num_rep>0:
            mensagem+='Erro, o titulo já existe 😨. \n'
            msgs.warning(request,mensagem)
            return render(request, "create_test.html", context)
        num_tags = len(selecionados)
        if num_tags == 0:
            mensagem+='Erro, 0 tags selecionadas 😨. \n'
        else:
            tag_quizzes = {}
            #buscar a base de dados os numeros de testes por tags e os seus ids
            for key in selecionados.keys():
                tag_quizzes[selecionados[key]]= list(Quiz.objects.filter(uses__gt=0,
                                                     tags_id = selecionados[key],
                                                     approval_state = 'Aprovado').values_list(
                                                     'id',flat=True))

            total_quizzes = 0
            contagem = {}
            for key,values in tag_quizzes.items():
                contagem[key] = len(values)
                total_quizzes += len(values)

            if total_quizzes<20:
                mensagem+= "Não foi possível criar o teste 😒 (tags selecionadas tinham "+str(total_quizzes)+" quizzes disponíveis). "
            else:
                selected_quizzes = {}
                for id in tag_quizzes.keys():
                    selected_quizzes[id] = list()
                keys_selecionados = list(tag_quizzes.keys())
                atual = 0
                key = keys_selecionados[atual]
                inseridos = 0
                while inseridos != number_quest:
                    if len(tag_quizzes[key]) > 0:
                        selected_quizzes[key].append(tag_quizzes[key][0])
                        tag_quizzes[key].pop(0)
                        inseridos+=1
                    atual += 1
                    if atual == len(keys_selecionados):
                        atual = 0
                    key = keys_selecionados[atual]
                print("por no teste os quizzes: ",selected_quizzes)
                mensagem+="Teste criado 😀\n"
                for key in selected_quizzes.keys():
                    mensagem+=tags_names[key-1]+": "+str(len(selected_quizzes[key]))+" utilizados. "

                teste = Teste.objects.create(name = title,creator_id = user_id)
                for key in selected_quizzes.keys():
                    cria = Tag.objects.get(id = key)
                    teste.tags.add(cria)
                    for i in range(len(selected_quizzes[key])):
                        quizze = Quiz.objects.get(id = selected_quizzes[key][i])
                        Quiz.objects.filter(id=selected_quizzes[key][i]).update(uses=quizze.uses-1)
                        teste.quizzes.add(quizze)
                teste.save()
        msgs.warning(request,mensagem)
    return render(request, "create_test.html", context)
