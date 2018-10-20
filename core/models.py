from django.db import models

# Create your models here.

class Usuario (models.Model):
    
    login =models.CharField(max_length=20)
    senha =models.CharField(max_length=30)
    email =models.CharField(max_length=30)
    celular =models.CharField(max_length=17)
    def __str__(self):
        return f'{self.login} -- {self.senha}----- {self.email}----- {self.celular}---'

class Curso(models.Model):
     nome=models.CharField(max_length=20)
   