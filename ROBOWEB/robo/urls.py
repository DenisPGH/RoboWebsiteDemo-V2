from django.urls import path, reverse_lazy

from ROBOWEB.robo.views import button_stop, play_video_button, button_ahead, stop_video_button, RoboSpeakView, \
    open_video

urlpatterns = (
    path("b/",button_stop,name="button_stop"),
    path("bh/",button_ahead,name="button_ahead"),
    path("bv/",play_video_button,name="play_video_button"),
    path("bs/",stop_video_button,name="stop_video_button"),
    path("bss/",open_video,name="open_video"),
    path("bss/",RoboSpeakView.as_view(),name="speak_button"),
)