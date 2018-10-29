from django.db import models

# Create your models here.

class UserInfoTest(models.Model):
    user_name = models.CharField(max_length=20)
    user_id = models.CharField(max_length=50)
    user_password = models.CharField(max_length=50)
    def __str__(self):
        return self.user_name#.encode('utf-8')

class PersonInfo(models.Model):
    region = models.CharField(max_length=20)
    area = models.CharField(max_length=50)
    group = models.CharField(max_length=50)
    area_leader = models.CharField(max_length=50)
    director = models.CharField(max_length=50)
    members = models.CharField(max_length=50)
    work_number = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    set_time = models.DateTimeField()
    def __str__(self):
        return self.members#.encode('utf-8')
