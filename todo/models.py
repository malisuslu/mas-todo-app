from django.db import models

# Create your models here.
class TodoItem(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    is_done = models.BooleanField(default=False)
    priority = models.IntegerField(unique=True, blank=False, null=False)

    def __str__(self):
        return f"{self.priority} - {self.title}"
    
    class Meta:
        ordering = ['priority']
