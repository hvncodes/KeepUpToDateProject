from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('tasktypes/', views.tasktypes, name="tasktypes"),
    path(‘gettasks/’, views.gettasks, name=’gettasks’),
    path(‘taskdetail/<int:id>’, views.taskdetail, name=’taskdetail’),
    path('newTask/', views.newTask, name='newtask'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]
