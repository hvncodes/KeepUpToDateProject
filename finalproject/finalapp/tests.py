from django.test import TestCase
from .models import TaskType, Task, Comment
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
