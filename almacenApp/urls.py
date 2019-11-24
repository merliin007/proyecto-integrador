# Created by Miguel Angel Aguilar 
# maac35@gmail.com - nov 2019
from django.urls import path
from almacenApp.views import UserList, UserRegister, UserUpdate, UserDelete, HomeView, SignUpView, \
    SignInView, SignOutView, StorageList, RoleCreate, RoleList, RoleUpdate, StorageCreate, StorageEdit, \
    StorageDeletion, RoleAssignList, RoleAssignEdit, IndexView

from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('roles', RoleList.as_view(), name='rolesList'),
    path('roleAdd', RoleCreate.as_view(), name='roleAdd'),
    path('roleEdit/<pk>', RoleUpdate.as_view(), name='roleEdit'),

    path('roleAssign/', RoleAssignList.as_view(), name='roleAssignList'),
    path('roleStorageAssignEdit/<pk>', RoleAssignEdit.as_view(), name='roleStorageAssignEdit'),
    path('users', UserList.as_view(), name='usersList'),
    path('userAdd', UserRegister.as_view(), name='usersAdd'),
    path('userEdit/<pk>/', UserUpdate.as_view(), name='userEdit'),
    path('userDelete/<pk>/', UserDelete.as_view(), name='userDelete'),
    path('userRoleEdit/<pk>', RoleAssignEdit.as_view(), name='userRoleEdit'),

    path('home/', HomeView.as_view(), name='home'),
    path('signup/', SignUpView.as_view(), name='sign_up'),

    path('signin/', SignInView.as_view(), name='sign_in'),
    path('signout/', SignOutView.as_view(), name='sign_out'),
    path('password-change/', PasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),

    path('passwordChange', PasswordChangeView.as_view(), name='pwd_change'),
    path('passwordChange/done', PasswordChangeDoneView.as_view(), name='pwd_change_done'),


    path('storages/', StorageList.as_view(), name='storages'),
    path('storageAdd', StorageCreate.as_view(), name='storageAdd'),
    path('storageEdit/<pk>/', StorageEdit.as_view(), name='storageEdit'),
    path('storageDelete/<pk>/', StorageDeletion.as_view(), name='storageDelete'),
]