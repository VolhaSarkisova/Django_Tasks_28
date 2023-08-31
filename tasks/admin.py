from django.contrib import admin
from tasks.models import Tasks

@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'users', 'status', 'date_completion', 'date_completion')
    search_fields = ('name', )
    list_filter = ('date_completion',)

# Register your models here.
