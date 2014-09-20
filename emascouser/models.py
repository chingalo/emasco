from django.db import models


#model for user for website
class User(models.Model):
	
	full_name = models.CharField(max_length = 200)
	position = models.CharField(max_length = 200 )
	email = models.EmailField(max_length = 200)
	mobile_number = models.CharField(max_length = 200)
	gender_selection = (('male','male'),('female','female'))
	gender = models.CharField(max_length=20, choices = gender_selection , default = 'male')
	pic = models.CharField(max_length=20, default = 'no')
	user_history = models.TextField(max_length = 20000, blank = True)
	username = models.CharField(max_length = 200)
	password = models.CharField(max_length = 200)
	
	login_status = models.CharField(max_length = 200, default = "logout")
	
	def __unicode__(self):
		return self.full_name


#model for user specialization
class Specialization(models.Model):
	
	emasco_member = models.ForeignKey('User',on_delete = models.CASCADE)
	specialization = models.CharField(max_length = 200 )
	
	def __unicode__(self):
		return self.specialization



#model for position of professional team for the site
class Position(models.Model):
	
	user_position = models.CharField(max_length = 256)
	
	def __unicode__(self):
		return self.user_position
		
		

#model for category for team of professional
class TeamCategory(models.Model):
	
	team_member = models.ForeignKey('User',on_delete = models.CASCADE)
	team_category = models.CharField(max_length = 256)
	
	def __unicode__(self):
		return self.team_category	
		
