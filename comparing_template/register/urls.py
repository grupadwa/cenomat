from django.urls import path

from register.views import register, edit_profile, delete_profile


urlpatterns = [

    path("register", register, name="register"),
    path("edit_profile", edit_profile, name="edit_profile"),
    path("delete_profile", delete_profile, name="delete_profile"),

]
