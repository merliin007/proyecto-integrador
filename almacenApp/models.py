from django.contrib import auth
from django.db import models
from django.contrib.auth.models import User


class Almacen(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.TextField(max_length=500)

    def __str__(self):
        return '{}'.format(self.nombre)


class Permissions(models.Model):
    permission = models.CharField(max_length=30, null=False, blank=True)

    def __str__(self):
        return '{}'.format(self.permission)


class Role(models.Model):
    role = models.CharField(max_length=15)
    permission = models.ManyToManyField(Permissions, blank=True)
    almacen = models.ForeignKey(Almacen, on_delete=models.CASCADE, blank=True, default=1)

    def __str__(self):
        return '{}'.format(self.role)


class User(models.Model):
    firstName = models.CharField(max_length=30, null=False)
    lastName = models.CharField(max_length=30)
    userName = models.CharField(max_length=15, null=False, unique=True)
    password = models.CharField(max_length=20, null=False)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.firstName + ' ' + self.lastName


class Storage(models.Model):
    storageNumber = models.SmallIntegerField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)


class Perfil(models.Model):
    usuario = models.OneToOneField(auth.models.User, on_delete=models.CASCADE)
    # almacen = models.ForeignKey('Almacen', on_delete=models.SET_NULL, null=True)
    role = models.OneToOneField(Role, on_delete=models.CASCADE)
