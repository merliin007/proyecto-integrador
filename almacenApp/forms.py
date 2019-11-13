# Created by Miguel Angel Aguilar 
# maac35@gmail.com - nov 2019

from django import forms
from almacenApp.models import User


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