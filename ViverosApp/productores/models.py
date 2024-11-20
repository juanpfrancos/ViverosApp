# productores/models.py
from django.db import models

class Productor(models.Model):
    documento_identidad = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.documento_identidad})"


class Finca(models.Model):
    numero_catastro = models.CharField(max_length=20, unique=True)
    municipio = models.CharField(max_length=50)
    productor = models.ForeignKey(Productor, related_name='fincas', on_delete=models.CASCADE)

    def __str__(self):
        return f"Finca {self.numero_catastro} - {self.municipio}"


class Vivero(models.Model):
    codigo = models.CharField(max_length=20)
    tipo_cultivo = models.CharField(max_length=50)
    finca = models.ForeignKey(Finca, related_name='viveros', on_delete=models.CASCADE)

    def __str__(self):
        return f"Vivero {self.codigo} - {self.tipo_cultivo}"


class Labor(models.Model):
    fecha = models.DateField()
    descripcion = models.TextField()
    vivero = models.ForeignKey(Vivero, related_name='labores', on_delete=models.CASCADE)

    def __str__(self):
        return f"Labor en {self.vivero.codigo} - {self.fecha}: {self.descripcion[:30]}"
