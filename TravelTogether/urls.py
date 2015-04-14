from django.conf.urls import include, url
from django.contrib import admin
from tastypie.api import Api
from plans.api import PlanResource, UserResource

# plan_resource = PlanResource()

v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(PlanResource())

urlpatterns = [
    # Examples:
	url(r'^$', 'plans.views.main.main', name='main'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),
    # url(r'^plans/', include('plans.urls'), namespace = 'plans'),
]
