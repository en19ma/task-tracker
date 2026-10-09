from django.contrib import admin
from .models import Project, Task, Comment
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display=('name','owner','created_at'); search_fields=('name','description')
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display=('title','project','assigned_to','status','priority','due_date'); search_fields=('title',); list_filter=('project','status','priority')
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=('task','user','created_at'); search_fields=('body','task__title','user__username')
