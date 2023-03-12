from django.urls import path
from . import views

#URL config
urlpatterns=[
    path('', views.home),
    path('login',views.log_in),
    path('register',views.register),
]