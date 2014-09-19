from django.db import models

class Service(models.Model):
	
	name_of_service = models.CharField(max_length = 256)
	
	def __unicode__(self):
		return self.name_of_service
