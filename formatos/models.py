from django.db import models

class Registro(models.Model):
    date = models.DateField(auto_now_add=True)
    documento = models.IntegerField()
    type = models.CharField(max_length=100)

class IngresoAportesColpensiones(Registro):
    code = models.CharField(max_length=53)
    
class RetiroAportesColpensiones(Registro):
    code = models.CharField(max_length=34)

class IngresoCreditoColpensiones(Registro):
    code = models.CharField(max_length=84)

class RetiroCreditoColpensiones(Registro):
    code = models.CharField(max_length=44)

class RegistroFopep(Registro):
    code = models.CharField(max_length=173)