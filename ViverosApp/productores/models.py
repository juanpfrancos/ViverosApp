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


class ProductoControl(models.Model):
    REGISTRO_TIPO_CHOICES = [
        ('hongo', 'Producto Control de Hongo'),
        ('plaga', 'Producto Control de Plaga'),
        ('fertilizante', 'Producto Control de Fertilizante'),
    ]
    registro_ica = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=50)
    frecuencia_aplicacion = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=15, choices=REGISTRO_TIPO_CHOICES)

    def __str__(self):
        return f"{self.nombre} ({self.tipo})"

class ProductoControlHongo(models.Model):
    producto = models.OneToOneField(ProductoControl, on_delete=models.CASCADE)
    periodo_carencia = models.IntegerField()
    hongo_afectado = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.producto.nombre} - Hongo: {self.hongo_afectado}"

class ProductoControlPlaga(models.Model):
    producto = models.OneToOneField(ProductoControl, on_delete=models.CASCADE)
    periodo_carencia = models.IntegerField()

    def __str__(self):
        return f"{self.producto.nombre} - Plaga"

class ProductoControlFertilizante(models.Model):
    producto = models.OneToOneField(ProductoControl, on_delete=models.CASCADE)
    fecha_ultima_aplicacion = models.DateField()

    def __str__(self):
        return f"{self.producto.nombre} - Fertilizante"
