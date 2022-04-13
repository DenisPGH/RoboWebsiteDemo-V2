from django.urls import path

from ROBOWEB.adm.views import admin_page, edit_new_user, reject_new_user, CreateNewPhotoView, delete_pic_galery, \
    give_access_new_user, reject_access_new_user

urlpatterns = (
    path("a/",admin_page,name="admin_page"),
    path("edituser/<int:pk>/",edit_new_user,name="edit_new_user"),
    # path("reject/<int:pk>/",reject_new_user,name="reject_new_user"),
    path("createpic/",CreateNewPhotoView.as_view(),name="add_new_photo"),
    path("createpic/del/<int:pk>/",delete_pic_galery,name="delete_pic_galery"),
    path("access/<int:pk>/",give_access_new_user,name="give_access_new_user"),
    path("reject/<int:pk>/",reject_access_new_user,name="reject_access_new_user"),
               )