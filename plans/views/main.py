from django.http import HttpResponse

def auth(request):
	return HttpResponse("hello auth")