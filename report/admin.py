from django.contrib import admin

# Register your models here.
from .models import *


class UserInfoTestAdmin(admin.ModelAdmin):
    list_display = ['user_name','user_id','user_password']
class PersonInfoAdmin(admin.ModelAdmin):
    list_display = ['region','area','group','area_leader','director','members','work_number','position','set_time']

admin.site.register(UserInfoTest,UserInfoTestAdmin)
admin.site.register(PersonInfo,PersonInfoAdmin)


