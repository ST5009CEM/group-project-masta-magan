from turtle import color
from django.db import models

# Create your models here.

class CheatModel (models.Model):
    id = models.AutoField(auto_created=True,primary_key=True)
    billbook = models.CharField(max_length=50)
    licence = models.CharField(max_length=50)
    name = models.TextField(max_length=225)
    number = models.TextField(max_length=50)
    vechilename = models.TextField(max_length=100)
    phonenumber = models.TextField(max_length=100)
    type = models.TextField(max_length=225)
    fine = models.TextField(max_length=10)

    class Meta:
        db_table= 'cheat'

class LostModel (models.Model):
    id = models.AutoField(auto_created=True,primary_key=True)
    vechiletype = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    color = models.TextField(max_length=225)
    number = models.TextField(max_length=50)
    vechilename = models.TextField(max_length=100)
    phonenumber = models.TextField(max_length=100)
    enginenumber = models.TextField(max_length=225)
    date = models.TextField(max_length=50)
    resolved = models.TextField(max_length=10, blank=True, default='reported')

    class Meta:
        db_table= 'lost'

