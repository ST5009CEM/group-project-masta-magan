from django.db import models

# Create your models here.

class CheatModel (models.Model):
    id = models.AutoField(auto_created=True,primary_key=True)
    billbook = models.CharField(max_length=50)
    licence = models.CharField(max_length=10)
    name = models.TextField(max_length=225)
    number = models.TextField(max_length=50)
    vechilename = models.TextField(max_length=100)
    vechiletype= models.TextField(max_length=100,blank=True)
    phonenumber = models.TextField(max_length=100)
    type = models.TextField(max_length=225)
    fine = models.TextField(max_length=10)

    class Meta:
        db_table= 'cheat'

