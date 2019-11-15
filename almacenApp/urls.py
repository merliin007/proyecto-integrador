# Created by Miguel Angel Aguilar 
# maac35@gmail.com - nov 2019
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth.decorators import login_required
from django.urls import path
from almacenApp.views import UserList, UserRegister, UserUpdate, UserDelete, HomeView, SignUpView, \
    SignInView, SignOutView, StorageList, RoleCreate, RoleList, RoleUpdate, StorageCreate, StorageEdit, \
    StorageDeletion
from . import views

urlpatterns = [
    path('', login_required(views.index), name='index'),
    path('roles', login_required(RoleList.as_view()), name='rolesList'),
    path('roleAdd', login_required(RoleCreate.as_view()), name='roleAdd'),
    path('roleEdit/<pk>', login_required(RoleUpdate.as_view()), name='roleEdit'),
    path('users', login_required(UserList.as_view()), name='usersList'),
    path('userAdd', login_required(UserRegister.as_view()), name='usersAdd'),
    path('userEdit/<pk>/', login_required(UserUpdate.as_view()), name='userEdit'),
    path('userDelete/<pk>/', login_required(UserDelete.as_view()), name='userDelete'),

    path('home/', HomeView.as_view(), name='home'),
    path('signup/', SignUpView.as_view(), name='sign_up'),
    path('signin/', SignInView.as_view(), name='sign_in'),
    path('signout/', SignOutView.as_view(), name='sign_out'),

    # TBD: investigate how to properly change this to use our own custom templates
    path('passwordChange', PasswordChangeView.as_view(), name='pwd_change'),
    path('passwordChange/done', PasswordChangeDoneView.as_view(), name='pwd_change_done'),


    path('storages', login_required(StorageList.as_view()), name='storages'),
    path('storageAdd', login_required(StorageCreate.as_view()), name='storageAdd'),
    path('storageEdit/<pk>/', login_required(StorageEdit.as_view()), name='storageEdit'),
    path('storageDelete/<pk>/', login_required(StorageDeletion.as_view()), name='storageDelete'),
]