from captcha.fields import CaptchaField
from django import forms
from .models import FamousWomen


class AddPostForm(forms.ModelForm):

    class Meta:
        model = FamousWomen
        fields = ['name', 'slug', 'photo', 'old', 'content', 'is_published', 'cat', 'tags']


class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=255)
    email = forms.EmailField(label='Email')
    content = forms.CharField(widget=forms.Textarea())
    captcha = CaptchaField()
