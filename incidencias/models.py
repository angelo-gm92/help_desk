from django.db import models


class Tecnico(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nombre


class Incidencia(models.Model):

    ESTADOS = [
        ("ABIERTO", "Abierto"),
        ("PROCESO", "En Proceso"),
        ("CERRADO", "Cerrado"),
    ]

    PRIORIDADES = [
        ("ALTA", "Alta"),
        ("MEDIA", "Media"),
        ("BAJA", "Baja"),
    ]

    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADOS)
    prioridad = models.CharField(max_length=20, choices=PRIORIDADES)

    tecnico = models.ForeignKey(
        Tecnico, on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return self.titulo
