from dataclasses import fields
from django import forms
from django.forms import ModelForm, ValidationError, widgets
from .models import *

# importar para poder crear el usuario en la base de datos de Django
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import widgets


class LoginForm(forms.Form):
    username = forms.EmailField(
        label='Correo Electrónico', 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su Correo'}))
    
    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su contraseña'}))



class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su Correo'}),
    )
    first_name = forms.CharField(
        max_length=80,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su Nombre'}),
    )
    last_name = forms.CharField(
        max_length=80,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su Apellidos'}),
    )
    password1 = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su contraseña'}))
    password2 = forms.CharField(
        label='Confirmar Contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirme su contraseña'}))

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data["email"]
        user.email = self.cleaned_data["email"]  # Set email to be the same as username
        if commit:
            user.save()
        return user
