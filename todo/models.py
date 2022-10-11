from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver

# Create your models here.
class TodoUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    page_url = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.id} - {self.username} - {self.email}"

class TodoItem(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    is_done = models.BooleanField(default=False)
    priority = models.IntegerField(blank=False, null=False)
    user = models.ForeignKey(TodoUser, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.priority} - {self.title}"
    
    class Meta:
        ordering = ['priority']
