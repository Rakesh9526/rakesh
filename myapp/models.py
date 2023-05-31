from django.db import models

# Create your models here.

class studentdata(models.Model):
    Name = models.CharField(max_length=100,null=True,blank=True)
    Age = models.IntegerField(null=True,blank=True)
    Mobile_number = models.IntegerField(null=True,blank=True)
    Image = models.ImageField(upload_to="profile")