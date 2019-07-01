from django.views import View
from todoapp.forms import List_Form
from django.shortcuts import *
from django.urls import resolve
from django.utils.timezone import now
from todoapp.models import TodoList

class AddList_View(View):
    def get(self,request,*args,**kwargs):
        if kwargs:
            list=TodoList.objects.get(id=kwargs['key'])
            list_form=List_Form(instance=list)
        else:
            list_form=List_Form()
        return render(
            request,
            template_name='list_form.html',
            context={
                'list_form':list_form,
                'title':'ADD NEW LIST',
            }
        )

    def post(self,request,*args,**kwargs):

        if resolve(request.path_info).url_name=='delete_list_html':
            TodoList.objects.get(id=kwargs['key']).delete()
            return redirect('todolist_html')

        if resolve(request.path_info).url_name=='edit_list_html':
            todolist=TodoList.objects.get(id=kwargs['key'])
            list_form=List_Form(request.POST,instance=todolist)
            if list_form.is_valid():
                list_form=list_form.save()
                return redirect('todolist_html')
        else:
            list_form = List_Form(request.POST)
            if list_form.is_valid():
                list_form=list_form.save(commit=False)
                list_form.user=request.user
                list_form.created_date=now()
                list_form.save()
                return redirect('todolist_html')

        return render(
            request,
            template_name='list_form.html',
            context={
                'list_form': list_form,
                'title': 'ADD NEW LIST',
            }
        )