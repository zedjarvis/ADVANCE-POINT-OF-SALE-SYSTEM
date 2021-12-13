# -*- encoding: utf-8 -*-
"""
Copyright (c) 2021 - Cedrouseroll
"""

# Create your views here.+

from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .forms import SignUpForm


# Register Account View
def register_user(request):
    # authenticated users are not allowed on this page
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        # user registration page
        form = SignUpForm()  # custom userform

        if request.method == 'POST':
            form = SignUpForm(request.POST or None)
            if form.is_valid():
                user = form.save(commit=False)
                user.save()
                user_name = form.cleaned_data.get("username")
                messages.success(request,
                                 user_name.upper() + ', account created!',
                                 extra_tags='alert-success')
                # send new user to login page
                return redirect('login')

            else:
                return render(request,
                              'authentication/register.html', {'form': form})

    context = {'form': form}

    return render(request,
                  'authentication/register.html', context)


def lock_screen(request):
    return render(request, 'authentication/lockscreen.html')


@csrf_exempt
def lock_screen_view(request):
    request.session['lock'] = 'locked'
    return redirect('lock')


# Reset password page
def reset_password(request):
    return render(request, 'authentication/reset_password.html')


# CUSTOM ERROR PAGES
def handler400(request, exception=None):
    response = render(request, "authentication/errors/400.html", {})
    return response


def handler403(request, exception=None):
    response = render(request, "authentication/errors/403.html", {})
    return response


def handler404(request, exception=None):
    response = render(request, "authentication/errors/404.html", {})
    return response


def handler500(request, exeption=None):
    response = render(request, "authentication/errors/500.html", {})
    return response
