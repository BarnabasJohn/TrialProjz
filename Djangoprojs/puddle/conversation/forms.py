from django import forms
from .models import ConversationMessage


class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model = ConversationMessage
        fields = ('content',)
        widget = {
            'content': forms.Textarea(attrs={
                'class': 'w-3/4 py-4 px-6 rounded-xl border'
            })
        }
