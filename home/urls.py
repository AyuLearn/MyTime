from . import views
from django.urls import path

urlpatterns = [
    path('', views.handleSignup, name='handleSignup'),
    path('login', views.handleLogin, name='handleLogin'),
    path('panel', views.panel, name='panel')
]
