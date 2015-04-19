# from django.contrib.auth.models import User
# from tastypie.resources import ModelResource
# from plans.models import Plan
# from tastypie import fields

# class UserResource(ModelResource):
#     class Meta:
#         queryset = User.objects.all()
#         resource_name = 'user'

# class PlanResource(ModelResource):
# 	user = fields.ForeignKey(UserResource, 'holder')
# 	# pass
# 	class Meta:
# 		queryset = Plan.objects.all()
# 		resource_name = 'plan'