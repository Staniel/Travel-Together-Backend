from django.http import HttpResponse
from plans.facebook_proxy import login_auth
import json

def auth(request, access_token):
	result = login_auth(access_token)
	return HttpResponse(json.dumps(login_auth(access_token)))