from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import json
# Create your models here.

class FBUser(models.Model):
	fbid = models.CharField(max_length = 20, primary_key=True)
	name = models.CharField(max_length = 50)
	access_token = models.CharField(max_length = 500)
	avatar = models.CharField(max_length = 200)
	def __str__(self):
		return self.name
	def as_dict(self):
		return {
		'id': self.fbid,
		'name': self.name,
		'avatar': self.avatar
		}

class Plan(models.Model):
	holder = models.ForeignKey(FBUser)
	title = models.CharField(max_length = 200)
	description = models.CharField(max_length = 500)
	destination = models.CharField(max_length = 200)
	limit = models.IntegerField()
	depart_time = models.DateTimeField()
	length = models.IntegerField()
	visible_type = models.IntegerField()
	def __str__(self):
		return self.destination+'.'+self.description
	def clean(self):
		if self.limit < 2 or self.limit > 20:
			raise ValidationError('group size too large or too small')
		if self.visible_type != 1 and self.visible_type != 2 and self.visible_type != 3:
			raise ValidationError('visible_type parameter error')
	def as_dict(self):
		return {
		'plan_id': self.id,
		'holder': self.holder.as_dict(),
		'title': self.title,
		'destination': self.destination,
		'description': self.description,
		'limit': self.limit,
		'depart_time': str(self.depart_time),
		'length': self.length,
		'visible_type': self.visible_type
		}

class JoinedPlan(models.Model):
	joined_user = models.ForeignKey(FBUser)
	joined_plan = models.ForeignKey(Plan)
	class Meta:
		unique_together = ('joined_user', 'joined_plan')
	def __str__(self):
		return self.joined_user.__str__()+" join "+self.joined_plan.__str__()

class PrivatePlan(models.Model):
	accessible_user = models.ForeignKey(FBUser)
	accessible_plan = models.ForeignKey(Plan)
	class Meta:
		unique_together = ('accessible_user', 'accessible_plan')
	def __str__(self):
		return self.accessible_user.__str__()+" can see "+self.accessible_plan.__str__()
