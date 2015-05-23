from django.http import HttpResponse
from plans.facebook_proxy import login_auth
from plans.plan_manager import *
from plans.format_result import format
from plans.models import FBUser, Plan
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from datetime import datetime

@csrf_exempt
@require_http_methods(["POST"])
def add_plan(request, access_token):
	result = login_auth(access_token)
	if result['err']['code'] != 0:
		return HttpResponse(json.dumps(result))	
	userid = result['data']['id']
	try:
		new_plan = Plan()
		user = FBUser.objects.get(fbid=userid)
		new_plan.holder = user
		new_plan.title = request.POST.get('title', "testtitle")
		new_plan.destination = request.POST.get('destination', "testdestination")
		new_plan.description = request.POST.get('description', "testdescription")
		new_plan.depart_time = request.POST.get('depart_time', datetime.today())
		new_plan.length = request.POST.get('length', 2)
		new_plan.limit = request.POST.get('limit', 2)
		visible_type = request.POST.get('visible_type', 1)
		new_plan.visible_type = int(visible_type)
		friend_list = request.POST.getlist('friendlist',[])
		new_plan.full_clean()
		new_plan.save()
		if new_plan.visible_type == 3:
			for friendid in friend_list:
				friend = FBUser.objects.get(fbid=friendid)
				private = PrivatePlan()
				private.accessible_user = friend
				private.accessible_plan = new_plan
				private.full_clean()
				private.save()
		result = format(0, 'create success')
		return HttpResponse(json.dumps(result))	
	except Exception as e:
   		result = format(400, str(e))
        return HttpResponse(json.dumps(result))	

#django do not support put, use post instead
@csrf_exempt
@require_http_methods(["POST"])
def edit_plan(request, access_token, planid):
	result = login_auth(access_token)
	if result['err']['code'] != 0:
		return HttpResponse(json.dumps(result))	
	userid = result['data']['id']
	try:
		plan = Plan.objects.get(id__exact=planid)
		user = FBUser.objects.get(fbid=userid)
		PrivatePlan.objects.filter(accessible_plan=plan).delete()
		plan.holder = user
		plan.title = request.POST.get('title', plan.title)
		plan.destination = request.POST.get('destination', plan.destination)
		plan.description = request.POST.get('description', plan.description)
		plan.depart_time = request.POST.get('depart_time', plan.depart_time)
		plan.length = request.POST.get('length', plan.length)
		plan.limit = request.POST.get('limit', plan.limit)
		visible_type = request.POST.get('visible_type', plan.visible_type)
		plan.visible_type = int(visible_type)
		friend_list = request.POST.getlist('friendlist', [])
		plan.full_clean()
		plan.save()
		if plan.visible_type == 3:
			for friendid in friend_list:
				friend = FBUser.objects.get(fbid=friendid)
				private = PrivatePlan()
				private.accessible_user = friend
				private.accessible_plan = plan
				private.full_clean()
				private.save()
		result = format(0, 'edit success')
		return HttpResponse(json.dumps(result))	
	except Exception as e:
   		result = format(400, str(e))
        return HttpResponse(json.dumps(result))	

@csrf_exempt
@require_http_methods(["DELETE"])
def delete_plan(request, access_token, planid):
	result = login_auth(access_token)
	if result['err']['code'] != 0:
		return HttpResponse(json.dumps(result))	
	userid = result['data']['id']
	try:
		plan = Plan.objects.get(id__exact=planid)
		if get_editable(userid, plan):
			plan.delete()
			result = format(0, 'delete success')
		else:
			result = format(403, 'delete permission denied')
		return HttpResponse(json.dumps(result))	
	except Exception as e:
		result = format(400, str(e))
		return HttpResponse(json.dumps(result))	


@csrf_exempt
@require_http_methods(["POST"])
def join_plan(request, access_token, planid):
	result = login_auth(access_token)
	if result['err']['code'] != 0:
		return HttpResponse(json.dumps(result))	
	userid = result['data']['id']
	try:
		plan = Plan.objects.get(id__exact=planid)
		if get_joinable(userid, plan):
			newjoin = JoinedPlan()
			user = FBUser.objects.get(fbid=userid)
			newjoin.joined_user = user
			newjoin.joined_plan = plan
			newjoin.full_clean()
			newjoin.save()
			result = format(0, 'join success')
		else:
			result = format(403, 'join permission denied')
		return HttpResponse(json.dumps(result))	
	except Exception as e:
		result = format(400, str(e))
		return HttpResponse(json.dumps(result))	

@csrf_exempt
@require_http_methods(["POST"])
def unjoin_plan(request, access_token, planid):
	result = login_auth(access_token)
	if result['err']['code'] != 0:
		return HttpResponse(json.dumps(result))	
	userid = result['data']['id']
	try:
		plan = Plan.objects.get(id__exact=planid)
		print plan
		print userid
		r = JoinedPlan.objects.filter(joined_user__exact=userid, joined_plan=plan)
		if len(r) == 0:
			result = format(403, 'unjoin permission denied')
		elif len(r) > 1:
			result = format(400, 'internal realtionship error')
		else:
			rel = r[0]
			rel.delete()
			result = format(0, 'unjoin success')
		return HttpResponse(json.dumps(result))	
	except Exception as e:
		result = format(400, str(e))
		return HttpResponse(json.dumps(result))	
