from django.contrib.auth.models import User, Group, Permission
from django.contrib import auth
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import pdb


class Almacen(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.TextField(max_length=500)

    def __str__(self):
        return '{}'.format(self.nombre)


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
        return obj, created


class UsuarioAdmin(SingletonModel):
    nombre = models.CharField(max_length=100, default='Usuario Administrador')
    identificador = models.CharField(max_length=255, default='ACbcad883c9c3e9d9913a715557dddff99')


class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    almacen = models.ForeignKey(Almacen, on_delete=models.SET_NULL, null=True)
    groups = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True)
    user_perms = models.ManyToManyField(Permission, null=True, related_name='perfil')

    def __str__(self):
        return '{} {}'.format(self.usuario.first_name, self.usuario.last_name)

    # @receiver(post_save, sender=User)
    # def create_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         Perfil.objects.create(usuario=instance)

    # @receiver(post_save, sender=User)
    # def save_user_profile(sender, instance, created, **kwargs):
    #     instance.perfil.save()
