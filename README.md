# TravelTogether

TravelTogether is a Android mobile app for user with Facebook account to create, join and share travel plans. Facebook APIs, Google Map APIs, Foursquare APIs are integrated in our app.

This repo is the backend REST api design for our app. 

###API example:

###authenticate

POST:
http://cloud6998.elasticbeanstalk.com/v1/auth/:access_token/
```
{
  'avatar': "url"
}
```

result:
```
{
  err:{
    code:400,
    msg: 'invalid token'
  },
  data:{}
}
```

###add plans

POST: http://cloud6998.elasticbeanstalk.com/v1/add/:access_token/
```
{
  'title': 'XXX',
  'destination': 'XXX',
  'depart_time': XXXX-XX-XX,
  'length': 3,
  'description': "XXX",
  'type': 1, //(1 'all'| 2 'friends'|3 'private',)
  'limit':5,
  'friendlist':['fbid1', 'fbid2']
}
```

return:
```
{
  err:{
    code:0,
    msg:'success'
  },
  data:{}
}
```

###edit plans

POST: http://cloud6998.elasticbeanstalk.com/v1/edit/:access_token/:planid/

```
{
  'title': 'XXX',
  'destination': 'XXX',
  'depart_time': XXXX-XX-XX,
  'length': 3,
  'description': "XXX",
  'type': 1, //(1 'all'| 2 'friends'|3 'private',)
  'limit':5,
  'friendlist':['fbid1', 'fbid2']
}
```

return:
```
{
  err:{
    code:0,
    msg:'success'
  },
  data:{}
}
```

###Delete plan

DELETE : http://cloud6998.elasticbeanstalk.com/v1/delete/:access_token/:planid/

return:

```
{
  err:{
    code:0,
    msg:'success'
  },
  data:{}
}
```


###join plan

POST : http://cloud6998.elasticbeanstalk.com/v1/join/:access_token/:planid/

return:

```
{
  err:{
    code:0,
    msg:'success'
  },
  data:{}
}
```

###unjoin plan

POST : http://cloud6998.elasticbeanstalk.com/v1/plan/unjoin/:access_token/:planid/

return:

```
{
  err:{
    code:0,
    msg:'success'
  },
  data:{}
}
```

###get plan detail

get joined user fbid and name for this plan and other joinable editable condition, other info has already been retrieved in list page.

GET: http://cloud6998.elasticbeanstalk.com/v1/plan/:access_token/:planid/

result:
```
{
    "data": {
        "joinable": false,
        "editable": false,
        "plan_id": "1",
        "joined": false,
        "joined_list": [
            {
                "id": "123456",
                "avatar": "",
                "name": "Terrence"
            },
            {
                "id": "56677",
                "avatar": "",
                "name": "Staniel"
            }
        ]
    },
    "err": {
        "msg": "success",
        "code": 0
    }
}
```


###list all plans

GET: http://cloud6998.elasticbeanstalk.com/v1/plan/:access_token/:type/

type=all|mine|joined

result:
```
{
  err:{
    'code': 0,
    'msg': 'success'
  },
  data:{
  [{
            "count": 2,
            "length": 3,
            "plan_id": 1,
            "description": "hahha",
            "title": "trip to Seattle",
            "visible_type": 1,
            "limit": 3,
            "destination": "Seattle",
            "holder": {
                "id": "367582766756159",
                "avatar": "",
                "name": "Lixin Daniel Yao"
            },
            "depart_time": "2015-04-19 22:09:24+00:00"
        }]
}
```

Non-visible private plan will be filtered out at backend. Filtering of non-friend plan would be done in Mobile side.

###To Do

Version 1 finished. Wait for mobile developer providing feedback and make improvement
