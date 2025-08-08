from django.db import models
from apps.usuarios.models import Carrera

class ProgramaPOA(models.Model):
    id_programa = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.nombre

class POA(models.Model):
    ESTADO_CHOICES = [
        ('Borrador', 'Borrador'),
        ('Aprobado', 'Aprobado'),
        ('Ejecutado', 'Ejecutado'),
        ('Archivado', 'Archivado'),
    ]

    id_poa = models.AutoField(primary_key=True)
    id_carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    id_programa = models.ForeignKey(ProgramaPOA, on_delete=models.SET_NULL, null=True, blank=True)
    gestion = models.IntegerField()
    unidad_solicitante = models.CharField(max_length=200)
    objetivo_institucional = models.TextField(max_length=2000)
    estado = models.CharField(max_length=30, choices=ESTADO_CHOICES, default='Borrador')
    fecha_creacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"POA {self.gestion} - {self.id_carrera.nombre}"

class ObjetivoEspecifico(models.Model):
    id_objetivo = models.AutoField(primary_key=True)
    id_poa = models.ForeignKey(POA, on_delete=models.CASCADE)
    codigo = models.CharField(max_length=20)
    descripcion = models.TextField(max_length=1000)
    meta = models.CharField(max_length=200, null=True, blank=True)
    linea_base = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f"{self.codigo} - {self.descripcion[:50]}"
