from django.urls import path
from .views import *

urlpatterns = [
    path('',index),
    path('register/',register, name='register'),
    path('login/',login, name='login'),
    path('login_page/',login_page, name='login_page'),
    path('register_page/',register_page, name='register_page'),
    path('otp_page/',otp_page, name='otp_page'),
    path('varify_otp/',varify_otp, name='varify_otp'),
    path('profile_page/',profile_page, name='profile_page'),
    path('profile_data/',profile_data, name='profile_data'),
    path('profile_setting_page/',profile_setting_page, name='profile_setting_page'),
    path('sign_out/',sign_out, name='sign_out'),
]