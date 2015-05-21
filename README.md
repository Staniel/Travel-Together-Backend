# TravelTogether

TravelTogether is a Android mobile app for user with Facebook account to create, join and share travel plans. Facebook APIs, Google Map APIs, Foursquare APIs are integrated in our app.

This repo is the backend REST api design for our app. 

###API example:

###authenticate

POST:
http://cloud6998.elasticbeanstalk.com/v1/auth/:access_token/

{
  'avatar': "url"
}


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
  err:{
    'code': 0,
    'msg': 'success'
  },
  data:{
    'joinable': True,
    'editable': False,
    'joined': True,
    'joined_list':[
      {
        'fbid':'bbb',
        'name':'xinyue'
      },
      {
        'fbid':'ccc',
        'name':'qiuyang'
      }
    ]
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
  planlist:[{
    'planid': 1,
    'holder': {
      'fbid':'aaa',
      'name':'hong'
    },
    'title': 'qqq',
    'description': 'aaa',
    'destination': 'ny',
    'depart_time': 'xxxx-xx-xx',
    'limit': 1,
    'length': 2,
    'visible_type': 1
  }]
  }
}
```

Non-visible private plan will be filtered out at backend. Filtering of non-friend plan would be done in Mobile side.

###To Do

Version 1 finished. Wait for mobile developer providing feedback and make improvement
