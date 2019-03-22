from django.shortcuts import render
from .models import TaskType

# Create your views here.
def index(request):
    return render(request, 'finalapp/index.html')

def tasktypes(request):
    type_list=TaskType.objects.all()
    return render(request, 'finalapp/types.html', {'type_list': type_list})



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
