from django.urls import path
from .views import *

urlpatterns = [
    path('register/',register,name='register'),
    path('',login_,name='login_'),
    path('logout_/',logout_,name='logout_'),
    path('profile/',profile,name='profile'),
    path('reset/',reset,name='reset'),
    path('forgot/',forgot,name='forgot'),
    path('new_password/',new_password,name='new_password')
]