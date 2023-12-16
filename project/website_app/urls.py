from django.urls import include, path
from . import views
from .views import CreateFolderView
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.apps import apps


urlpatterns = [

    path("", views.index, name="index"),
    
    path("login/", views.logIn, name="login"),
    path("signUp/", views.signUp, name="signUp"),
    path("profile/", views.profile, name="profile"),

    path("home/<int:id>", views.home, name="home"),
    path("home/<int:id>/adding-folder", CreateFolderView.as_view(), name="adding-folder"),
    # path("home/adding-folder", views.addFolder, name="adding-folder"),


]


