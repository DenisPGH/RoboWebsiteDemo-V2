from django.contrib.auth.views import LoginView,LogoutView
from  django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import generic as views
from django.contrib.auth import views as auth_views, get_user_model
from django.contrib.auth import mixins as auth_mixin

# Create your views here.
from django.urls import reverse_lazy

from ROBOWEB.adm.models import Phrase
from ROBOWEB.first.forms import FormRegistrationPost, FormEditProfil, CreateNewUserForm, \
    FormPlaceHolderMixin
from ROBOWEB.first.models import WaitingUser, Images, RoboUser,Profile
from ROBOWEB.robo.forms import FormCreateNewPhrase
from ROBOWEB.robo.helper import StateVideo
from ROBOWEB.robo.views import RoboSpeakView, play_video_button


class RedirectToLoginPage:
    """" this is help class for redirecting"""
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('login_page')

        return super().dispatch(request, *args, **kwargs)


class LoginPageView(LoginView, FormRegistrationPost):

    """ new class view for login"""
    template_name = 'first_page.html'
    def get_success_url(self):
        return reverse_lazy('login_page')

class LogoutPageView(LogoutView):
    """ by pressing logout, redirect to fitst page"""
    def get_success_url(self):
        return reverse_lazy('first_page')


class RegistrationView(views.CreateView):
    """" This View start the register page form for new users"""
    form_class = CreateNewUserForm
    template_name = 'register_page.html'
    success_url = reverse_lazy('first_page')

# def register_page(request):
#     """this function start regirstration page
#     with all fields, and make new user ask waiting for confirmation """
#     print(request.method)
#     print(request.FILES)
#     if request.method=='POST':
#         registration=FormRegistrationPost(request.POST,request.FILES)
#         if registration.is_valid():
#             #save the collected date to the bd
#             new_waiting_user=WaitingUser(
#                 user_name=registration.cleaned_data['user_name'],
#                 first_name=registration.cleaned_data["first_name"],
#                 last_name=registration.cleaned_data["last_name"],
#                 email=registration.cleaned_data["email"],
#                 born=registration.cleaned_data["born"],
#                 password=registration.cleaned_data['password'],
#                 picture=registration.cleaned_data.get('picture'),
#             )
#             new_waiting_user.save()
#             return redirect('first_page')
#     else:
#         registration=FormRegistrationPost()
#     context={
#         "registration":registration,
#     }
#     return render(request, 'register_page.html', context)

# def first_page(request):
#     """
#     this function start the main screen, if login is succes start login_page,
#     else stay in same page but error occure and show error
#     """
#     #print(request.method)
#     invalid_user=False
#     form=FormFirstPage()
#
#     if request.method=='POST':
#         form=FormFirstPage(request.POST)
#         if form.is_valid():
#             #form.save()
#             return redirect('login_page')
#     context={
#         'login':form,
#         'invalid_user':invalid_user
#             }
#     return render(request, "first_page.html", context)

def login_page(request):
    """this page is important, show login, control panel, video, all"""
    status_video=StateVideo.STATE_VIDEO
    #current_user =Profile.objects.get(pk=get_user_model().id)
    current_user =Profile.objects.get(pk=request.user.id)
    new_users = 0
    all_waiting_users = WaitingUser.objects.all()
    if len(all_waiting_users) > 0:
        new_users = len(all_waiting_users)
    # print(current_user)

    all_phrases= Phrase.objects.all().order_by('-id')
    to_write=Phrase.objects.all()[0]  #.values_list('id', flat=True).order_by('-id').first()
    if  all_phrases:
        to_write =all_phrases[0]
        # YOU CAN TAKE MESSAGE FOR THE ROBO FROM HERE
    say_form =FormCreateNewPhrase()
    if request.method=="POST":
        print(f'SAY==={request.method}')
        say_form = FormCreateNewPhrase(request.POST)
        if say_form.is_valid():
            new_phrase=Phrase(phrase=say_form.cleaned_data['phrase'])
            new_phrase.save()
            to_write=Phrase.objects.all()[0]
            for_delete = all_phrases[1]
            for_delete.delete()
            return redirect('login_page')

    context={

        "new_waiting_users": new_users,
        "current_user":current_user,
        "denis": current_user.first_name,
        'pk':current_user.pk,
        'say_form':say_form,
        'to_write':to_write.phrase,
        'status_video':status_video,
    }

    return render(request, 'login_page.html', context)


def galery(request):
    """ this function shows the pictures from images tabel"""
    pictures = Images.objects.all()
    context={
        'pictures':pictures,
    }
    return render(request, "galery_page.html", context)



class ProfilDetailsView(views.DetailView):
    """ start personal info for random profil"""
    model = Profile
    template_name = 'profil_page.html'
    context_object_name = "form"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # self.object is a Profile instance
        added_profile = Profile.objects.get(user_id=self.object.user_id)
        user_profil=RoboUser.objects.get(id=self.object.user_id)
        context['profile']=added_profile
        context['user_profil']=user_profil
        return context



class EditProfilView(views.UpdateView):
    """Not in use"""
    """this function edit the profil details"""
    #model = Profile
    #fields = ('first_name','last_name',"picture",'born')
    form_class = FormEditProfil
    template_name = 'edit_profil_page.html'

    # def form_valid(self, form):
    #     pass

    #slug_field = 'email'
    #slug_url_kwarg = 'slug'


    def get_success_url(self):
        return reverse_lazy('profil_page',kwargs={'pk':self.object.user_id})
    # def get_object(self, queryset=None):
    #     pass


class ChangeUserPasswordView(auth_views.PasswordChangeView):
    """" this class change the password of logged user and return himself to first page"""
    template_name = 'change_password_page.html'

@login_required()
def saved_password(request):
    """" not sure if I use this function, think not"""

    return redirect('admin_page')

    # def get_success_url(self):
    #     print(self.kwargs['user_id'])
    #     return reverse_lazy('profil_page',kwargs={'pk':self.kwargs['user_id']})

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     profile = RoboUser.objects.get(pk=1)
    #     context['profile']=profile
    #     return context

class DeleteProfilView(views.DeleteView):
    pass







def edit_profil(request, pk):
    """
    get=show form(other usr), post save data(to same url)
    this function edit new user, delete from waiting users and store in users
    """
    user_for_edit=Profile.objects.get(pk=pk)
    print(user_for_edit.__dict__)
    if user_for_edit:
        if request.method == 'POST':
            print(request.method)
            #here store the new date to the current user
            user_form=FormEditProfil(request.POST,request.FILES,instance=user_for_edit)
            if user_form.is_valid():

                user_for_edit.save()
                # new_valid_user=RoboUser(
                #
                #         first_name=user_form.cleaned_data["first_name"],
                #         last_name=user_form.cleaned_data["last_name"],
                #         email=user_form.cleaned_data["email"],
                #         born=user_form.cleaned_data["born"],
                #         picture=user_form.cleaned_data.get('picture'),
                # )


                # new_valid_user.save()


                return redirect('profil_page',pk)


    contex={
        "user_for_edit":user_for_edit,
        #"profile":user_for_edit,
        "form":FormEditProfil(instance=user_for_edit),


    }
    return render(request, "edit_profil_page.html", contex)




