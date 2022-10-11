from django.contrib import admin
from .models import TodoItem, TodoUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.
@admin.register(TodoUser)
class TodoUserAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ('page_url', 'avatar')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('page_url', 'avatar')}),
    )

admin.site.register(TodoItem)
admin.site.unregister(TodoUser)
admin.site.register(TodoUser, TodoUserAdmin)