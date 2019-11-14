from django.contrib import admin
from almacenApp.models import Role, User, Perfil, Almacen

# Register your models here.

admin.site.register(Role)
admin.site.register(User)
admin.site.register(Almacen)
admin.site.register(Perfil)