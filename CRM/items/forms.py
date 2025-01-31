from django import forms
from .models import Item

class AdditemForm(forms.ModelForm):
   
    class Meta:
        model = Item
        fields = {'Category','name','price','description','image'}
        widgets = {
        'Category': forms.Select(attrs={
            'class':'custom_input'
        }),
        'name':forms.TextInput(attrs={
            'class':'custom_input'
        }),
        'price':forms.TextInput(attrs={
            'class':'custom_input'
        }),
        'description':forms.Textarea(attrs={
            'class':'custom_input'
        }),
        'image':forms.FileInput(attrs={
            'class':'custom_input'
        })
    }
    
class EdititemForm(forms.ModelForm):
   
    class Meta:
        model = Item
        fields = {'name','price','description','image','is_sold'}
        widgets = {
        'name':forms.TextInput(attrs={
            'class':'custom_input'
        }),
        'price':forms.TextInput(attrs={
            'class':'custom_input'
        }),
        'description':forms.Textarea(attrs={
            'class':'custom_input'
        }),
        'image':forms.FileInput(attrs={
            'class':'custom_input'
        })
    }
