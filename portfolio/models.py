from django.db import models

class Client(models.Model):
	name = models.CharField(max_length = 256)
	mobile_number = models.CharField(max_length = 200 , blank = True)
	email = models.EmailField(max_length = 200)
	postal_address = models.CharField(max_length = 200 , blank = True)
	location = models.CharField(max_length = 200 , blank = True)

	
	def __unicode__(self):
		return self.name
		

class Portfolio(models.Model):
	title = models.CharField(max_length = 200)
	description = models.TextField(max_length = 20000, blank = True)
	date_of_submission = models.DateTimeField()
	client = models.ForeignKey('Client',on_delete = models.CASCADE)
	
	def __unicode__(self):
		return self.title

class Gallery(models.Model):
	portfolio = models.ForeignKey('Portfolio',on_delete = models.CASCADE)
	image = models.ImageField(upload_to='portfolio')
	
	def __unicode__(self):
		return portfolio.title
	
