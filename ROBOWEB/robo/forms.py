from ROBOWEB.adm.models import Phrase
from ROBOWEB.first.forms import FormPlaceHolderMixin
from django.contrib.auth import forms as auth_forms, get_user_model
from django import forms



class FormCreateNewPhrase(FormPlaceHolderMixin,forms.ModelForm):
    """ Class Form for editing the personal data for logged user"""
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self._init_muster_place_holder_and_form_control()
    """this class is forma for editing in profil page"""
    class Meta:
        model=Phrase
        fields='__all__'
        # widgets = {
        #    'phrase': forms.Textarea(
        #        attrs={'rows':3}
        #    )
        # }