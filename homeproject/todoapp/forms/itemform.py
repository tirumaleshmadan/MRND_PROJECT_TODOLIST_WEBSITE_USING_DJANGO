from django import forms
from todoapp.models import TodoItem

class Item_Form(forms.ModelForm):
    class Meta:
        model=TodoItem
        exclude=['id','list_id']
        widgets={
            'description':forms.TextInput(attrs={'class':'input box is-rounded is-primary','placeholder':'type the description'}),
            'due_date':forms.DateInput(attrs={'class':'input'}),
            'completed':forms.CheckboxInput(attrs={'class':'is-checkradio'})
        }