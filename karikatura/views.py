from django.shortcuts import render
from .models import ImageModel


def index(request):
    objects = ImageModel.objects.all()
    return render(request, 'index.html', context={'objs': objects})
