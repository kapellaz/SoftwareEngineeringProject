import random
import xml.etree.ElementTree as ET

from django.contrib import messages
from django.contrib.auth import login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import Group
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.db.models import Count
from django.http import Http404
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from quiz.models import Quiz, Option, Tag
from test_results.models import Answer
from . import forms
from .forms import SetNewPassword, ImportXMLForm
from .models import KahUCUser
from .tokens import account_activation_token


def register(request):
    """
    View para registo de utilizadores
    :param request: request HTML
    :return: página de registo
    """
    # Utilizador está com a sessão iniciada e vai direto para a página home
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        form = forms.RegisterUser(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            creator_group = Group.objects.get(name='Creator')
            user.groups.add(creator_group)
            activate_email_for_register(request, user, user.username)
            return redirect('register')
        else:
            for message in form.errors:
                print(message)
                messages.error(request, form.errors.get(message))
    else:
        form = forms.RegisterUser()
    return render(request, 'register.html', {'form': form})


def activate_email_for_register(request, user, email):
    """
    View para a confirmação de email
    :param request: request HTML
    :param user: utilizador
    :param email: email de destino
    """
    email_subject = "Ative a sua conta KahUC"
    message = render_to_string("activate_account.html", {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        'protocol': 'https' if request.is_secure() else 'http'
    })
    email_send = EmailMessage(email_subject, message, to=[email])
    if email_send.send():
        messages.success(request, f'Por favor, verifique  email |{email}|')
    else:
        messages.error(request, f'Erro ao enviar email para |{email}|, verifique se está correto')


def activate(request, uidb64, token):
    """
    Atualiza o utilizador como confirmado para prosseguir para o login
    :param request: request HTML
    :param uidb64: id utilizador encoded
    :param token: token
    :return: pagina de login
    """
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None:
        if account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            messages.success(request, "Email confirmado! Podes prosseguir para o login!")
            return redirect('login')
        else:
            user.delete()
            messages.error(request, "Link de ativação expirou!")
    return redirect('register')


def confirm(request):
    """
    View para confirmação de email do utilizador (depois do registo)
    :param request: request HTML
    :return:
    """
    return render(request, 'confirm.html')


def login_page(request):
    """
    Função para validar as credenciais inseridas, verificar se o user tem a sessao iniciada
    :param request: resquest HTML
    :return: pagina login ao abrir
    :return pagina home caso credenciais estejam corretas ou ja esteja com sessao iniciada
    """
    # Utilizador está com a sessão iniciada e vai direto para a página home
    if request.user.is_authenticated:
        return redirect('home')
    context = {}
    # nao esta logado, vamos verificar o que foi inserido
    if request.method == 'POST':
        context = {'data': request.POST}
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember_me')
        # user = authenticate(username=username, password=password)
        try:
            user = KahUCUser.objects.get(username=username)
            if not user.check_password(password):
                user = None
        except:
            user = None
        if user is not None:
            if not user.is_active:
                messages.add_message(request, messages.ERROR,
                                     'Email não está confirmado, por favor verifique o seu inbox')
                return render(request, 'login.html', context)
            login(request, user)
            if not remember_me:
                request.session.set_expiry(0)

            return redirect('home')
        else:
            messages.info(request, 'Credenciais Erradas')

    return render(request, 'login.html', context)


def reset_password_get_email(request):
    """
        View para obtenção do email do utilizador
        :param request: request HTML
        :return:
    """
    form = PasswordResetForm(request.POST)
    if form.is_valid():
        email = form.cleaned_data['email']
        try:
            user = KahUCUser.objects.get(username=email)
        except:
            user = None
        if user is not None:
            activate_email_for_password_reset(request, user, user.username)
        else:
            messages.info(request, 'Não existe um utilizador com esse email associado')

    form = PasswordResetForm()
    return render(request, 'reset_password_get_email.html', {"form": form})


def activate_email_for_password_reset(request, user, email):
    """
    View para a confirmação de email (para a recuperação de palavra-passe)
    :param request: request HTML
    :param user: utilizador
    :param email: email de destino
    """
    email_subject = "Recupere a palavra-passe da sua conta KahUC"
    message = render_to_string("password_reset_template.html", {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        'protocol': 'https' if request.is_secure() else 'http'
    })
    email_send = EmailMessage(email_subject, message, to=[email])
    if email_send.send():
        messages.success(request, f'Por favor, verifique  email |{email}|')

    else:
        messages.error(request, f'Erro ao enviar email para |{email}|, verifique se está correto')


# , uidb64, token
def change_password_from_reset(request, uidb64, token):
    User = get_user_model()

    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        if request.method == 'POST':
            form = SetNewPassword(user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "A password foi alterada com sucesso! Pode prosseguir para o login!")
                return redirect('login')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)
        form = SetNewPassword(user)
        return render(request, 'password_reset.html', {'form': form})
    else:
        messages.error(request, "Link expirou!")
    messages.error(request, 'Algo correu mal, redirecionando para a homepage')
    return redirect("")

    # return render(request, 'password_reset.html')


def logout_view(request):
    logout(request)
    return redirect("/home/")


@login_required
def importxml(request):
    if request.method == 'POST':
        form = ImportXMLForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES.get('file')
            xml_string = file.read().decode('utf-8')

            reviewers = KahUCUser.objects.filter(groups__gte=2)
            len_reviewers = len(reviewers)
            if request.user in reviewers:
                len_reviewers -= 1
            if len_reviewers < 3:
                raise Http404(
                    "Numero de revisores insuficiente! Não existem 3 revisores diferentes para aprovar um quiz.")

            try:
                erro = False
                root = ET.fromstring(xml_string)
                for pergunta in root[0]:
                    random_nums = []
                    i = 0
                    while i < 3:
                        rand = random.randint(0, len(reviewers) - 1)
                        if rand not in random_nums and reviewers[rand].id != request.user.id:
                            random_nums.append(rand)
                            i += 1
                    reviewer1 = reviewers[random_nums[0]]
                    reviewer2 = reviewers[random_nums[1]]
                    reviewer3 = reviewers[random_nums[2]]

                    quiz = Quiz()
                    quiz.creator = request.user

                    desc = pergunta.find('descricao')
                    if desc is None:
                        messages.error(request, "Pergunta sem descrição")
                        erro = True
                        break
                    quiz.question = desc.text
                    quiz.description = desc.text

                    tag = pergunta.find('tags')
                    if tag is None or tag[0] is None:
                        messages.error(request, "Pergunta sem tag")
                        erro = True
                        break

                    quiz.tags = Tag.objects.filter(name=tag[0].text)[0]

                    quiz.score = 0
                    quiz.num_approvals = 0
                    quiz.num_rejections = 0

                    quiz.approver1 = reviewer1
                    quiz.approver2 = reviewer2
                    quiz.approver3 = reviewer3

                    quiz.approval_state = 'À espera de revisão'
                    quiz.save()

                    for resposta in pergunta.find('respostas').findall('resposta'):
                        option = Option()
                        option.quiz = quiz

                        designacao = resposta.find('designacao')
                        if designacao.text is None:
                            option.text = ""
                        else:
                            option.text = designacao.text

                        valor_logico = resposta.find('valor_logico')
                        if valor_logico.text is None or valor_logico.text.lower() not in ['true', 'false']:
                            option.valor_logico = False
                        else:
                            option.selection = valor_logico.text == 'True'

                        justificacao = resposta.find('justificacao')
                        if justificacao.text is None:
                            option.justification = ""
                        else:
                            option.justification = justificacao.text

                        option.save()
            except:
                messages.error(request, "Erro ao ler ficheiro")
                erro = True
            if not erro:
                return redirect("/historic_quiz/")
        else:
            for message in form.errors:
                print(message)
                if message == 'file':
                    messages.error(request, "Só são aceites ficheiros do tipo .xml")
                else:
                    messages.error(request, form.errors.get(message))
    else:
        form = ImportXMLForm()
    return render(request, 'importxml_temp.html', {'form': form})


@login_required
def profile(request):
    """
    Apresenta o perfil do utilizador
    :param request: request HTML
    :return:
    """

    num_my_quizzes = len(Quiz.objects.filter(creator=request.user.pk))
    num_my_quizzes_approved = len(Quiz.objects.filter(creator=request.user.pk, approval_state="Aprovado"))

    if num_my_quizzes == 0:
        approved = 0
    else:
        approved = int(num_my_quizzes_approved / num_my_quizzes * 100)

    # buscar answers realizadas pelo user
    all_answers = Answer.objects.filter(user_id=request.user.id).values_list('id', flat=True)

    # buscar os quizzes respondidos pelo user
    all_quizzes = Quiz.objects.filter(id__in=all_answers).values("tags_id").annotate(count_tag=Count("tags_id"))

    # buscar o número de respostas corretas total
    options = Option.objects.filter(selection=True).values_list('id', flat=True)

    # buscar as anwsers corretas respondidas pelo user
    correct_answers = Answer.objects.filter(user_id=request.user.id, option_id__in=options).values_list('id', flat=True)

    # buscar os quizzes por tag respondidos corretamente pelo user
    correct_quizzes = Quiz.objects.filter(id__in=correct_answers).values("tags_id").annotate(count_tag=Count("tags_id"))

    correct_tags = {}

    for i in list(correct_quizzes.values_list("tags_id", "count_tag")):
        correct_tags[i[0]] = i[1]

    all_tags = {k: 0 for k in range(1, 13)}
    count = 0

    for i in list(all_quizzes.values_list("tags_id", "count_tag")):
        all_tags[i[0]] = i[1]
        count += i[1]

    percentage_of_correct_tag = [0 for _ in range(12)]
    last_percentage = 0

    for i in range(1, 13):
        if i in list(correct_tags.keys()):
            percentage_of_correct_tag[i - 1] = int(last_percentage + 100 - ((count - correct_tags[i]) / count)*100)
            last_percentage = percentage_of_correct_tag[i - 1]

    for i in range(1, 13):
        if i not in list(correct_tags.keys()):
            correct_tags[i] = 0

    correct_tags = sorted(correct_tags.items(), key=lambda x: x[0])

    tags = Tag.objects.all().values_list("name", flat=True)

    print(percentage_of_correct_tag)
    context = {
        "approved": approved,
        "not_reviewed": 100 - approved,
        "percentagem_tags": percentage_of_correct_tag,
        "all_answers": all_tags,
        "correct_answers": correct_tags,
        "tag": tags,
        # "correct_quizzes": int(correct_quizzes/quizzes_done * 100),
        # "correct_tests": int(correct_tests/tests_done * 100)
    }

    return render(request, 'profile.html', context)
