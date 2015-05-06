from django.db import models
from django.utils.html import format_html
from django.conf import settings

"""
Tech : ex python
"""
class Tech(models.Model):
	name = models.CharField(max_length=20)
	icon = models.ImageField(upload_to = 'images/icons/')
	notes = models.CharField(max_length=200, blank=True)
	
	def __unicode__(self):
		return self.name
		
	def icon_32(self):
		return format_html('<img style="height:32px; width:32px" src="media/{}"/>',
						   self.icon,
						)
	
class Tag(models.Model):
	name = models.CharField(max_length=200)
	
	def __unicode__(self):
		return self.name
	
	
class Work(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField()
	date = models.DateField()
	
	image = models.ImageField(upload_to = 'images/thumb/', blank=True)
	
	techs = models.ManyToManyField(Tech, blank=True)
	tags = models.ManyToManyField(Tag, blank=True)
	
	def __unicode__(self):
		return self.title
		
	def used_techs(self):
		return format_html("".join([p.icon_32() for p in self.techs.all()]))
		
	def translated_in(self):
		flags = ""
		if len(self.content_zh) > 1:
			flags += '<img style="height:20px; width:32px; margin:4px" src="'+settings.STATIC_URL +'portfolio/img/flags/zh.png"/>'
		if len(self.content_fr) > 1:
			flags += '<img style="height:20px; width:32px; margin:4px" src="'+settings.STATIC_URL +'portfolio/img/flags/fr.png"/>'
		if len(self.content_en) > 1:
			flags += '<img style="height:20px; width:32px; margin:4px" src="'+settings.STATIC_URL +'portfolio/img/flags/en.png"/>'
		
		return format_html(flags)
