from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class CustomRegisterForm(UserCreationForm):
    username = forms.CharField(required=True,
                               label='Имя пользователя',
                               widget=forms.TextInput(attrs={
                                   'placeholder': '',
                                   'class': 'form-control'
                               }))
    password1 = forms.CharField(required=True,
                                label='Пароль',
                                widget=forms.TextInput(attrs={
                                    'class': 'form-control'
                                }))
    password2 = forms.CharField(required=True,
                                label='Подтвердите пароль',
                                widget=forms.TextInput(attrs={
                                    'class': 'form-control'
                                }))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(required=True,
                               label='Имя пользователья',
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control'
                               }))
    password = forms.CharField(label='Пароль',
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control'
                               }))

