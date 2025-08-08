from django.db import models

class ObjetivoEspecifico(models.Model):
    id_poa = models.IntegerField()  # FK a POA (no se modela aquí directamente por simplicidad)
    codigo = models.CharField(max_length=20)
    descripcion = models.TextField()
    meta = models.CharField(max_length=200, blank=True, null=True)
    linea_base = models.CharField(max_length=200, blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.codigo} - {self.descripcion[:50]}"
