from django.views import View
from todoapp.forms import Item_Form
from django.shortcuts import redirect,render
from django.urls import resolve
from todoapp.models import *

class AddItem_View(View):
    def get(self,request,*args,**kwargs):
        if len(kwargs)==2:
            item=TodoItem.objects.get(id=kwargs['item'])
            item_form=Item_Form(instance=item)
        else:
            item_form=Item_Form()
        return render(
            request,
            template_name='item_form.html',
            context={
                'item_form':item_form,
                'title':'ADD NEW ITEM',
            }
        )

    def post(self,request,*args,**kwargs):

        if resolve(request.path_info).url_name=='delete_item_html':
            TodoItem.objects.get(id=kwargs['item']).delete()
            return redirect('todoitems_html',kwargs['key'])

        if resolve(request.path_info).url_name=='edit_item_html':
            item=TodoItem.objects.get(id=kwargs['item'])
            item_form=Item_Form(request.POST,instance=item)
            if item_form.is_valid():
                item_form.save(commit=False)
                list=TodoList.objects.get(id=kwargs['key'])
                item_form.list=list
                item_form.save()
                return redirect('todoitems_html',kwargs['key'])

        else:
            item_form=Item_Form(request.POST)
            if item_form.is_valid():
                item_form.save(commit=False)
                list=TodoList.objects.get(id=kwargs['key'])
                item_form.list=list
                item_form.save()
                return redirect('todoitems_html',kwargs['key'])



        return render(
            request,
            template_name='item_form.html',
            context={
                'item_form':item_form,
                'title':'ADD NEW ITEM',
            }
        )