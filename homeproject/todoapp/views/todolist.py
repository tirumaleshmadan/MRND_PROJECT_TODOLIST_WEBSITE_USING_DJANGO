from django.views import View
from django.shortcuts import *
from todoapp.models import TodoList,TodoItem
from django.contrib.auth.mixins import LoginRequiredMixin

class ToDoList_View(LoginRequiredMixin,View):
    login_url = '/login/'
    def get(self,request,*args,**kwargs):
        lists=TodoList.objects.filter(user_id=request.user.id)
        if kwargs:
            items=TodoItem.objects.filter(list_id=kwargs['key'])
            return render(
                request,
                template_name='todoitem.html',
                context={
                    'title':'Lets do this',
                    'items':items,
                }
            )
        return render(
            request,
            template_name='todolist.html',
            context={
                'title':'Lets do this',
                'lists':lists,
            }
        )
