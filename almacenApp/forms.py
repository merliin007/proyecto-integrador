# Created by Miguel Angel Aguilar 
# maac35@gmail.com - nov 2019
from betterforms.multiform import MultiModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from django.forms import ModelForm
from almacenApp.models import Perfil, Almacen


class RoleForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = [
            'name',
        ]
        labels = {
            'name': 'Rol',
        }
        widgets ={
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class UserModelForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
        ]

        labels = {
            'username': 'User Name',
            'email': 'Email',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'password1': 'Password',
            'password2': 'Confirma Password',
        }

        widgets ={
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }


class PerfilModelForm(ModelForm):
    class Meta:
        model = Perfil
        fields = [
            'usuario',
            'almacen',
            'groups',
        ]
        labels = {
            'usuario': 'Usuario',
            'almacen': 'Almacen',
            'groups': 'Rol',
        }
        widgets ={
            'usuario': forms.Select(attrs={'class':'form-control'}),
            'almacen': forms.Select(attrs={'class':'form-control'}),
            'groups': forms.Select(attrs={'class':'form-control'}),
        }


class PerfilModelFormEdit(ModelForm):
    class Meta:
        model = Perfil
        fields = [
            'usuario',
            'almacen',
            'groups',
        ]
        labels = {
            'usuario': 'Usuario',
            'almacen': 'Almacen',
            'groups': 'Rol',
        }
        widgets ={
            'usuario': forms.Select(attrs={'class':'form-control'}),
            'almacen': forms.Select(attrs={'class':'form-control'}),
            'groups': forms.Select(attrs={'class':'form-control'}),
        }


class StorageForm(ModelForm):
    class Meta:
        model = Almacen
        fields =[
            'nombre',
            'direccion',
        ]
        labels ={
            'nombre': 'Nombre del Almacen',
            'direccion': 'Direccion'
        }
        widgets={
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'direccion': forms.Textarea(attrs={'class':'form-control'}),
        }


class StorageFormSimple(ModelForm):
    class Meta:
        model = Almacen
        fields =[
            'nombre',
        ]
        labels ={
            'nombre': 'Nombre del Almacen',
        }
        widgets={
            'nombre': forms.Select(attrs={'class':'form-control'}),
        }


class GroupPermissionsForm(ModelForm):
    pass
    # class Meta:
    #     model = GroupPermissions
    #     fields = [
    #         'groups',
    #         'perms',
    #     ]
    #     labels = {
    #         'groups': 'Rol',
    #         'perms': 'Permisos',
    #     }
    #     widgets = {
    #         'groups': forms.Select(attrs={'class':'form-control'}),
    #         'perms': forms.SelectMultiple(),
    #     }

