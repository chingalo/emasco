from django.db import models

class Client(models.Model):
	name = models.CharField(max_length = 256)
	mobile_number = models.CharField(max_length = 200 , blank = True)
	email = models.EmailField(max_length = 200)
	postal_address = models.CharField(max_length = 200 , blank = True)
	location = models.CharField(max_length = 200 , blank = True)

	
	def __unicode__(self):
		return self.name
		
