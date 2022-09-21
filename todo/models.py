from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    page_url = models.URLField(max_length=200, blank=True, null=True)

class TodoItem(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    is_done = models.BooleanField(default=False)
    priority = models.IntegerField(blank=False, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todos', blank=True, null=True)

    def __str__(self):
        return f"{self.priority} - {self.title}"
    
    class Meta:
        ordering = ['priority']


