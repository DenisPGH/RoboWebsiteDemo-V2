from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import forms as auth_forms, get_user_model

from ROBOWEB.first.models import RoboUser, WaitingUser, Profile, Images


# class FormFirstPage(forms.Form):
#     """this class create buttons and collect info during the both fileds on first page-login """
#     first_name=forms.CharField(
#         max_length=User.MAX_LENGHT_FIRST_NAME,
#         validators=(
#             vaidator_current_username,
#         ),
#     )
#     password=forms.CharField(
#         max_length=User.MAX_LENGHT_PASSWORD,
#         validators=(
#             validator_min_lenght,
#         )
#     )

class FormPlaceHolderMixin:
    """this function has no init field and is for children, place holder and class:form control"""
    @staticmethod
    def Make_name_better(name):
        """this function make the names looks beter 'first_name'==First Name """
        #new_name=name.capitalize()
        new_name=name
        if "_" in new_name:
            new_name=new_name.replace('_'," ")
        return new_name


    def _init_muster_place_holder_and_form_control(self):
        for name_field,field in self.fields.items():
            if not hasattr(field.widget,'attrs'):
                setattr(field.widget,'atrrs',{})
            if 'placeholder' not in field.widget.attrs:
                field.widget.attrs['placeholder']=''
            field.widget.attrs['placeholder']+=\
                f"Enter your {FormPlaceHolderMixin.Make_name_better(name_field)} here:"
            if 'class' not in field.widget.attrs:
                field.widget.attrs['class']=''
            field.widget.attrs['class']+="form-control"

    # def _init_muster_form_control(self):
    #     for _,field in self.fields.items():
    #         if not hasattr(field.widget,'attrs'):
    #             setattr(field.widget,'atrrs',{})
    #         if 'class' not in field.widget.attrs:
    #             field.widget.attrs['class']=''
    #         field.widget.attrs['class']+="form-control"


# class FormFirstPage(FormPlaceHolderMixin,forms.ModelForm):
#     """model forma for first page"""
#     def __init__(self,*args,**kwargs):
#         super().__init__(*args,**kwargs)
#         self._init_muster_place_holder_and_form_control()
#
#     class Meta:
#         model=User
#         fields=('first_name','password')
#
#
#
#     def clean_first_name(self):
#         if self.cleaned_data['first_name'] !="Denislav":
#             raise forms.ValidationError(f"{self.cleaned_data['first_name']} not in our DB")
#         return self.cleaned_data['first_name']
#
#         # widgets={
#         #     'first_name':forms.TextInput(
#         #         attrs={
#         #             'placeholder':" Enter First name",
#         #         }
#         #     ),
#         # }
#
#     def valid_name_first_name(self):
#         # dont work
#         cur_name=self.cleaned_data['first_name']
#         print(f"name={cur_name}")
#         if not cur_name== "Denislav":
#             raise ValidationError("Not in our DB")
#         #return None

class FormRegistrationPost(FormPlaceHolderMixin,forms.ModelForm):
    """this function give to user to store the data from registration form,
    make the windows with the input"""
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self._init_muster_place_holder_and_form_control()


    class Meta:
        model=WaitingUser
        #fields='__all__'
        fields=('user_name',"first_name","last_name","email","born","password","picture")
        # widgets={
        #     "confirm_password":forms.TextInput()
        # }

    # admin = "admin"
    # random = "random"
    # type_users = ((random, random), (admin, admin))

    # user_name = forms.CharField(max_length=User.MAX_LENGHT_FIRST_NAME)
    # first_name = forms.CharField(max_length=User.MAX_LENGHT_FIRST_NAME)
    # last_name = forms.CharField(max_length=User.MAX_LENGHT_LAST_NAME)
    # email = forms.EmailField()
    # born = forms.DateField()
    # password = forms.CharField(
    #     max_length=User.MAX_LENGHT_PASSWORD,
    #     min_length=2
    # )
    # picture = forms.ImageField()
    #     # null=True,
    #     # blank=True,
    #     # upload_to="media/image_profils",)
    # # type_user = forms.CharField(
    # #     max_length=max([len(a) for a, _ in type_users]),
    # #     choices=type_users,
    # #     default='---'
    # # )




class FormEditProfil(FormPlaceHolderMixin,forms.ModelForm):
    """ Class Form for editing the personal data for logged user"""
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self._init_muster_place_holder_and_form_control()
    """this class is forma for editing in profil page"""
    class Meta:
        model=Profile
        fields=("first_name","last_name","born","picture")
        # fields='__all__'

class CreateNewUserForm(FormPlaceHolderMixin,auth_forms.UserCreationForm):
    """" Form for creatiin profil"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_muster_place_holder_and_form_control()

    first_name = forms.CharField(max_length=25, )
    last_name = forms.CharField(max_length=Profile.MAX_LENGHT_LAST_NAME)
    email = forms.EmailField()
    born = forms.DateField(

    )
    picture = forms.ImageField()
    # type_user = forms.CharField(
    #     max_length=max([len(a) for a, _ in Profile.type_users]),
    #     choices=Profile.type_users,
    # )
    # type_user = forms.ChoiceField(
    #     choices=Profile.type_users,
    # )

    def save(self, commit=True):
        user = super().save(commit=commit)

        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            picture=self.cleaned_data['picture'],
            born=self.cleaned_data['born'],
            user=user,
        )


        if commit:
            profile.save()
            wait_user = WaitingUser(
                first_name=self.cleaned_data['first_name'],
                last_name=self.cleaned_data['last_name'],
                id=profile.pk,

            )
            wait_user.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ('password1', 'password2', 'first_name', 'last_name', 'picture', 'born',"email")
        #widgets = {
        # widgets = {
        #     'first_name': forms.TextInput(
        #         attrs={
        #             'placeholder': 'Enter first name',
        #         }
        #     ),
        #     'last_name': forms.TextInput(
        #         attrs={
        #             'placeholder': 'Enter last name',
        #         }
        #     ),
        #     'picture': forms.TextInput(
        #         attrs={
        #             'placeholder': 'Enter URL',
        #         }
        #     ),
        # }










# class FormDeleteUser(forms.ModelForm):
#     """ delete the loged user"""
#     class Meta:
#         model=RoboUser
#         fields=('user_name',"first_name","last_name","email","born","password","picture")