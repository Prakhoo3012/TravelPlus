from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("package/<str:pk>/", views.package, name="each_package"),
    path("register/", views.registerPage, name="register"),
    path("login/", views.loginPage, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("addpackages/", views.addPackages, name="addpackages"),
    path("user/", views.userPage, name="user"),
]