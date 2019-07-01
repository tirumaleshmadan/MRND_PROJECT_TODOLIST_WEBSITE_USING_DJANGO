from django import forms
from todoapp.models import TodoList

class List_Form(forms.ModelForm):
    class Meta:
        model=TodoList
        exclude=['id','user','created_date']
        widgets={
            'name':forms.TextInput(attrs={'class':'input box is-rounded is-primary','placeholder':'enter the name'}),
        }