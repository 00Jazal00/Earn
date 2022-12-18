from django.db import models

# Create your models here.
class Join_User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=1000, default="")
    gender = models.CharField(max_length=1000, default="")
    email = models.CharField(max_length=1000, default="")
    mobile_number = models.CharField(max_length=1000, default="")
    qualification = models.CharField(max_length=1000, default="")
    experience = models.CharField(max_length=1000, default="")
    location = models.CharField(max_length=1000, default="")

    def __str__(self):                                  
        return self.username