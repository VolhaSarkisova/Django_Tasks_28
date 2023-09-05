from django.contrib import admin

from comments.models import Comments

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('task', 'user', 'text', 'date_creation', 'parent')
    search_fields = ('task', )
    list_filter = ('task',)
