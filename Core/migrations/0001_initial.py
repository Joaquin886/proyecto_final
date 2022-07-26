# Generated by Django 4.0.5 on 2022-07-24 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='super_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_de_usuario', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('contrasenia', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_de_usuario', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('contrasenia', models.CharField(max_length=12)),
            ],
        ),
    ]
