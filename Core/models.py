from django.db import models

# Create your models here.

class super_user(models.Model):

    nombre_de_usuario = models.CharField(max_length=10)
    
    email = models.EmailField()

    contrasenia = models.CharField(max_length=12)

class usuario(models.Model):

    nombre_de_usuario = models.CharField(max_length=10)

    email = models.EmailField()

    contrasenia = models.CharField(max_length=12)

class post_usuario(models.Model):

    titulo = models.CharField(max_length=10)

    cuerpo = models.CharField(max_length=100)

    fecha = models.DateTimeField()

class post_super_user(models.Model):

    titulo = models.CharField(max_length=10)

    cuerpo = models.CharField(max_length=100)

    fecha = models.DateTimeField()




