from django.urls import reverse_lazy
from django.views.generic import FormView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from django.shortcuts import redirect

from .forms import *


class UserRegistrationView(FormView):
    template_name = 'authorization/register.html'
    form_class = CustomRegisterForm
    success_url = reverse_lazy('main_page')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.success_url)


class UserLoginView(LoginView):
    template_name = 'authorization/login.html'
    form_class = CustomLoginForm

    def get_success_url(self):
        return reverse_lazy('main_page')


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('main_page')





