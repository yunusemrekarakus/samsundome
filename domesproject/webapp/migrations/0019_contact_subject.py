# Generated by Django 5.1.2 on 2024-11-07 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0018_contact_is_read'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='subject',
            field=models.CharField(default=1, max_length=200, verbose_name='Konu'),
            preserve_default=False,
        ),
    ]
