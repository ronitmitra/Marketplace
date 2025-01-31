from django import forms

from .models import Messages

class MessageForm(forms.ModelForm):
    class Meta:
        model = Messages
        fields = {'content',}
        widgets = {
            'content':forms.Textarea(attrs={
                'class':'message_content'
            })
        }