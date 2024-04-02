from django.shortcuts import render, redirect

from users.models import KahUCUser


def home_redirect(request):
    return redirect('/home/')


def home(request):
    context = {
        # os 3 users com mais quizzes acertados
        'users': KahUCUser.objects.all().exclude(number_of_correct_quizzes=0).order_by('-number_of_correct_quizzes').values_list('first_name', 'last_name')[:3],
    }

    return render(request, 'home.html', context)


def about_us(request):
    return render(request, 'about_us.html')


def my_custom_page_not_found_view(request, exception):
    return render(request, '404.html', status=404)


def my_custom_error_view(request):
    return render(request, '500.html', status=500)


def my_custom_permission_denied_view(request, exception):
    return render(request, '403.html', status=403)


def my_custom_bad_request_view(request, exception):
    return render(request, '400.html', status=400)
