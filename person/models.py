from django.db import models

GENDER = (('male', 'male'), ('female', 'female'))

class Person (models.Model):
	facebookid = models.CharField(max_lenght = 30, primary_key = True)
	username = models.CharField(max_lenght = 30, blank = False, default = '')
	name = models.CharField(max_lenght = 100, blank = False, default = '')
	gender = models.CharField(choices = GENDER, blank = False, default = 'male')


	class Meta:
		ordering = ('facebookid',)