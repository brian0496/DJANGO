from django.db import models
from django.utils import timezone 
# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=120, default="")
    usuario = models.CharField(max_length=20, default="")
    mail = models.CharField(max_length=100)
    pasw = models.CharField(max_length=100)
    
    class Meta:
        ordering = ('nombre',)
        
    def __str__(self):
        return self.nombre

class Estado(models.Model):
    ESTADOS = (
        ('A','Alta'),
        ('B','Baja'),
    )
    
    
    #relacion cliente
    cliente = models.ForeignKey('cliente', on_delete=models.CASCADE)
    fechahora = models.DateTimeField(default=timezone.now)
    estado = models.CharField(max_length=8,
           choices=ESTADOS,
           default='A')
    
    class Meta:
        ordering = ('-fechahora',)
        
    def __str__(self):
        return str(self.fechahora) + '-' + str(self.cliente)
    
class Conte(models.Model):
    titulo = models.CharField(max_length=50)
    text = models.CharField(max_length=300)
    user = models.CharField(max_length=100)
    fecha = models.DateField()
    
    def __str__(self):
        return str(self.titulo)+ '-' + str(self.text)