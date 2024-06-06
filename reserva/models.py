from django.db import models
from cliente.models import Cliente

# Create your models here.

class Reserva(models.Model):
    id_cliente = models.IntegerField(null=False)
    mesa = models.IntegerField(default=0)
    data = models.DateField(null=True)

    def __str__(self):
        return f"Cliente: {self.id_cliente}, Mesa:{self.mesa}"
    
    def to_dict(self):
        return {
            'mesa': self.mesa,
            'data': self.data.strftime('%Y-%m-%d'),
        }