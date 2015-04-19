from django.http import HttpResponse

def auth(request, access_token):
	return HttpResponse("hello auth "+access_token)