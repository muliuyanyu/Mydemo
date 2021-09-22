# -*-coding:utf-8-*-
# Mydemo
# Author: Feng
# @Time: 2021/9/21 13:59

from django.urls import path
from .views import Register,Login,LogoutUser,Index,change,delate,Create,find,changebtn

urlpatterns = [
    path('',Register.as_view(),name='register'),
    path('login/',Login.as_view(),name='login'),
    path('index/',Index.as_view(),name='index'),
    path('logout/',LogoutUser.as_view(),name='logout'),
    path('change/',change.as_view(),name='change'),
    path('delate/',delate.as_view(),name='delate'),
    path('create/',Create.as_view(),name='create'),
    path('find/',find.as_view(),name='find'),
    path('changebtn/',changebtn.as_view(),name='changebtn'),
]
