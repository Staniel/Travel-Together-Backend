import facebook
from format_result import format
from plans.models import FBUser
import json
def login_auth(access_token):
	result = {}
	try:
		graph = facebook.GraphAPI(access_token)
		profile = graph.get_object("me")
		fbid = profile['id']
		users = FBUser.objects.filter(fbid=fbid)
		if len(users) == 1:
			user = users[0]
			user.access_token = access_token
			user.save()
			return format(0, 'success', user.as_dict())
		elif len(user) == 0:
			newUser = FBUser()
			newUser.fbid = fbid
			newUser.name = profile['name']
			newUser.access_token = access_token
			newUser.save()
			return format(0, 'create a new user', newUser.as_dict())
	except Exception as e:
		print e
		return format(401, str(e))

def get_friend_list(userid):
	try:
		user = FBUser.objects.get(fbid=userid)
		graph = facebook.GraphAPI(user.access_token)
		profile = graph.get_object("me")
		friends = graph.get_connections("me", "friends")
		friend_list = [friend['id'] for friend in friends['data']]
		return friend_list
	except:
		return None

def is_friend(userid, otherid):
	friend_list = get_friend_list(userid)
	if otherid in friend_list:
		return True
	return False

