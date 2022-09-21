from django.contrib import admin
from .models import TodoItem, TodoUser
# Register your models here.
admin.site.register(TodoItem)
admin.site.register(TodoUser)