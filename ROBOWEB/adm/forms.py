from django import forms

from ROBOWEB.first.forms import FormPlaceHolderMixin
from ROBOWEB.first.models import WaitingUser, Images


class FormEditUser(forms.ModelForm):
    """ not using this form"""

    """create form to edit the each fileds in edit_page"""
    class Meta:
        model=WaitingUser
        fields='__all__'


class AddNewPhotoForm(FormPlaceHolderMixin,forms.ModelForm):
    """this Form show fields for save new picture to Images in DB"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_muster_place_holder_and_form_control()

    # pic = forms.CharField(max_length=25, )
    # link = forms.ImageField()

    # def save(self, commit=True):
    #     # commit false does not persist to database
    #     # just returns the object to be created
    #     pet = super().save(commit=False)
    #     pet.save()
    #     return pet
    class Meta:
        model=Images
        fields=('pic',"link")
        # widgets = {
        #     'pic': forms.TextInput(),
        # }

    def save(self, commit=True):

        image = Images(
            pic=self.cleaned_data['pic'],
            link=self.cleaned_data['link'],
        )
        image.save()
        return image