from django.db import models
from django.utils.html import format_html
from django.conf import settings
from PIL import Image

import os
from cStringIO import StringIO
from django.core.files.uploadedfile import SimpleUploadedFile

"""
Tech : ex python
"""
class Tech(models.Model):
	name = models.CharField(max_length=20)
	icon = models.ImageField(upload_to = 'images/icons/', db_column="icon")
	icon_g = models.ImageField(upload_to = 'images/icons/', blank=True)
	notes = models.CharField(max_length=200, blank=True)
	
	def __unicode__(self):
		return self.name
		
	def icon_32(self):
		return format_html('<img style="height:32px; width:32px" src="'+settings.MEDIA_URL+'{}"/>', self.icon,)
						
	def __init__(self, *args, **kwargs):
		super(Tech, self).__init__(*args, **kwargs)
		self.__original_icon = self.icon
		
	def save(self, *args, **kwargs):

		if self.__original_icon != self.icon:
			#create the greyscale icon
			
			#open the normal image
			image = Image.open(self.icon)
			
			#convert to greyscale
			image = image.convert('LA')
			
			# save the thumbnail to memory
			temp_handle = StringIO()
			image.save(temp_handle, 'png')
			temp_handle.seek(0) # rewind the file
			
			# save to the thumbnail field
			base = os.path.split( self.icon.name )[-1]
			suf = SimpleUploadedFile(os.path.splitext(base)[0], #without extension
									 temp_handle.read(),
									 content_type='image/png')
			self.icon_g.save(suf.name+'g.png', suf, save=False)
					
		super(Tech, self).save(*args, **kwargs)
		
	
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
		
class Article(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField()
	
	def translated_in(self):
		flags = ""
		if len(self.content_zh) > 1:
			flags += '<img style="height:20px; width:32px; margin:4px" src="'+settings.STATIC_URL +'portfolio/img/flags/zh.png"/>'
		if len(self.content_fr) > 1:
			flags += '<img style="height:20px; width:32px; margin:4px" src="'+settings.STATIC_URL +'portfolio/img/flags/fr.png"/>'
		if len(self.content_en) > 1:
			flags += '<img style="height:20px; width:32px; margin:4px" src="'+settings.STATIC_URL +'portfolio/img/flags/en.png"/>'
		
		return format_html(flags)
