from django.db import models

class Robot(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Sensor(models.Model):
    robot = models.ForeignKey(Robot, on_delete=models.CASCADE, related_name='sensores')
    tipo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.tipo} de {self.robot.nombre}"

class Tarea(models.Model):
    robot = models.ForeignKey(Robot, on_delete=models.CASCADE, related_name='tareas')
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} ({self.robot.nombre})"
