from django.db import models

# Create your models here.

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
	
	
class Work(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField()
	date = models.DateField()
	
	techs = ManyToManyField(Tech)
	tags = ManyToManyField(Tag)
	
	def __unicode__(self):
        return self.title
