from django.contrib import admin
from .models import TaskType, Task, Comment

# Register your models here.
admin.site.register(TaskType)
admin.site.register(Task)
admin.site.register(Comment)
