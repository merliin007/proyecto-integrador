from django.contrib import auth
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Almacen(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.TextField(max_length=500)

    def __str__(self):
        return '{}'.format(self.nombre)

#
# class GroupPermissions(models.Model):
#     role = models.ForeignKey(auth.models.Group, on_delete=models.CASCADE, null=True)
#     perms = models.ForeignKey(auth.models.Permission, on_delete=models.CASCADE, null=True)


class Storage(models.Model):
    storageNumber = models.SmallIntegerField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)


class Perfil(models.Model):
    usuario = models.OneToOneField(auth.models.User, on_delete=models.CASCADE)
    almacen = models.ForeignKey(Almacen, on_delete=models.SET_NULL, null=True, blank=True)
    groups = models.ForeignKey(auth.models.Group, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return '{} {}'.format(self.usuario.first_name, self.usuario.last_name)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Perfil.objects.create(usuario=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, created, **kwargs):
        instance.perfil.save()
