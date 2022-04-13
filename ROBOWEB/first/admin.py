from django.contrib import admin

# Register your models here.
from ROBOWEB.first.models import RoboUser, Images, WaitingUser,Profile


@admin.register(RoboUser)
class TaskUser(admin.ModelAdmin):
    list_display = ('password','last_login','email')

@admin.register(Profile)
class TaskProfile(admin.ModelAdmin):
    list_display = ('first_name','last_name','born','picture','type_user','user_id')


@admin.register(WaitingUser)
class TaskWaitingUser(admin.ModelAdmin):
    list_display = ('first_name','last_name','email','born','password','picture')

@admin.register(Images)
class TaskImages(admin.ModelAdmin):
    list_display = ('pic','link')
