from django.http import HttpResponse
from plans.facebook_proxy import login_auth
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json

@csrf_exempt
@require_http_methods(["POST"])
def auth(request, access_token):
	avatar = request.POST.get('avatar', "")
	result = login_auth(access_token, avatar)
	return HttpResponse(json.dumps(result))