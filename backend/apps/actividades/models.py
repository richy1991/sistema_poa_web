from django.db import models
from apps.objetivos.models import ObjetivoEspecifico
from apps.usuarios.models import Usuarios

class EstadosActividad(models.Model):
    id_estado = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(null=True, blank=True)
    color = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.nombre

class ActividadPOA(models.Model):
    id_actividad = models.AutoField(primary_key=True)
    id_objetivo = models.ForeignKey(ObjetivoEspecifico, on_delete=models.CASCADE)
    codigo = models.CharField(max_length=20)
    nombre = models.CharField(max_length=500)
    producto_esperado = models.CharField(max_length=500)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    id_estado = models.ForeignKey(EstadosActividad, on_delete=models.SET_NULL, null=True, blank=True)
    avance_fisico = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    avance_financiero = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    anio = models.IntegerField(null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True, null=True, blank=True)
    creado_por = models.ForeignKey(Usuarios, on_delete=models.SET_NULL, null=True, blank=True, related_name='actividades_creadas')
    modificado_por = models.ForeignKey(Usuarios, on_delete=models.SET_NULL, null=True, blank=True, related_name='actividades_modificadas')
    responsables = models.ManyToManyField(Usuarios, related_name='actividades_responsables')

    def __str__(self):
        return self.nombre

class CronogramaPOA(models.Model):
    id_cronograma = models.AutoField(primary_key=True)
    id_actividad = models.ForeignKey(ActividadPOA, on_delete=models.CASCADE)
    mes = models.IntegerField() # Should add validation for 1-12
    ejecutado = models.BooleanField(default=False)

    def __str__(self):
        return f"Cronograma para {self.id_actividad.nombre} - Mes {self.mes}"
