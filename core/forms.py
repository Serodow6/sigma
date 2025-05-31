from django import forms
from core.models import *

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),
            'subject':forms.TextInput(attrs={'class':'form-control','placeholder':'Subject'}),
            'message':forms.Textarea(attrs={'class':'form-control','rows':'5','placeholder':'Message'}),
        }
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text':forms.Textarea(attrs={'class':'form-control','rows':'5','placeholder':'Message'})
        }