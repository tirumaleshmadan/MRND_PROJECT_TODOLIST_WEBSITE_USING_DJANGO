from django.contrib import admin
from django.urls import path
from todoapp.views import LoginView,LogoutView,SignupView

urlpatterns = [
    path('login/',LoginView.as_view(),name='login_html'),
    path('signup/',SignupView.as_view(),name='signup_html'),
    path('logout/',LogoutView.as_view(),name='logout_html'),
]
