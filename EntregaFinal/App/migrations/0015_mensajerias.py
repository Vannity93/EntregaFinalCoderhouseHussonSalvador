# Generated by Django 4.0.3 on 2022-04-13 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0014_delete_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mensajerias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remitente', models.CharField(max_length=40)),
                ('destinatario', models.CharField(max_length=40)),
                ('contenido', models.CharField(max_length=500)),
            ],
        ),
    ]
