from django.urls import path
from . import views

urlpatterns = [
    path("sign-up/", views.sign_up_view, name="sign-up"),
    path("register/", views.sign_up_view_2, name="register"),
    path("sign-in/", views.sign_in_view, name="sign-in"),
]
