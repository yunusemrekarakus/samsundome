# Generated by Django 5.1.2 on 2024-11-10 17:54

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0023_mymodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymodel',
            name='content',
            field=tinymce.models.HTMLField(),
        ),
    ]