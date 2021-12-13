# -*- encoding: utf-8 -*-
"""
Copyright (c) 2021 - Cedrouseroll
"""

from django.urls import path
from .views import register_user, lock_screen, reset_password, lock_screen_view
from django.contrib.auth.views import LogoutView, LoginView as view

urlpatterns = [
    path('login/', view.as_view(
        template_name='authentication/login.html',
        redirect_authenticated_user=True), name="login"),
    path('register/', register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("lockscreen/", lock_screen, name="lock"),
    path("reset_password/", reset_password, name="reset_password"),
    path("lock_screen/", lock_screen_view, name='lock_screen')
]
