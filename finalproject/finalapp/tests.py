from django.test import TestCase
from .models import TaskType, Task, Comment
from .forms import TaskForm
from datetime import datetime
from django.urls import reverse

# python manage.py test
# Create your tests here.
class TaskTest(TestCase):
  def test_stringOutput(self):
    task=Task(typename='Daily')
    self.assertEqual(str(Task), task.taskname)
  
  def test_tablename(self):
    self.assertEqual(str(Task._meta.db_table), 'task')
    
Class TestIndex(TestCase):
  def test_view_url_accessible_by_name(self):
    response=self.client(reverse('index'))
    self.assertEqual(response.status_code, 200)

  def test_view_users_correct_template(self):
    response=self.client(reverse('index'))
    self.assertTemplateUsed(response, 'finalapp/index.html')

    
    
class New_Task_Form_Test(TestCase):

    # Valid Form Data
    def test_TaskForm_is_valid(self):
        form = TaskForm(data={'taskname': "Check up", 'tasktype': "Monthly", 'user': "John", 'taskentrydate': "2019-03-22", 'taskurl': "google.com", 'eventdescription': "words go here"})
        self.assertTrue(form.is_valid())
    # Invalid Form Data
    def test_UserForm_invalid(self):
        form = TaskForm(data={'taskname': "Check up", 'tasktype': "Monthly", 'user': "John", 'taskentrydate': "2018-03-22", 'taskurl': "google.com", 'eventdescription': "task description goes here"})
        self.assertFalse(form.is_valid())
