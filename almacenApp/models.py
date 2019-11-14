from django.contrib import auth
from django.db import models
from django.contrib.auth.models import User

class Role(models.Model):
    role = models.CharField(max_length=15)

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


class Almacen(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=500)


class Perfil(models.Model):
    usuario = models.OneToOneField(auth.models.User, on_delete=models.CASCADE)
    almacen = models.ForeignKey('Almacen', on_delete=models.SET_NULL, null=True)

class SingletonModel(models.Model):
    class Meta:
        abstract = True
    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)
    def delete(self, *args, **kwargs):
        pass
    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

class UsuarioAdmin(SingletonModel):
    #usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100, default='Usuario Administrador')
    identificador = models.CharField(max_length=255, default='ACbcad883c9c3e9d9913a715557dddff99')