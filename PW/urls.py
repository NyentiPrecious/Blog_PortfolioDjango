from django.urls import path, include
from PW import views

urlpatterns = [
    # path('', views.PW, name='PW'),
    path('Homepage', views.Homepage, name='Homepage'),
    path('Main', views.Main, name='Main'),
    path('Student', views.Student, name='Student'),
    path('photo', views.photo, name='photo'),
    path('Web', views.Web, name='Web'),
    path('Marketing', views.Marketing, name='Marketing'),
]