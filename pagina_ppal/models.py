from django.db import models

# Create your models here.
class reuniones_comunes(models.Model):
    descripcion = models.CharField(max_length=64)
    dia = models.CharField(max_length=64)
    horario = models.CharField(max_length=64)
    lugar = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.descripcion}: {self.dia} {self.horario} ( {self.lugar} )"

class reuniones_especiales(models.Model):
    descripcion = models.CharField(max_length=64)
    dia = models.CharField(max_length=64)
    horario = models.CharField(max_length=64)
    lugar = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.descripcion}: {self.dia} {self.horario} ( {self.lugar} )"