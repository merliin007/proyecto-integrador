from django.contrib import auth
from django.contrib.auth import update_session_auth_hash, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User, Group
from django.contrib.auth.views import LoginView, LogoutView, PasswordContextMixin
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic.base import View

from almacenApp.models import Almacen, Perfil
from almacenApp.forms import UserModelForm, RoleForm, StorageForm, PerfilModelFormEdit, GroupPermissionsForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView, FormView, DetailView
from django.urls import reverse_lazy
import pdb


class SignUpView(CreateView):
    model = Perfil
    form_class = UserModelForm
    template_name = 'profiles/profile_form.html'

    def form_valid(self, form):
        form.save()
        user = form.cleaned_data.get('username')
        pwd = form.cleaned_data.get('password1')
        usuario = authenticate(username=user, password=pwd)
        login(self.request, usuario)
        return redirect('/home/')


class PasswordChange(LoginRequiredMixin, PasswordContextMixin, FormView):
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


class HomeView(View):
    @method_decorator(login_required)
    def get(self, request):
        # context = user.get_all_permissions()
        context = request.user.perfil.groups.name
        # pdb.set_trace()
        return render(request, 'profiles/home.html', dict.fromkeys('perm', context))


class SignInView(LoginView):
    template_name = 'profiles/sign_in.html'


class SignOutView(LogoutView):
    pass


class IndexView(LoginRequiredMixin, TemplateView):
    template_name='almacenes/index.html'


class UserList(LoginRequiredMixin, ListView):
    model = User
    template_name = 'almacenes/users_list.html'


class UserRegister(CreateView):
    model = User
    form_class = UserModelForm
    template_name = 'almacenes/users_form.html'
    success_url = reverse_lazy('usersList')


class UserUpdate(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserModelForm
    template_name = 'almacenes/users_form.html'
    success_url = reverse_lazy('usersList')


class UserDelete(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'almacenes/user_delete.html'
    success_url = reverse_lazy('usersList')


class StorageList(LoginRequiredMixin, ListView):
    model = Almacen
    template_name = 'almacenes/storage_list.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['storage'] = self.model.objects.all()
    #     return context

    def get(self, request, *args, **kwargs):
        group = request.user.perfil.groups.name
        if 'Administrators' in group:
            context = {
                'storage': self.model.objects.all(),
            }
            # pdb.set_trace()
            return render(request, self.template_name, context)
        else:
            return render(request, 'almacenes/403.html')


class RoleCreate(LoginRequiredMixin, CreateView):
    model = Group
    form_class = RoleForm
    template_name = 'almacenes/role_form.html'
    success_url = reverse_lazy('rolesList')


class RoleList(LoginRequiredMixin, ListView):
    model = Group
    template_name = 'almacenes/roles_list.html'


class RoleUpdate(LoginRequiredMixin, UpdateView):
    model = Group
    form_class = RoleForm
    template_name = 'almacenes/role_form.html'
    success_url = reverse_lazy('rolesList')


class StorageCreate(LoginRequiredMixin, CreateView):
    model = Almacen
    form_class = StorageForm
    template_name = 'almacenes/storage_form.html'
    success_url = reverse_lazy('storages')


class StorageEdit(LoginRequiredMixin, UpdateView):
    model = Almacen
    form_class = StorageForm
    template_name = 'almacenes/storage_form.html'
    success_url = reverse_lazy('storages')


class StorageDeletion(LoginRequiredMixin, DeleteView):
    model = Almacen
    template_name = 'almacenes/confirm_deletion.html'
    success_url = reverse_lazy('storages')


class RoleAssignList(LoginRequiredMixin, ListView):
    model = Perfil
    template_name = 'user_role_list.html'


class RoleAssignEdit(LoginRequiredMixin, UpdateView):
    model = Perfil
    form_class = PerfilModelFormEdit
    template_name = 'profiles/user_role_form.html'
    success_url = reverse_lazy('roleAssignList')

    def get_context_data(self, **kwargs):
        context = super(RoleAssignEdit, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        perfil = self.model.objects.get(id=pk)
        if 'form' not in context:
            context['form'] = self.form_class(instance=perfil)
        context['id'] = pk
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_perfil = kwargs['pk']
        perfil = self.model.objects.get(id=id_perfil)
        form = self.form_class(request.POST, instance=perfil)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.success_url)
        else:
            self.render_to_response(self.get_context_data(form=form))

#
# class GroupPermissionsEdit(LoginRequiredMixin, UpdateView):
#     model = GroupPermissions
#     form_class = GroupPermissionsForm
#     template_name = 'almacenes/group_permissions.html'
#     success_url = reverse_lazy('rolesList')
#
#
# class GroupPermissionsCreate(LoginRequiredMixin, CreateView):
#     model = GroupPermissions
#     form_class = GroupPermissionsForm
#     template_name = 'almacenes/group_permissions.html'
#     success_url = reverse_lazy('rolesList')