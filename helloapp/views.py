from django.shortcuts import render

from .models import Data


def index(request):
    info = Data.objects.all()
    a = {
        "data": info
    }
    return render(request, "index.html", a)
