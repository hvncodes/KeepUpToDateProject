from django.shortcuts import render
from .models import TaskType

# Create your views here.
def index(request):
    return render(request, 'finalapp/index.html')

def tasktypes(request):
    type_list=TaskType.objects.all()
    return render(request, 'finalapp/types.html', {'type_list': type_list})
