from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'auth$', 'plans.views.main.auth', name='auth'),
)
