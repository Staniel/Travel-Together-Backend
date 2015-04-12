from django.contrib import admin
from plans.models import Plan, JoinedPlan
# Register your models here.
admin.site.register(Plan)
admin.site.register(JoinedPlan)
