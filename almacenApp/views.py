from django.contrib import auth
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from almacenApp.models import Role, User, Almacen, UsuarioAdmin
from almacenApp.forms import UsuarioForm, PerfilUserModelForm, UserModelForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy


class SignUpView(CreateView):
    form_class = PerfilUserModelForm
    template_name = 'profiles/profile_form.html'

    def form_valid(self, form):
        user = form['user'].save()
        perfil = form['perfil'].save(commit=False)
        perfil.usuario = user
        perfil.save()

        userAdmin = UsuarioAdmin
        userAdmin.usuario = user
        userAdmin.load()

        return redirect('/home/')


class HomeView(TemplateView):
   template_name = 'profiles/home.html'


class SignInView(LoginView):
    template_name = 'profiles/sign_in.html'


class SignOutView(LogoutView):
    pass


def index(request):
    # return HttpResponse("Index")
    return render(request, "almacenes/index.html", )


def roles_list(request):
    list_roles = Role.objects.all()
    context = {
        'roles_obj': list_roles,
    }
    return render(request, "almacenes/roles_list.html", context)


def user_list(request):
    list_users = User.objects.all()
    context = {
        'user_list': list_users,
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
    return render(request, 'almacenes/users_form.html', {'form': form})


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
    model = auth.models.User
    template_name = 'almacenes/users_list.html'


class UserCreate(CreateView):
    model = auth.models.User
    form_class = UserModelForm
    template_name = 'almacenes/users_form.html'
    success_url = reverse_lazy('usersList')


class UserUpdate(UpdateView):
    model = auth.models.User
    form_class = UserModelForm
    template_name = 'almacenes/users_form.html'
    success_url = reverse_lazy('usersList')


class UserDelete(DeleteView):
    model = User
    template_name = 'almacenes/user_delete.html'
    success_url = reverse_lazy('usersList')


class StorageList(ListView):
    model = Almacen
    template_name = 'almacenes/storage_list.html'

