# Generated by Django 5.1.2 on 2024-10-17 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_otelmemnuniyet_cihaz_bilgisi_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='otelmemnuniyet',
            old_name='onayli',
            new_name='yayinla',
        ),
    ]