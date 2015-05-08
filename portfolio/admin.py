from django.contrib import admin
from django import forms

from redactor.widgets import RedactorEditor

from portfolio.models import Work, Tech, Tag, Article

class TechAdmin(admin.ModelAdmin):
	list_display = ('name', 'icon_32')
	
admin.site.register(Tech, TechAdmin)
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
	list_display = ('title', 'used_techs','translated_in')
	form = WorkAdminForm
	
class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title', 'translated_in')
	
admin.site.register(Work, WorkAdmin)
admin.site.register(Article, ArticleAdmin)
