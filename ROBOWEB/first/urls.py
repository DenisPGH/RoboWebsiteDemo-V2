from django.urls import path, reverse_lazy
from django.views.generic import RedirectView
from ROBOWEB.first.views import LoginPageView, login_page, galery, ProfilDetailsView, \
    LogoutPageView, DeleteProfilView, ChangeUserPasswordView, edit_profil, saved_password, \
    RegistrationView

urlpatterns = (
    path("",LoginPageView.as_view(),name="first_page" ),
    path("r/",RegistrationView.as_view(),name="register_page" ),
    path("l/",login_page,name="login_page" ),
    path("g/",galery,name="galery"),

    path("",LogoutPageView.as_view(),name="logout"),
    path("profil/<int:pk>/",ProfilDetailsView.as_view(),name="profil_page"),
    path("edit/<int:pk>/", edit_profil, name="edit_profil_page"),
    path("delete/<int:pk>/",DeleteProfilView.as_view(),name="delete_profil_page"),
    path("change/",ChangeUserPasswordView.as_view(),name="change_password_page"),
    path("",saved_password,name="saved_password"),
    path('password_change_done/', RedirectView.as_view(url=reverse_lazy('first_page')), name='password_change_done'),
)