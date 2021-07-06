# Create your views here.
from django.shortcuts import render
from .models import Videos


def index(request):
    info = Videos.objects.all
    a = {
        "Videos": info
    }
    return render(request, "indexe.html", a)
