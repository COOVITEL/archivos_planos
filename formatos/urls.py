from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('retiroAportes/', retiroAportesColpensiones, name="retiroaportescolpensiones"),
    path('ingresoAportes/', ingresoAportesColpensiones, name="ingresoaportescolpensiones"),
    path('retiroCredito/', retiroCreditoColpensiones, name="retirocreditocolpensiones"),
    path('ingresoCredito/', ingresoCreditoColpensiones, name="ingresocreditocolpensiones"),
    path('descarga/', descargaFormato, name="descarga")
]
