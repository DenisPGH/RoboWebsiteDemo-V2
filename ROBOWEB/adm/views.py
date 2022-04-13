from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import mixins as auth_mixin
from django.contrib.auth import views as auth_views
from django.views import generic as views

# Create your views here.
from django.urls import reverse_lazy

from ROBOWEB.adm.forms import AddNewPhotoForm, FormEditUser
from ROBOWEB.first.models import WaitingUser, RoboUser, Images,Profile


def admin_page(request):
    """ this is admin panel, reject or give acces to every register user"""
    denis = Profile.objects.get(pk=request.user.id)

    all_waiting_users = WaitingUser.objects.all()
    all_users = RoboUser.objects.all()
    all_profils=Profile.objects.all()
    galery=Images.objects.all()
    picture=AddNewPhotoForm
    print(request.method)

    if request.method=="GET":
        pass
    context = {

        "denis": denis,
        "waiting_users":all_waiting_users,
        "all_users":all_users,
        "all_profiles":all_profils,
        "galery":galery,
        "picture":picture

    }
    return render(request, 'admin_page.html', context)


@login_required()
def edit_new_user(request,pk):
    """
       get=show form(other usr), post save data(to same url)
       this function edit new user, delete from waiting users and store in users
       """
    user_for_edit = WaitingUser.objects.get(pk=pk)
    if user_for_edit:
        user_form = FormEditUser(instance=user_for_edit)
        if request.method == 'POST':
            print(request.method)
            # here store the new date to the current user
            user_form = FormEditUser(request.POST, request.FILES, instance=user_for_edit)
            if user_form.is_valid():
                # user_form.save()
                new_valid_user = RoboUser(
                    email=user_form.cleaned_data["email"],
                    password=user_form.cleaned_data['password'],
                )
                new_valid_user.save()
                new_valid_profile=Profile(
                    first_name=user_form.cleaned_data["first_name"],
                    last_name=user_form.cleaned_data["last_name"],
                    # email=user_form.cleaned_data["email"],
                    born=user_form.cleaned_data["born"],
                    picture=user_form.cleaned_data.get('picture'),


                    type_user=user_form.cleaned_data['type_user'],
                    user_id=new_valid_user.pk)

                new_valid_profile.save()
                user_for_edit.delete()

                return redirect('admin_page')
        else:
            pass

    contex = {
        "user_for_edit": user_for_edit,
        "user_form": user_form,
        # "new_user":new_user,

    }
    return render(request, "edit_new_user.html", contex)


def reject_new_user(request,pk):
    """this function delete new user, which was reject, in admina page table"""
    user_for_delete = WaitingUser.objects.get(pk=pk)
    user_for_delete.delete()
    return redirect('admin_page')

@login_required()
def add_new_photo(request):
    """" dont work, add new foto to Images"""
    if request =="POST":
        user_form = AddNewPhotoForm(request.POST, request.FILES)
        if user_form.is_valid():
            new_pic=Images(
                pic=user_form.cleaned_data['pic'],
                link=user_form.cleaned_data['link']
            )
            new_pic.save()
        return redirect("admin_page")

class CreateNewPhotoView(auth_mixin.LoginRequiredMixin,views.CreateView):
    """ this view add new picture to the Images in DB"""
    form_class = AddNewPhotoForm
    template_name = 'add_new_photo.html'
    success_url = reverse_lazy('admin_page')
    def form_valid(self, form):
        form.instance.user = self.request.user
        super(CreateNewPhotoView, self).form_valid(form)
        return redirect('admin_page')




def delete_pic_galery(request,pk):
    """" this view delete picture from Images in DB"""
    pic_for_delete=Images.objects.get(id=pk)
    pic_for_delete.delete()

    return redirect('admin_page')


@login_required()
def edit_new_user(request,pk):
    """
       get=show form(other usr), post save data(to same url)
       this function edit new user, delete from waiting users and store in users
       """
    user_for_edit = WaitingUser.objects.get(pk=pk)
    if user_for_edit:
        user_form = FormEditUser(instance=user_for_edit)
        if request.method == 'POST':
            print(request.method)
            # here store the new date to the current user
            user_form = FormEditUser(request.POST, request.FILES, instance=user_for_edit)
            if user_form.is_valid():
                # user_form.save()
                new_valid_user = RoboUser(
                    email=user_form.cleaned_data["email"],
                    password=user_form.cleaned_data['password'],
                )
                new_valid_user.save()
                new_valid_profile=Profile(
                    first_name=user_form.cleaned_data["first_name"],
                    last_name=user_form.cleaned_data["last_name"],
                    # email=user_form.cleaned_data["email"],
                    born=user_form.cleaned_data["born"],
                    picture=user_form.cleaned_data.get('picture'),


                    type_user=user_form.cleaned_data['type_user'],
                    user_id=new_valid_user.pk)

                new_valid_profile.save()
                user_for_edit.delete()

                return redirect('admin_page')
        else:
            pass

    contex = {
        "user_for_edit": user_for_edit,
        "user_form": user_form,
        # "new_user":new_user,

    }
    return render(request, "edit_new_user.html", contex)

@login_required()
def give_access_new_user(request,pk):
    """" to give permission to new user to use website"""
    user_give=Profile.objects.get(user_id=pk)
    user_give.access=True
    user_give.save()
    if len(WaitingUser.objects.all()) >0:
        wait_user=WaitingUser.objects.get(pk=pk)
        wait_user.delete()
    return redirect('admin_page')
@login_required()
def reject_access_new_user(request,pk):
    """" to give permission to new user to use website"""
    user_give=Profile.objects.get(user_id=pk)
    user_give.access=False
    user_give.save()
    if len(WaitingUser.objects.all()) > 0:
        wait_user = WaitingUser.objects.get(pk=pk)
        wait_user.delete()
    return redirect('admin_page')