from django.contrib import admin
from django import forms

from redactor.widgets import RedactorEditor

from portfolio.models import Work, Tech, Tag


admin.site.register(Tech)
admin.site.register(Tag)

#https://github.com/TigorC/django-redactorjs

			
class WorkAdminForm(forms.ModelForm):
	class Meta:
		model = Work
		widgets = {
		   'content_en': RedactorEditor(),
		}
		fields = '__all__'

class WorkAdmin(admin.ModelAdmin):
	form = WorkAdminForm
	
admin.site.register(Work, WorkAdmin)
