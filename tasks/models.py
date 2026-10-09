from django.contrib.auth.models import User
from django.db import models
class Project(models.Model):
    name=models.CharField(max_length=150); description=models.TextField(blank=True)
    owner=models.ForeignKey(User,on_delete=models.CASCADE,related_name='owned_projects'); created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self): return self.name
class Task(models.Model):
    class Status(models.TextChoices): TODO='TODO','To Do'; IN_PROGRESS='IN_PROGRESS','In Progress'; DONE='DONE','Done'
    class Priority(models.TextChoices): LOW='LOW','Low'; MEDIUM='MEDIUM','Medium'; HIGH='HIGH','High'
    title=models.CharField(max_length=200); description=models.TextField(blank=True)
    project=models.ForeignKey(Project,on_delete=models.CASCADE,related_name='tasks')
    assigned_to=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True,related_name='assigned_tasks')
    status=models.CharField(max_length=20,choices=Status.choices,default=Status.TODO)
    priority=models.CharField(max_length=10,choices=Priority.choices,default=Priority.MEDIUM)
    due_date=models.DateField(null=True,blank=True); created_at=models.DateTimeField(auto_now_add=True); updated_at=models.DateTimeField(auto_now=True)
    def __str__(self): return self.title
class Comment(models.Model):
    task=models.ForeignKey(Task,on_delete=models.CASCADE,related_name='comments'); user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='task_comments'); body=models.TextField(); created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self): return f'Comment by {self.user.username} on {self.task.title}'
