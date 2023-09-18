# Generated by Django 4.2.1 on 2023-09-12 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jacks_website', '0003_remove_project_image_projectimage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='details',
            new_name='summary',
        ),
        migrations.AddField(
            model_name='project',
            name='building_process',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='project',
            name='challenges',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='project',
            name='improvements',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='project',
            name='tools_and_technologies',
            field=models.TextField(default=''),
        ),
    ]
