from django.db import models

#model for mission for site
class Mission(models.Model):
	
	mission = "mission"
	description = models.TextField(max_length = 20000)
	
	def __unicode__(self):
		return self.mission



#model for vission
class Vision(models.Model):
	
	vision = "vision"
	description = models.TextField(max_length = 20000)
	
	def __unicode__(self):
		return self.vision
