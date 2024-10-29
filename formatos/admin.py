from django.contrib import admin
from .models import *


@admin.register(IngresoAportesColpensiones)
class IngresoAportesColpensionesAdmin(admin.ModelAdmin):
    list_display = ["date", "documento", "type", "code"]

@admin.register(RetiroAportesColpensiones)
class RetiroAportesColpensionesAdmin(admin.ModelAdmin):
    list_display = ["date", "documento", "type", "code"]

@admin.register(IngresoCreditoColpensiones)
class IngresoCreditoColpensionesAdmin(admin.ModelAdmin):
    list_display = ["date", "documento", "type", "code"]

@admin.register(RetiroCreditoColpensiones)
class RetiroCreditoColpensionesAdmin(admin.ModelAdmin):
    list_display = ["date", "documento", "type", "code"]

@admin.register(RegistroFopep)
class RegistroAdmin(admin.ModelAdmin):
    list_display = ["date", "documento", "type", "code"]
