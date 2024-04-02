"""This file have all views about user-story: create quizz."""
from django.http import Http404
from django.shortcuts import render, redirect
from .forms import NewQuizz
from .models import Quiz, Option, Tag
from users.models import KahUCUser
from django.contrib.auth.decorators import login_required
import xml.etree.ElementTree as xml_tree
from django.http import HttpResponse
import random


def insert_quiz(*args):
    """Insert in quiz table."""
    try:
        quiz = Quiz()
        quiz.creator = args[0]
        quiz.question = args[1]
        quiz.description = args[2]

        quiz.approver1 = args[3]
        quiz.approver2 = args[4]
        quiz.approver3 = args[5]

        quiz.approval_state = 'À espera de revisão'
        quiz.score = 0
        quiz.num_approvals = 0
        quiz.num_rejections = 0

        quiz.tags = args[6]

        quiz.save()

        return quiz
    except Exception:
        return None


def insert_option(*args):
    """Insert in alinea table."""
    try:
        option = Option()

        option.quiz = args[0]
        option.text = args[1]
        option.justification = args[2]
        option.selection = args[3]

        option.save()

        return option
    except Exception:
        return None


@login_required
def CreateQuizz(request):
    """View response to create a quizz."""
    primary_key = request.user.id

    usr_obj = KahUCUser.objects.filter(id=primary_key)[0]
    reviewers = KahUCUser.objects.filter(groups__gte=2)

    len_reviewers = len(reviewers)
    if usr_obj in reviewers:
        len_reviewers -= 1
    if len_reviewers < 3:
        raise Http404("Numero de revisores insuficiente! Não existem 3 "
                      "revisores diferentes para aprovar um quiz.")

    random_nums = []
    i = 0
    while i < 3:
        rand = random.randint(0, len(reviewers) - 1)
        if rand not in random_nums and reviewers[rand].id != usr_obj.id:
            random_nums.append(rand)
            i += 1
    reviewer1 = reviewers[random_nums[0]]
    reviewer2 = reviewers[random_nums[1]]
    reviewer3 = reviewers[random_nums[2]]

    new_quizz = NewQuizz()

    if request.method == 'POST':
        new_quizz = NewQuizz(request.POST or None)

        if new_quizz.is_valid():
            quizz = new_quizz.cleaned_data

            tag_obj = Tag.objects.filter(id=quizz['tag'])[0]

            quiz = insert_quiz(usr_obj, quizz['question'],
                               quizz['description'], reviewer1, reviewer2,
                               reviewer3, tag_obj)
            insert_option(quiz, quizz['answer1'], quizz['reason1'],
                          quizz['option1'])
            insert_option(quiz, quizz['answer2'], quizz['reason2'],
                          quizz['option2'])
            insert_option(quiz, quizz['answer3'], quizz['reason3'],
                          quizz['option3'])
            insert_option(quiz, quizz['answer4'], quizz['reason4'],
                          quizz['option4'])
            insert_option(quiz, quizz['answer5'], quizz['reason5'],
                          quizz['option5'])
            insert_option(quiz, quizz['answer6'], quizz['reason6'],
                          quizz['option6'])

            # sucess case
            return redirect("../historic_quiz/")

        # not valid
        context = {
            'form': new_quizz,
            'errors': new_quizz.errors['__all__']
        }
        return render(request, 'create_quiz.html', context)

    context = {
        'form': new_quizz,
    }

    return render(request, 'create_quiz.html', context)


def generate_xml(quiz_id_list):
    """Gerar XML."""
    filename = "teste.xml"
    root = xml_tree.Element('quizzes')

    c1 = xml_tree.Element("perguntas")
    root.append(c1)

    for x in quiz_id_list:
        quiz = Quiz.objects.get(id=x)
        c2 = xml_tree.SubElement(c1, "pergunta")

        c3 = xml_tree.SubElement(c2, "tag")
        c3.text = quiz.tags.name

        c4 = xml_tree.SubElement(c2, "descricao")
        c4.text = quiz.question

        c5 = xml_tree.SubElement(c2, "respostas")

        options = Option.objects.filter(quiz_id=x).values("text", "selection", "justification")
        for op in options:
            c6 = xml_tree.SubElement(c5, "resposta")
            c7 = xml_tree.SubElement(c6, "designacao")
            c7.text = op["text"]
            c7 = xml_tree.SubElement(c6, "valor_logico")
            if op["selection"]:
                c7.text = "True"
            else:
                c7.text = "False"
            c7 = xml_tree.SubElement(c6, "justificacao")
            c7.text = op["justification"]

    tree = xml_tree.ElementTree(root)
    with open(filename, "wb") as files:
        tree.write(files, encoding='utf-8', xml_declaration=True)
        files.close()

    with open(filename, "r", encoding="utf-8") as files:
        data = files.read()

    response = HttpResponse(data, content_type='text/xml')
    response['Content-Disposition'] = 'attachment; filename="quiz.xml"'

    return response


@login_required
def export_xml_site(request):
    """Export xml."""
    all_quizzes = Quiz.objects.filter(approval_state='Aprovado').values('id', 'description', 'question')

    context = {
        'all_quizzes': all_quizzes,
    }

    if request.method == "POST":
        response = generate_xml(request.POST.getlist("questions"))
        return response

    return render(request, 'export_XML.html', context)
