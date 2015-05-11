from django import forms

class ContactForm(forms.Form):
	email = forms.EmailField(required=True)
	name = forms.CharField(initial='Your name', max_length=100, required=True)
	subject = forms.CharField(max_length=100, required=True)
	message = forms.CharField(widget=forms.Textarea)
