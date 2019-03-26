from django.shortcuts import render
from django.views import View

from apps.utiles.views import ProtectedView


# Create your views here.


class Home(View):
    def get(self, request):
        return render(request, 'principal/index.html')