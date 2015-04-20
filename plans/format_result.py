def format(errcode, msg="", data={}):
	return {
	'err': {
		'code': errcode,
		'msg': msg
	},
	'data': data
	}