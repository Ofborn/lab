from django.db import models

GENDER = (('male', 'male'), ('female', 'female'))

class Person (models.Model):
	facebookid = models.CharField(max_length = 30, primary_key = True)
	username = models.CharField(max_length = 30, blank = False, default = '')
	name = models.CharField(max_length = 100, blank = False, default = '')
	gender = models.CharField(choices = GENDER, default = 'male', max_length = 6)


	class Meta:
		ordering = ('facebookid',)