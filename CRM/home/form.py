from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

class Login(AuthenticationForm):
      username = forms.CharField(widget = forms.TextInput(attrs={
            'class':'custom_input',
            'placeholder':'Enter Username'
        })
        )
      password= forms.CharField(widget=forms.PasswordInput(attrs={
            'class':'custom_input',
            'placeholder':"Enter Password"
        }))
      
    

class SignupForm(UserCreationForm):
    username = forms.CharField(widget = forms.TextInput(attrs={
            'class':'custom_input',
            'placeholder':'Enter Username'
        })
        )
    email = forms.CharField(widget=forms.TextInput(attrs={
            'class':'custom_input',
            'placeholder':"Enter Email"
        }))

    password1= forms.CharField(widget=forms.PasswordInput(attrs={
            'class':'custom_input',
            'placeholder':"Enter Password"
        }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
            'class':'custom_input',
            'placeholder':'Enter Password Again'
        }))
    class Meta:
        model = User
        fields = ('username','email','password1','password2')

        