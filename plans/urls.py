from django.conf.urls import patterns, url

urlpatterns = patterns('',
	
    url(r'auth/(?P<access_token>\w+)$', 'plans.views.main.auth', name='auth'),

    url(r'plan/(?P<access_token>\w+)/(?P<plan_id>\d+)$', 'plans.views.view_plan.plan_detail', name='detail'),
	url(r'plan/(?P<access_token>\w+)/(?P<visible_type>\w*)$', 'plans.views.view_plan.list_plans', name='list'),

	url(r'plan/join/(?P<access_token>\w+)/(?P<plan_id>\d+)$', 'plans.views.plan_action.join_plan.', name='join'),
	url(r'plan/unjoin/(?P<access_token>\w+)/(?P<plan_id>\d+)$', 'plans.views.plan_action.unjoin_plan.', name='unjoin'),
	url(r'plan/delete/(?P<access_token>\w+)/(?P<plan_id>\d+)$', 'plans.views.plan_action.delete_plan.', name='delete'),
	url(r'plan/edit/(?P<access_token>\w+)/(?P<plan_id>\d+)$', 'plans.views.plan_action.edit_plan.', name='edit'),
	url(r'plan/add/(?P<access_token>\w+)/$', 'plans.views.plan_action.add_plan.', name='add'),
)
