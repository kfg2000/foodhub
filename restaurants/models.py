from django.db import models

# Create your models here.
class Restaurant(models.Model):
	name = models.CharField(max_length=225)
	description = models.TextField()
	opening_time = models.TimeField()
	closing_time = models.TimeField()
