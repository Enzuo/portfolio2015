from django.db import models
from hvad.models import TranslatableModel, TranslatedFields
# django-hvad Doc : for translations
# http://django-hvad.readthedocs.org/en/latest/public/quickstart.html


"""
Tech : ex python
"""
class Tech(models.Model):
	name = models.CharField(max_length=20)
	icon = models.ImageField()
	notes = models.CharField(max_length=200)
	
	def __unicode__(self):
		return self.name
	
class Tag(models.Model):
	name = models.CharField(max_length=200)
	
	def __unicode__(self):
		return self.name
	
	
class Work(TranslatableModel):
	translations = TranslatedFields(
		title = models.CharField(max_length=200),
		content = models.TextField(),
	)
	date = models.DateField()
	
	techs = models.ManyToManyField(Tech)
	tags = models.ManyToManyField(Tag)
	
	def __unicode__(self):
		return self.title
