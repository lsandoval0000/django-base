from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import Form, ModelForm

from apps.usuarios.models import User


class LoginForm(Form):
    email = forms.CharField(
        label='Email',
        widget=forms.EmailInput()
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput()
    )


class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'avatar', 'password1', 'password2']

    def save(self):
        user = super(NewUserForm, self).save(commit=False)
        if user.avatar is not None:
            user.avatar = user.avatar.replace('http://', '')
            user.avatar = "https://i.imgur.com/%s" % user.avatar
        user.save()
        return user
