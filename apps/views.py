from django.shortcuts import render

from apps.models import Sheep


# Create your views here.

def index_view(request):
    contex = {
        'sheep': Sheep.objects.all()
    }
    return render(request, 'apps/index.html', contex)
