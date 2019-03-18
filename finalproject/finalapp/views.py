from django.shortcuts import render
from .models import EventType

# Create your views here.
def index(request):
    return render(request, 'finalapp/index.html')

def eventtypes(request):
    type_list=EventType.objects.all()
    return render(request, 'finalapp/types.html', {'type_list': type_list})
