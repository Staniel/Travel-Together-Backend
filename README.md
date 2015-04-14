# TravelTogether

TravelTogether is a Android mobile app for user with Facebook account to create, join and share travel plans. Facebook APIs, Google Map APIs, Foursquare APIs are integrated in our app.

This repo is the backend REST api design for our app. 

###API example:

###general description for available endpoints

http://cloud6998.elasticbeanstalk.com/api/v1/?format=json

###list all users

http://cloud6998.elasticbeanstalk.com/api/v1/user/?format=json

###user detail

http://cloud6998.elasticbeanstalk.com/api/v1/user/1/?format=json

###user schema

http://cloud6998.elasticbeanstalk.com/api/v1/user/schema/?format=json

###user in a range

http://cloud6998.elasticbeanstalk.com/api/v1/user/set/1;3/?format=json

###list all plans

http://cloud6998.elasticbeanstalk.com/api/v1/plan/?format=json

###plan detail

http://cloud6998.elasticbeanstalk.com/api/v1/plan/1/?format=json

###plan schema

http://cloud6998.elasticbeanstalk.com/api/v1/plan/schema/?format=json

###plans in a range

http://cloud6998.elasticbeanstalk.com/api/v1/plan/set/1;3/?format=json

###To Do

read more doc of Tastypie, add more functionality of APIs

incorporate python-social-oath

incorporate api authentication