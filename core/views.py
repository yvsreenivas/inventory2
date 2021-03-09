from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
# from core.forms import UserForm, UserProfileInfoForm
from django.urls import reverse


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(
                username, password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'core/login.html', {})


def home(request):
    title = 'Home'
    context = {
        "header": title,
    }
    if request.user.is_authenticated:
        return render(request, "core/home.html", context)
    else:
        # render(request, "stocks/home.html",context)
        return render(request, "core/login.html", context)
