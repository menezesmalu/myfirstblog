from django.db import models 
from django.utils import timezone

class Post(models.Model):
	author = models.ForeignKey('auth.User') #outro modelo
	title = models.CharField(max_length = 200) #numero limitado de caracteres
	text = models.TextField() #numero ilimitado de caracteres
	created_date = models.DateTimeField(default = timezone.now) # data e hora
	published_date = models.DateTimeField(blank = True, null = True)
	def publish(self):
		self.published_date = timezone.now()
		self.save()
	def __str__(self):
		return self.title 	
