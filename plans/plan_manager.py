from plans.models import Plan, JoinedPlan, PrivatePlan
from plans.facebook_proxy import is_friend

def get_available_plans(userid):
	plans = Plan.objects.all()
	plan_list = []
	for plan in plans:
		if get_viewable(userid, plan):
			single_plan = plan.as_dict()
			count = JoinedPlan.objects.filter(joined_plan__exact=plan.id).count()
			single_plan['count'] = count
			plan_list.append(single_plan)
	return plan_list

def get_my_plans(userid):
	plans = Plan.objects.filter(holder__exact=userid)
	plan_list = [plan.as_dict() for plan in plans]
	plan_list = []
	for plan in plans:
		single_plan = plan.as_dict()
		count = JoinedPlan.objects.filter(joined_plan__exact=plan.id).count()
		single_plan['count'] = count
		plan_list.append(single_plan)	
	return plan_list

def get_joined_plans(userid):
	plans = []
	joinedplans = JoinedPlan.objects.filter(joined_user__exact=userid)
	for joinedplan in joinedplans:
		single_plan = joinedplan.joined_plan.as_dict()
		count = JoinedPlan.objects.filter(joined_plan__exact=joinedplan.joined_plan.id).count()
		single_plan['count'] = count
		plans.append(single_plan)
	return plans
	
def get_joiners(plan):
	joiners = []
	joinedplans = JoinedPlan.objects.filter(joined_plan__exact=plan.id)
	for joinedplan in joinedplans:
		joiners.append(joinedplan.joined_user.as_dict())
	return joiners

def get_viewable(userid, plan):
	if plan is None:
		return False
	if plan.visible_type == 1 or userid == plan.holder.fbid:
		return True
	if plan.visible_type == 3:
		if PrivatePlan.objects.filter(accessible_user=userid, accessible_plan=plan.id).exists():
			return True
		else:
			return False
	if is_friend(userid, plan.holder.fbid):
		return True
	else:
		return False

def get_joinable(userid, plan):
	if plan is None:
		return False
	if userid == plan.holder.fbid:
		return False
	joiners = get_joiners(plan)
	joiner_id_list = [ joiner['id'] for joiner in joiners]
	if not get_viewable(userid, plan):
		return False
	if len(joiners) < plan.limit-1 and userid not in joiner_id_list:
		return True
	return False

def get_editable(userid, plan):
	if plan is None:
		return False
	if userid == plan.holder.fbid:
		return True
	else:
		return False


