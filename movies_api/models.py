from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Movie(models.Model):
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=500)
	created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='movies', default=None)

	def __str__(self):
		return self.title + '  ' + self.created_by.username