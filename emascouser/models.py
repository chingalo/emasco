from django.db import models

class User(models.Model):
	
	full_name = models.CharField(max_length = 200)
	position = models.CharField(max_length = 200 )
	email = models.EmailField(max_length = 200)
	mobile_number = models.CharField(max_length = 200)
	gender_selection = (('male','male'),('female','female'))
	gender = models.CharField(max_length=20, choices = gender_selection , default = 'male')
	user_history = models.TextField(max_length = 20000, blank = True)
	username = models.CharField(max_length = 200)
	password = models.CharField(max_length = 200)
	
	login_status = models.CharField(max_length = 200, default = "logout")
	
	def __unicode__(self):
		return self.full_name
