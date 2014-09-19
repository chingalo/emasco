from django.db import models

class AboutUs(models.Model):
	
	about= "About us"
	description = models.TextField(max_length = 20000)
	
	def __unicode__(self):
		return self.about
