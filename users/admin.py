from django.contrib import admin
from users.models import Users

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('login', 'mail', 'password')
    search_fields = ('login', )
    list_filter = ('login',)
# Register your models here.
