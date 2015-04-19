# TravelTogether

TravelTogether is a Android mobile app for user with Facebook account to create, join and share travel plans. Facebook APIs, Google Map APIs, Foursquare APIs are integrated in our app.

This repo is the backend REST api design for our app. 

###API example:

###general description for available endpoints

http://cloud6998.elasticbeanstalk.com/api/v1/?format=json

###authenticate

http://cloud6998.elasticbeanstalk.com/api/v1/auth/?access_token=XXX

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

POST: http://cloud6998.elasticbeanstalk.com/api/v1/plan/add/?access_token=XXX&format=json
```
{
  'title': 'XXX',
  'destination': 'XXX',
  'depart_time': XXXX-XX-XX,
  'length': 3,
  'description': "XXX",
  'type': 'all'|'friends'|'private',
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

PUT: http://cloud6998.elasticbeanstalk.com/api/v1/plan/edit/:planid?access_token=XXX&format=json

```
{
  'title': 'XXX',
  'destination': 'XXX',
  'depart_time': XXXX-XX-XX,
  'length': 3,
  'description': "XXX",
  'type': 'all'|'friends'|'private',
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

DELETE : http://cloud6998.elasticbeanstalk.com/api/v1/plan/delete/:planid?access_token=XXX&format=json

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

POST : http://cloud6998.elasticbeanstalk.com/api/v1/plan/join/:planid?access_token=XXX&format=json

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

POST : http://cloud6998.elasticbeanstalk.com/api/v1/plan/unjoin/:planid?access_token=XXX&format=json

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


###list all plans

GET: http://cloud6998.elasticbeanstalk.com/api/v1/plan/?type=all|mine|joined&access_token=XXX&format=json

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
    'visible_type': 0
  }]
  }
}
```

Non-visible private plan will be filtered out at backend. Filtering of non-friend plan would be done in Mobile side.

###To Do

read more doc of Tastypie, add more functionality of APIs

incorporate api authentication
