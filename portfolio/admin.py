from django.contrib import admin

from django_summernote.admin import SummernoteModelAdmin

from portfolio.models import Work, Tech, Tag



admin.site.register(Tech)
admin.site.register(Tag)

class WorkAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    pass
    
admin.site.register(Work, WorkAdmin)
