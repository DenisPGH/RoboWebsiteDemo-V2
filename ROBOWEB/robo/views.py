from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic as views



# Create your views here.
from ROBOWEB.adm.models import Phrase
from ROBOWEB.robo.forms import FormCreateNewPhrase
from ROBOWEB.robo.helper import StateVideo


@login_required()
def button_stop(request):
    """when button STOP is presed print stop in terminal"""
    print("STOP!!")
    return redirect('login_page')

@login_required()
def button_ahead(request):
    """when button STOP is presed print stop in terminal"""
    print("AHEAD!!")
    return redirect('login_page')



@login_required()
def play_video_button(request):
    StateVideo.STATE_VIDEO=True
    print("PLAY NOW")

    return redirect('login_page')

@login_required()
def stop_video_button(request):
    StateVideo.STATE_VIDEO = False
    print("Stop NOW")

    return redirect('login_page')


class RoboSpeakView(views.UpdateView):
    form_class = FormCreateNewPhrase
    # fields = "__all__"
    success_url = reverse_lazy('login_page')
    context_object_name = 'say'


def open_video(request):
    """this function is not ready"""

    return render(request,'video_page.html')