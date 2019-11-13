from django.shortcuts import render, redirect
from almacenApp.models import Role, User
from almacenApp.forms import UsuarioForm
from django.views.generic import ListView

def index(request):
    # return HttpResponse("Index")
    return render(request, "almacenes/index.html",)


def roles_list(request):
    list_roles = Role.objects.all()
    context = {
        'roles_obj': list_roles,
    }
    return render(request, "almacenes/roles_list.html", context)


def user_list(request):
    list_users = User.objects.all()
    context = {
        'user_list' :  list_users,
    }
    return render(request, "almacenes/users_list.html", context)


def user_view(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('usersList')
    else:
        form = UsuarioForm()
    return render(request,  'almacenes/users_form.html', {'form': form})


def user_edit(request, id_user):
    user = User.objects.get(id=id_user)
    if request.method == 'GET':
        form = UsuarioForm(instance=user)
    else:
        form = UsuarioForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
        return redirect('usersList')
    context = {
        'form': form,
    }
    return render(request, 'almacenes/users_form.html', context)


def user_delete(request, id_user):
    user = User.objects.get(id=id_user)
    if request.method == 'POST':
        user.delete()
        return redirect('userList')
    return render(request, 'almacenes/user_delete.html', {'user': user})


class UserList(ListView):
    model = User
    template_name = 'almacenes/users_list.html'