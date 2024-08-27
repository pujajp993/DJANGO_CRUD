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