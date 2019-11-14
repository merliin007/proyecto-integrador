# Created by Miguel Angel Aguilar 
# maac35@gmail.com - nov 2019

from django.urls import path
from almacenApp.views import UserList, UserCreate, UserUpdate, UserDelete, HomeView, SignUpView, \
    SignInView, SignOutView, StorageList
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('roles', views.roles_list, name='rolesList'),
    path('users', UserList.as_view(), name='usersList'),
    path('userAdd', UserCreate.as_view(), name='usersAdd'),
    path('userEdit/<pk>/', UserUpdate.as_view(), name='userEdit'),
    path('userDelete/<pk>/', UserDelete.as_view(), name='userDelete'),

    path('home/', HomeView.as_view(), name='home'),
    path('signup/', SignUpView.as_view(), name='sign_up'),
    path('signin/', SignInView.as_view(), name='sign_in'),
    path('signout/', SignOutView.as_view(), name='sign_out'),

    path('storages', StorageList.as_view(), name='storages')
]