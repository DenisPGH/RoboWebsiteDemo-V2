from ROBOWEB.first.models import WaitingUser

def logged_user():
    profiles=WaitingUser.objects.filter()
    if profiles:
        current_user=profiles[0] # which user here
        return current_user
    return None