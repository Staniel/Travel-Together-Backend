from django.conf.urls import include, url
from django.contrib import admin
# from tastypie.api import Api
# from plans.api import PlanResource, UserResource

# plan_resource = PlanResource()

# v1_api = Api(api_name='v1')
# v1_api.register(UserResource())
# v1_api.register(PlanResource())

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1', include('plans.urls', namespace="plans")),
]
