from django.db import models

class Usuarios(models.Model):
    ROL_CHOICES = [
        ('Administrador', 'Administrador'),
        ('Docente', 'Docente'),
        ('Estudiante', 'Estudiante'),
        ('Administrativo', 'Administrativo'),
    ]

    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(max_length=100, unique=True)
    contrasena = models.CharField(max_length=255)
    rol = models.CharField(max_length=20, choices=ROL_CHOICES)
    estado = models.BooleanField(default=True)
    ultimo_login = models.DateTimeField(null=True, blank=True)
    intentos_fallidos = models.IntegerField(default=0)
    bloqueado = models.BooleanField(default=False)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True, null=True, blank=True)
    creado_por = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='usuarios_creados')
    modificado_por = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='usuarios_modificados')

    def __str__(self):
        return self.nombre

class Carrera(models.Model):
    id_carrera = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200, unique=True)
    descripcion = models.CharField(max_length=500, null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True, null=True, blank=True)
    creado_por = models.ForeignKey(Usuarios, on_delete=models.SET_NULL, null=True, blank=True, related_name='carreras_creadas')
    modificado_por = models.ForeignKey(Usuarios, on_delete=models.SET_NULL, null=True, blank=True, related_name='carreras_modificadas')

    def __str__(self):
        return self.nombre

class Departamentos(models.Model):
    id_departamento = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nombre
