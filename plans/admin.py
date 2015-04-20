from django.contrib import admin
from plans.models import Plan, JoinedPlan, FBUser, PrivatePlan
# Register your models here.
admin.site.register(Plan)
admin.site.register(JoinedPlan)
admin.site.register(PrivatePlan)
admin.site.register(FBUser)
# admin.site.register(admin)
