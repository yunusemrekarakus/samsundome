# Generated by Django 5.1.2 on 2024-11-10 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0025_hakkimizda_delete_mymodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='hakkimizda',
            name='musteri_say',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
