from django.db import models
from django.template.defaultfilters import slugify
from django.db.models.signals import pre_save

# Create your models here.
class Restaurant(models.Model):
	name = models.CharField(max_length=225, unique=True)
	slug = models.SlugField(blank=True)
	description = models.TextField()
	opening_time = models.TimeField()
	closing_time = models.TimeField()
	logo = models.ImageField(null=True, blank=True, upload_to="logos")

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['name']

class Item(models.Model):
	restaurant = models.ForeignKey(Restaurant)
	name = models.CharField(max_length=225, unique=True)
	slug = models.SlugField(blank=True)
	description = models.TextField()
	price = models.DecimalField(max_digits=6, decimal_places=3)
	active = models.BooleanField(default=True)
		
	def __str__(self):
		return self.name

	class Meta:
		ordering = ['name']


def pre_save_function(sender, instance, *args, **kwargs):
	instance.slug = slugify(instance.name)

pre_save.connect(pre_save_function, sender=Restaurant)
pre_save.connect(pre_save_function, sender=Item)