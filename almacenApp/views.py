from django.contrib import auth
from django.contrib.auth import update_session_auth_hash, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import LoginView, LogoutView, PasswordContextMixin
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters

from almacenApp.models import Role, User, Almacen, Perfil
from almacenApp.forms import UsuarioForm, PerfilUserModelForm, UserModelForm, RoleForm, StorageForm, PerfilForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView, FormView
from django.urls import reverse_lazy


class SignUpView(CreateView):
    form_class = PerfilUserModelForm
    template_name = 'profiles/profile_form.html'

    def form_valid(self, form):
        user = form['user'].save()
        perfil = form['perfil'].save(commit=False)
        perfil.usuario = user
        perfil.save()
        return redirect('/home/')


class PasswordChange(PasswordContextMixin, FormView):
    form_class = PasswordChangeForm
    # success_url = reverse_lazy('password_change_done')
    success_url = reverse_lazy('index')
    template_name = 'profiles/password_change.html'
    title = 'Password change'

    @method_decorator(sensitive_post_parameters())
    @method_decorator(csrf_protect)
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        # Updating the password logs out all other sessions for the user
        # except the current one.
        update_session_auth_hash(self.request, form.user)
        return super().form_valid(form)


class HomeView(TemplateView):
   template_name = 'profiles/home.html'


class SignInView(LoginView):
    template_name = 'profiles/sign_in.html'


class SignOutView(LogoutView):
    pass


def index(request):
    # return HttpResponse("Index")
    return render(request, "almacenes/index.html", )





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


class UserRegister(CreateView):
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


class RoleCreate(CreateView):
    model = Role
    form_class = RoleForm
    template_name = 'almacenes/role_form.html'
    success_url = reverse_lazy('rolesList')


class RoleList(ListView):
    model = Role
    template_name = 'almacenes/roles_list.html'


class RoleUpdate(UpdateView):
    model = Role
    form_class = RoleForm
    template_name = 'almacenes/role_form.html'
    success_url = reverse_lazy('rolesList')


class StorageCreate(CreateView):
    model = Almacen
    form_class = StorageForm
    template_name = 'almacenes/storage_form.html'
    success_url = reverse_lazy('storages')


class StorageEdit(UpdateView):
    model = Almacen
    form_class = StorageForm
    template_name = 'almacenes/storage_form.html'
    success_url = reverse_lazy('storages')


class StorageDeletion(DeleteView):
    model = Almacen
    template_name = 'almacenes/confirm_deletion.html'
    success_url = reverse_lazy('storages')
