# Generated by Django 4.2.3 on 2023-09-20 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskpage', '0002_user_date_alter_task_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='asign',
            field=models.ManyToManyField(related_name='assign_to', to='taskpage.user'),
        ),
    ]