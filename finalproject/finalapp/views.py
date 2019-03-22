from django.shortcuts import render, get_object_or_404
from .models import TaskType, Task

# Create your views here.
def index(request):
    return render(request, 'finalapp/index.html')

def tasktypes(request):
    type_list=TaskType.objects.all()
    return render(request, 'finalapp/types.html', {'type_list': type_list})

def gettasks(request):
   task_list=Task.objects.all()
   return render(request, ‘finalapp/tasks.html’, {‘task_list’: task_list})

def taskdetail(request, id):
   taskdetail_list=get_object_or_404(Task, pk=id)
   return render(request, ‘techapp/taskdetail.html’, {‘taskdetail_list’: taskdetail_list})

#form view
@login_required
def newevent(request):
    form=TypeForm
    if request.method=='POST':
        form=TypeForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=TypeForm()
    else:
        form=TypeForm()
    return render(request, 'finalapp/newtask.html', {'form': form})

def loginmessage(request):
    return render(request, 'finalapp/loginmessage.html')

def logoutmessage(request):
    return render(request, 'finalapp/logoutmessage.html')
