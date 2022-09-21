# Generated by Django 4.1.1 on 2022-09-21 05:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_todoitem_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todoitem',
            name='user_id',
        ),
        migrations.AddField(
            model_name='todoitem',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='todos', to=settings.AUTH_USER_MODEL),
        ),
    ]