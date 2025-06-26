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
class CreateStoryForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(),widget=forms.Select(attrs={'class':'form-control','placeholder':'Category'}))
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(),widget=forms.SelectMultiple(attrs={'class':'form-control','placeholder':'Tags'}))
    class Meta:
        model = Story
        fields = '__all__'
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Title'}),
            'description':forms.Textarea(attrs={'class':'form-control','rows':'5','placeholder':'Description'}),
            'text':forms.Textarea(attrs={'class':'form-control','rows':'5','placeholder':'Text'}),
            'image':forms.FileInput(attrs={'class':'form-control','placeholder':'Image'}),
        }

class CreateRecipeForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(),widget=forms.Select(attrs={'class':'form-control','placeholder':'Category'}))
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(),widget=forms.SelectMultiple(attrs={'class':'form-control','placeholder':'Tags'}))
    class Meta:
        model = Recipe
        fields = '__all__'
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Title'}),
            'description':forms.Textarea(attrs={'class':'form-control','rows':'5','placeholder':'Description'}),
            'text':forms.Textarea(attrs={'class':'form-control','rows':'5','placeholder':'Text'}),
            'image':forms.FileInput(attrs={'class':'form-control','placeholder':'Image'}),
        }