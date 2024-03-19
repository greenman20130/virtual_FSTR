#This application is written for api communication between the application and the server. Django was used as the framework. A post request is received from the application and stored in the database. Database objects can be edited if necessary. The api uses rest_framework which is implemented in serializers.py . To work with the api, you need to enable the server with the python command 
'''
python manage.py runserver
''' 
and follow the link to localhost.

The tourist will use the mobile application to transmit the following data about the pass to the FSTR:

Information about yourself:
Surname;
Name;
Middle name;
Email;
Phone number.
The name of the object;
The coordinates of the object and its height;
The difficulty level depends on the time of the year;
A few photos.
After that, the tourist clicks the "Send" button in the mobile application. The mobile application will call the Pereval method.

API using this json format:
'''
{
  "beauty_title": "pass",
  "title": "title",
  "other_titles": "other_titles",
  "connect": "", 
 
  "add_time": "2024-03-19 10:00:00",
  "user": {"email": "name@mail.ru", 		
        "second_name": "",
		 "first_name": "",
		 "middle": "",
        "phone": ""}, 
 
   "coords":{
  "latitude": "42.35325",
  "longitude": "312.152325",
  "height": "800"}
 
 # how difficult is it to cross the pass at this time of the year (('4A', 'winter'), ('2A', 'spring'), ('1A', 'summer'), ('3A', 'autumn'),)

  level:{"winter": "", 
  "summer": "",
  "autumn": "",
  "spring": ""},
 
   images: [{data:"<img>", title:"title_img"},]
}
'''

Method PATCH
'''
PATCH /Pereval/<id>
'''
Editing an existing record (replacement) is possible only with the status "new". Fields with full name, email address and phone number cannot be changed. After editing, the answer comes:

state: 1 — if the record has been successfully updated in the database. 0 — if the update failed.

message: The reason for the failed record update.


Method GET
'''
GET /Pereval/<id>
'''
Retrieves information about a particular pass by its unique identifier, including the moderation status.


Method GET EMAIL
'''
GET /Pereval/?user_id__email=<email>
'''
Allows you to get the data of all objects sent to the server by the user with mail.

The implementation uses filtering by the user's email address using the django-filter package



drf-yasg
'''
swagger: http://127.0.0.1:8000/swagger/
redoc: http://127.0.0.1:8000/redoc/
'''


Project on pythonanywhere.com
'''
https://green20130.pythonanywhere.com
'''