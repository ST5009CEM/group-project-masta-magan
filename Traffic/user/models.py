from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserInfoModel (models.Model):
    id = models.AutoField(auto_created=True,primary_key=True)
    uid = models.ForeignKey(User,on_delete=models.CASCADE,blank=True)
    title = models.CharField(max_length=50)
    badge = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    section = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    role = models.CharField(max_length=55)
    contact = models.CharField(max_length=50)
    area = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    medals = models.CharField(max_length=50,default="0",blank=True)
    solvedcases = models.CharField(max_length=50,default="0",blank=True)
    badge = models.CharField(max_length=50,default="0",blank=True)
    cheat = models.CharField(max_length=55,default="0",blank=True)
    product_image = models.FileField(upload_to="static/image/user",blank=True)

    class Meta:
        db_table= 'userinfo'