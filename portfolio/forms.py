from django import forms
from django.utils.translation import ugettext_lazy

class ContactForm(forms.Form):
	email = forms.EmailField(label= ugettext_lazy('Email'), required=True)
	name = forms.CharField(label= ugettext_lazy('Name'), max_length=100, required=True)
	subject = forms.CharField(label= ugettext_lazy('Subject'), max_length=100, required=True)
	message = forms.CharField(label= ugettext_lazy('Message'), widget=forms.Textarea)
