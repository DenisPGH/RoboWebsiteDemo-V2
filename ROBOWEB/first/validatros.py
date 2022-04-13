from django.core.exceptions import ValidationError
# from ROBO.first.models import User
#from ROBO.first.helper import logged_user


def validator_min_lenght(text):
    """this function validate, if text is less than bestimt value"""
    how_much=8
    if len(text)<how_much:
        raise ValidationError(f"The text must be at least {how_much} long")

def vaidator_current_username(name):
    """ this function prove the correct user name"""
    right_name="Denislav"
    if name != right_name:
        raise ValidationError(f"There is no registration with {name}! ")

def validator_current_user_password():
    pass