# Created by Miguel Angel Aguilar 
# maac35@gmail.com - nov 2019
from betterforms.multiform import MultiModelForm
from django import forms
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from almacenApp.models import User, Perfil


class UsuarioForm(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            'firstName',
            'lastName',
            'userName',
            'password',
            'role',
        ]

        labels = {
            'firstName': 'Nombre',
            'lastName': 'Apellido',
            'userName': 'User Name',
            'password': 'Password',
            'role': 'Rol',
        }

        widgets = {
            'firstName':    forms.TextInput(attrs={'class': 'form-control'}),
            'lastName':     forms.TextInput(attrs={'class': 'form-control'}),
            'userName':     forms.TextInput(attrs={'class': 'form-control'}),
            'password':     forms.PasswordInput(attrs={'class': 'form-control'}),
            'role':         forms.Select(attrs={'class': 'form-control'}),
        }


class UserModelForm(UserCreationForm):
    class Meta:
        model = auth.models.User
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
        fields = ['almacen'] # No agregar el campo 'persona'


class PerfilUserModelForm(MultiModelForm):
    form_classes = {
        'user': UserModelForm,
        'perfil': PerfilModelForm,
    }