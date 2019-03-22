from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# one off?, daily, weekly, monthly
class TaskType(models.Model):
    typename=models.CharField(max_length=255)
    typedescription=models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.typename
    
    class Meta:
        db_table='tasktype'

class Task(models.Model):
    taskname=models.CharField(max_length=255)
    tasktype=models.ForeignKey(TaskType, on_delete=models.DO_NOTHING)
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    taskentrydate=models.DateField()
    taskurl=models.URLField(null=True, blank=True)
    taskdescription=models.TextField()

    def __str__(self):
        return self.taskname

    class Meta:
        db_table='task'

class Comment(models.Model):
    commenttitle=models.CharField(max_length=255)
    commentdate=models.DateField()
    task=models.ForeignKey(Task, on_delete=models.DO_NOTHING)
    user=models.ManyToManyField(User)
    commenttext=models.TextField()

    def __str__(self):
        return self.commenttitle

    class Meta:
        db_table='comment'
