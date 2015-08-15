from django.db import models

optional = {'null':True, 'blank':True}

class UserProfile(models.Model):
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=100)
	email = models.EmailField(max_length=200)
	avatar_url = models.ImageField(default='N/A', **optional)
	date_created = models.DateTimeField('Date Created')

