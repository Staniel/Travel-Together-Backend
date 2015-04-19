from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'auth/(?P<access_token>\w+)$', 'plans.views.main.auth', name='auth'),
)
