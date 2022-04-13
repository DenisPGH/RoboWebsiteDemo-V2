



# Create your models here.

from django.contrib.auth import models as auth_models
from django.db import models

# Create your models here.
from ROBOWEB.first.managers import AppUsersManager
from ROBOWEB.first.validatros import validator_min_lenght


class Time_C(models.Model):
    """this class store the date info for creating"""
    CREATE_ON= models.DateTimeField(auto_now_add=True,
                                    )
    UPDATE_ON = models.DateTimeField(auto_now=True,
                                     )
    class Meta:
        abstract=True
#
class WaitingUser(Time_C):
    """here store the new users, until get permision from admin user"""
    MAX_LENGHT_FIRST_NAME=30
    MAX_LENGHT_LAST_NAME=30
    MAX_LENGHT_USER_NAME=30
    MAX_LENGHT_PASSWORD=30
    admin="admin"
    random="random"
    type_users=((random,random),(admin,admin))


    user_name=models.CharField( max_length=MAX_LENGHT_USER_NAME,default="a")
    first_name=models.CharField(
        blank=True,
        null=True,
        max_length=MAX_LENGHT_FIRST_NAME)
    last_name=models.CharField(
        blank=True,
        null=True,
        max_length=MAX_LENGHT_LAST_NAME)
    email=models.EmailField()
    born=models.DateField(
        blank=True,
        null=True
    )
    password=models.CharField(
        blank=True,
        null=True,
        max_length=MAX_LENGHT_PASSWORD,
        validators=(
            validator_min_lenght, )
                              )
    picture=models.ImageField(
        upload_to='image_profils',
        blank=True,
        null=True

    )
    # type_user=models.CharField(
    #     max_length=max([len(a) for a,_ in type_users]),
    #     choices = type_users,
    #
    # )




class Images(models.Model):
    pic=models.CharField( max_length=200,)
    link=models.CharField( max_length=200,)



class RoboUser(auth_models.AbstractBaseUser,auth_models.PermissionsMixin):
    email = models.EmailField(
        unique=True,
        # null=False,
        # blank=False,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    USERNAME_FIELD = 'email' # how to be verified in the system, with email

    objects = AppUsersManager()


class Profile(models.Model):
    """ here store all aditional data to the user"""
    MAX_LENGHT_FIRST_NAME = 30
    MAX_LENGHT_LAST_NAME = 30
    admin = "admin"
    random="random"
    type_users=((random,random),(admin,admin))

    access = models.BooleanField(
        default=False,
    )

    first_name = models.CharField(max_length=25,)
    last_name = models.CharField(max_length=MAX_LENGHT_LAST_NAME)
    born = models.DateField(
        blank=True,
        null=True
    )
    picture = models.ImageField(
        upload_to='image_profils',
        blank=True,
        null=True

    )
    type_user = models.CharField(
        max_length=max([len(a) for a, _ in type_users]),
        choices=type_users,
                )

    user = models.OneToOneField(
        RoboUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )
