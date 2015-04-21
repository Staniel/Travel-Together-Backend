from django.http import HttpResponse
from plans.facebook_proxy import login_auth
import json
from plans.format_result import format
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from plans.plan_manager import *

@csrf_exempt
@require_http_methods(["GET"])
def list_plans(request, access_token, visible_type=""):
	result = login_auth(access_token)
	if result['err']['code'] != 0:
		return HttpResponse(json.dumps(result))	
	userid = result['data']['id']
	try:
		if visible_type == 'all' or visible_type == "":
			planlist = get_available_plans(userid)
		elif visible_type == 'mine':
			planlist = get_my_plans(userid)
		elif visible_type == 'joined':
			planlist = get_joined_plans(userid)
		else:
			result = format(400, 'invalid parameter')
			return HttpResponse(json.dumps(result))	
		result = format(0, 'success', planlist)
		return HttpResponse(json.dumps(result))	
	except Exception as e:
		result = format(400, str(e))
		return HttpResponse(json.dumps(result))	


@csrf_exempt
@require_http_methods(["GET"])
def plan_detail(request, access_token, planid):
	result = login_auth(access_token)
	if result['err']['code'] != 0:
		return HttpResponse(json.dumps(result))
	try:
		plan = Plan.objects.get(id__exact=planid)
		userid = result['data']['id']
		if plan is None:
			result = format(404, 'no plan found')
		elif not get_viewable(userid, plan):
			result = format(403, 'not viewable')	
		else:
			joinable = get_joinable(userid, plan)
			editable = get_editable(userid, plan)
			joined_list = get_joiners(plan)
			joined = False
			joined_id_list = [joiner['id'] for joiner in joined_list]
			if userid in joined_id_list:
				joined = True
			data = {
				'plan_id': planid,
				'joinable': joinable,
				'editable': editable,
				'joined': joined,
				'joined_list': joined_list
			}
			result = format(0, 'success', data)
		return HttpResponse(json.dumps(result))
	except Exception as e:
		result = format(400, str(e))
		return HttpResponse(json.dumps(result))	

