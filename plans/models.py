from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class FBUser(models.Model):
	fbid = models.CharField(max_length = 20)
	access_token = models.CharField(max_length = 100)
	name = models.CharField(max_length = 50)

class Plan(models.Model):
	holder = models.ForeignKey(User)
	title = models.CharField(max_length = 200)
	description = models.CharField(max_length = 500)
	destination = models.CharField(max_length = 200)
	limit = models.IntegerField()
	depart_time = models.DateTimeField()
	length = models.IntegerField()
	visible_type = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(3)])
	def __str__(self):
		return self.destination+'.'+self.description

class JoinedPlan(models.Model):
	joined_user = models.ForeignKey(User)
	joined_plan = models.ForeignKey(Plan)
	def __str__(self):
		return self.joined_user.__str__()+" join "+self.joined_plan.__str__()

class PrivatePlan(models.Model):
	accessible_user = models.ForeignKey(User)
	accessible_plan = models.ForeignKey(Plan)
	def __str__(self):
		return self.accessible_user.__str__()+" can see "+self.accessible_plan.__str__()
