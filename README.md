1.	pip install virtualenv
2.	virtualenv env   or python -m venv env
3.	env/script/activate
4.	pip install Django
5.	start a project named demo	# django-admin startproject demo
6.	cd demo
7.	django-admin startapp demo_app
8.	py manage.py makemigrations
9.	py manage.py migrate
10.	activate admin	#py manage.py createsuperuser   create with username and password
urls.py

from django.contrib import admin                    (in demo folder urls then create  a file urls.py in
from django.urls import path,include		demo_app and url provide there)
from demo_app import views

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('',include('demo_app.urls'))
]

Settings.py
INSTALLED_APPS = [
    'demo_app'
]

AUTH_USER_MODEL="demo_app.User"		create model using auth_user


Urls.py
from django.urls import path
from demo_app import views

urlpatterns = [
    
   path('',views.index,name='index')
]

When we migrate and makemigration thetable created from auth user we need to commend the url for admin (#  path('admin/', admin.site.urls),) and inside INSTALLED_APPS = [
#    'django.contrib.admin',] need to commend am migrate and make migration done then uncommend it




Models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    Address=models.CharField(max_length=50,verbose_name='Address')
    Phone_no=models.IntegerField(verbose_name="Phone")
    DOB=models.DateField(verbose_name="Date of Joining")
    class Meta:
        db_table="tbl_user"

class tbl_bustype(models.Model):
   Bus_type=models.CharField(max_length=25)


