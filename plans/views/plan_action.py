from django.http import HttpResponse
from plans.facebook_proxy import login_auth
from plans.plan_manager import *

def add_plan(request, access_token):
	result = login_auth(access_token)
	if result['err']['code'] != 0:
		return HttpResponse(json.dumps(result))	
	userid = result['data']['id']

def edit_plan(request, access_token, planid):
	result = login_auth(access_token)
	if result['err']['code'] != 0:
		return HttpResponse(json.dumps(result))	
	userid = result['data']['id']

def delete_plan(request, access_token, planid):
	result = login_auth(access_token)
	if result['err']['code'] != 0:
		return HttpResponse(json.dumps(result))	
	userid = result['data']['id']

def join_plan(request, access_token, planid):
	result = login_auth(access_token)
	if result['err']['code'] != 0:
		return HttpResponse(json.dumps(result))	
	userid = result['data']['id']

def unjoin_plan(request, access_token, planid):
	result = login_auth(access_token)
	if result['err']['code'] != 0:
		return HttpResponse(json.dumps(result))	
	userid = result['data']['id']