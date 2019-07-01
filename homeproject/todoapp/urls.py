from django.contrib import admin
from django.urls import path
from todoapp.views import *

urlpatterns = [

    path('login/',LoginView.as_view(),name='login_html'),
    path('signup/',SignupView.as_view(),name='signup_html'),
    path('logout/',LogoutView.as_view(),name='logout_html'),


    path('todolist/',ToDoList_View.as_view(),name='todolist_html'),
    path('todolist/<int:key>/',ToDoList_View.as_view(),name='todoitems_html'),

    path('todolist/add/',AddList_View.as_view(),name='add_list_html'),
    path('todolist/edit/<int:key>',AddList_View.as_view(),name='edit_list_html'),
    path('todolist/delete/<int:key>',AddList_View.as_view(),name='delete_list_html'),

    path('todolist/<int:key>/add/',AddItem_View.as_view(),name='add_item_html'),
    path('todolist/<int:key>/edit/<int:item>/',AddItem_View.as_view(),name='edit_item_html'),
    path('todolist/<int:key>/delete/<int:item>/',AddItem_View.as_view(),name='delete_item_html')
]
