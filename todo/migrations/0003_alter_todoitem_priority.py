# Generated by Django 4.1.1 on 2022-09-17 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_rename_completed_todoitem_is_done'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='priority',
            field=models.IntegerField(unique=True),
        ),
    ]
