# Generated by Django 4.0.3 on 2022-04-15 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0024_remove_blog_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='avatars'),
        ),
    ]
