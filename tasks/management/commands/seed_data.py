from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from tasks.models import Project,Task,Comment
class Command(BaseCommand):
    def handle(self,*args,**kwargs):
        user,_=User.objects.get_or_create(username='demo_user',defaults={'email':'demo@example.com'})
        user.set_password('demo-password-123'); user.save()
        project,_=Project.objects.get_or_create(name='Django Course Project',defaults={'description':'Week 3 Task Tracker','owner':user})
        for title,status,priority in [('Set up Django project','DONE','HIGH'),('Build task models','DONE','HIGH'),('Create task API','IN_PROGRESS','HIGH'),('Test CRUD operations','TODO','MEDIUM')]:
            task,_=Task.objects.get_or_create(title=title,project=project,defaults={'description':title,'assigned_to':user,'status':status,'priority':priority})
            if title=='Set up Django project': Comment.objects.get_or_create(task=task,user=user,body='Initial setup completed.')
        self.stdout.write(self.style.SUCCESS('Sample data created.'))
