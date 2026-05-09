from django.db import models


class Doctor(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} - {self.especialidad}"


class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.PositiveIntegerField()
    diagnostico = models.CharField(max_length=200)
    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        related_name='pacientes'
    )

    def __str__(self):
        return self.nombre