from django.urls import path
from . import views

app_name='website'

urlpatterns=[
        path('', views.landing, name='landing'),
        path('signup', views.signup, name='signup'),
        path('welcome', views.welcome, name='welcome'),
        ]
