from django.contrib import admin
from django import forms
from django.db import models

from portfolio.models import Work, Tech, Tag



admin.site.register(Tech)
admin.site.register(Tag)

class WorkModelAdmin(admin.ModelAdmin):
    formfield_overrides = { models.TextField: {'widget': forms.Textarea(attrs={'class':'ckeditor'})}, }

    class Media:
        js = ('/static/ckeditor/ckeditor/ckeditor.js',)
    
admin.site.register(Work, WorkModelAdmin)
