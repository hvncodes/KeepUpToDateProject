from django.test import TestCase
from .models import TaskType, Task, Comment
from .forms import TaskForm
from datetime import datetime
from django.urls import reverse

# python manage.py test
#models
class TaskTypeTest(TestCase):
  def test_stringOutput(self):
    tasktype=TaskType(typename='Daily')
    self.assertEqual(str(TaskType), tasktype.typename)
  
  def test_tablename(self):
    self.assertEqual(str(TaskType._meta.db_table), 'tasktype')

class TaskTest(TestCase):
  def test_stringOutput(self):
    task=Task(taskname='Lunch')
    self.assertEqual(str(Task), task.taskname)
  
  def test_tablename(self):
    self.assertEqual(str(Task._meta.db_table), 'task')
    
class CommentTest(TestCase):
    def test_stringOutput(self):
        comment=Comment(commenttitle='Bring a drink')
        self.assertEqual(str(comment), comment.commenttitle)

    def test_tablename(self):
        self.assertEqual(str(Comment._meta.db_table), 'comment')

#views
class TestIndex(TestCase):
  def test_view_url_accessible_by_name(self):
    response=self.client(reverse('index'))
    self.assertEqual(response.status_code, 200)

  def test_view_users_correct_template(self):
    response=self.client(reverse('index'))
    self.assertTemplateUsed(response, 'finalapp/index.html')

class TestTaskTypes(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/finalapp/types')
        self.assertEqual(response.status_code, 200)
  
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('taskdetail'))
        self.assertEqual(response.status_code, 200)
    
    def test_view_uses_correct_template(self):
        response=self.client.get(reverse('types'))
        self.assertTemplateUsed(response, 'finalapp/types.html')  
    
class TestGetTask(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/finalapp/tasks')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('gettasks'))
        self.assertEqual(response.status_code, 200)
        
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('gettasks'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'finalapp/tasks.html')

class TestTaskDetails(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/finalapp/taskdetail')
        self.assertEqual(response.status_code, 200)
  
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('taskdetail'))
        self.assertEqual(response.status_code, 200)
    
    def test_view_uses_correct_template(self):
        response=self.client.get(reverse('taskdetail'))
        self.assertTemplateUsed(response, 'finalapp/taskdetail.html')        
        
class TestLoginMessage(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/finalapp/loginmessage')
        self.assertEqual(response.status_code, 200)
  
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('loginmessage'))
        self.assertEqual(response.status_code, 200)
    
    def test_view_uses_correct_template(self):
        response=self.client.get(reverse('loginmessage'))
        self.assertTemplateUsed(response, 'finalapp/loginmessage.html')
    
class TestLogOutMessage(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/finalapp/logoutmessage')
        self.assertEqual(response.status_code, 200)
  
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('logoutmessage'))
        self.assertEqual(response.status_code, 200)
    
    def test_view_uses_correct_template(self):
        response=self.client.get(reverse('logoutmessage'))
        self.assertTemplateUsed(response, 'finalapp/logoutmessage.html')
    
class TestLogin(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/registration/login')
        self.assertEqual(response.status_code, 200)
  
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
    
    def test_view_uses_correct_template(self):
        response=self.client.get(reverse('login'))
        self.assertTemplateUsed(response, 'registration/login.html')
        
#forms
class New_Task_Form_Test(TestCase):

    # Valid Form Data
    def test_TaskForm_is_valid(self):
        form = TaskForm(data={'taskname': "Check up", 'tasktype': "Monthly", 'user': "John", 'taskentrydate': "2019-03-22", 'taskurl': "google.com", 'eventdescription': "words go here"})
        self.assertTrue(form.is_valid())
    # Invalid Form Data
    def test_UserForm_invalid(self):
        form = TaskForm(data={'taskname': "Check up", 'tasktype': "Monthly", 'user': "John", 'taskentrydate': "2018-03-22", 'taskurl': "google.com", 'eventdescription': "task description goes here"})
        self.assertFalse(form.is_valid())
