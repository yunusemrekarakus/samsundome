# Generated by Django 5.1.2 on 2024-11-06 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0013_remove_videogallery_cover_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ekip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=100)),
                ('resim', models.ImageField(upload_to='team_images/')),
                ('vasif', models.CharField(max_length=100)),
                ('instagram_url', models.URLField(blank=True, null=True)),
            ],
        ),
    ]