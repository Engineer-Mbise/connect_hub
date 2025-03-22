from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("create_module/", views.create_module, name="create_module"),
    path("", views.list_of_modules, name="index"),
    path("discussions/<str:mdl>/", views.list_of_filtered_discussions, name="list_of_filtered_discussions"),
    path("discussions", views.list_of_discussions, name="discussions"),
]