from django.db import models

class CompanyInfo(models.Model):
	name_of_company = models.CharField(max_length = 200 , default = "Emasco TZ")
	email = models.EmailField(max_length = 200)
	postal_address = models.CharField(max_length = 200 , blank = True)
	physical_location = models.CharField(max_length = 200 , blank = True)
	mobile_number = models.CharField(max_length = 200 , blank = True)
	fax_number = models.CharField(max_length = 200 , blank = True)	
	website = models.CharField(max_length = 200 , default = "http://emascotz.herokuapp.com/")
	
	def __unicode__(self):
		return self.name_of_company


class CompanyMessage(models.Model):
	fullname = models.CharField(max_length = 256)
	email = models.EmailField(max_length = 200, blank = True)
	mobile_number = models.CharField(max_length = 256, blank = True)
	subject = models.CharField(max_length = 256)
	message = models.TextField(max_length = 20000)
	
	def __unicode__(self):
		return self.subject
