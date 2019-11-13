# Created by Miguel Angel Aguilar 
# maac35@gmail.com - nov 2019

from django.urls import path
from almacenApp.views import UserList
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('roles', views.roles_list, name='rolesList'),
    # path('users', views.user_list, name='usersList'),
    path('users', UserList.as_view(), name='usersList'),
    path('userAdd', views.user_view, name='usersAdd'),
    path('userEdit/<id_user>/', views.user_edit, name='userEdit'),
    path('userDelete/<id_user>/', views.user_delete, name='userDelete'),

]