from django.contrib.auth import logout, authenticate, login
from django.http import JsonResponse, Http404
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from apps.usuarios.forms import LoginForm, NewUserForm, EventForm
from apps.usuarios.models import Calendario
from apps.utiles.views import ProtectedView


class LoginView(View):
    def get(self, request):
        error_messages = []
        form = LoginForm()
        context = {
            'errors': error_messages,
            'form': form
        }
        return render(request, 'usuarios/login.html', context=context)

    def post(self, request):
        error_messages = []
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(username=email, password=password)
            if user is None:
                error_messages.append('Wrong username or password')
            else:
                if user.is_active:
                    login(request, user)
                    url = request.GET.get('next', 'principal:panel')
                    return redirect(url)
                else:
                    error_messages.append('User is inactive')
        context = {
            'errors': error_messages,
            'form': form
        }
        return render(request, 'usuarios/login.html', context=context)


class LogOutView(ProtectedView):
    def get(self, request):
        logout(request)
        return redirect('home')


class NewUserView(View):
    def get(self, request):
        return render(request, 'usuarios/register.html')


class RegisterNewUser(View):
    def post(self, request):
        status = 200
        respuesta = {}
        form = NewUserForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('email')
            clave = form.cleaned_data.get('password1')
            form.save()
            user = authenticate(username=usuario, password=clave)
            login(request, user)
        else:
            respuesta['errores'] = form.errors
            status = 400
        return JsonResponse(respuesta, status=status)

    def get(self, request):
        raise Http404()