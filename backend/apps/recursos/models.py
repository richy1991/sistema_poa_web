from django.db import models
from apps.actividades.models import ActividadPOA

class TipoIndicador(models.Model):
    id_tipo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(null=True, blank=True)
    formula = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nombre

class PartidasPresupuestarias(models.Model):
    codigo_partida = models.CharField(max_length=10, primary_key=True)
    descripcion = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return f"{self.codigo_partida} - {self.descripcion}"

class Indicadores(models.Model):
    id_indicador = models.AutoField(primary_key=True)
    id_actividad = models.ForeignKey(ActividadPOA, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    tipo_id = models.ForeignKey(TipoIndicador, on_delete=models.SET_NULL, null=True, blank=True)
    formula = models.CharField(max_length=500, null=True, blank=True)
    frecuencia = models.CharField(max_length=50, null=True, blank=True)
    fuente_dato = models.CharField(max_length=200, null=True, blank=True)
    linea_base = models.CharField(max_length=100, null=True, blank=True)
    meta = models.CharField(max_length=100, null=True, blank=True)
    unidad_medida = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.nombre

class ItemsPOA(models.Model):
    id_item = models.AutoField(primary_key=True)
    id_actividad = models.ForeignKey(ActividadPOA, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=300)
    unidad = models.CharField(max_length=50, null=True, blank=True)
    cantidad = models.IntegerField()
    costo_unitario = models.DecimalField(max_digits=18, decimal_places=2)
    subtotal = models.DecimalField(max_digits=18, decimal_places=2, editable=False)
    fuente_financiamiento = models.CharField(max_length=100, null=True, blank=True)
    codigo_partida = models.ForeignKey(PartidasPresupuestarias, on_delete=models.SET_NULL, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.subtotal = self.cantidad * self.costo_unitario
        super().save(*args, **kwargs)

    def __str__(self):
        return self.descripcion

class EjecucionPresupuestaria(models.Model):
    id = models.AutoField(primary_key=True)
    id_item = models.ForeignKey(ItemsPOA, on_delete=models.CASCADE)
    fecha = models.DateField()
    monto_ejecutado = models.DecimalField(max_digits=18, decimal_places=2)
    descripcion = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return f"Ejecución de {self.id_item.descripcion} - {self.fecha}"
