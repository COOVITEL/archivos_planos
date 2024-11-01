from django.shortcuts import render, redirect, HttpResponse
from .forms import *
from .utils import *
from .models import *

def retiroAportesColpensiones(request):
    form = AportesColpensiones()
    if request.method == "POST":
        form = AportesColpensiones(request.POST)
        if form.is_valid():
            afiliacion = form.cleaned_data['afiliacion']
            documento = form.cleaned_data['documento']
            code = codigoRetiroAportesColpensiones(afiliacion, documento)
            registro = RetiroAportesColpensiones(code=code, documento=int(documento), type="Retiro Aportes Colpensiones")
            registro.save()
            return redirect("retiroaportescolpensiones")
    return render(request, 'retiroAportesColpensiones.html', {'form': form})

def ingresoAportesColpensiones(request):
    form = AportesColpensiones()
    if request.method == "POST":
        form = AportesColpensiones(request.POST)
        if form.is_valid():
            afiliacion = form.cleaned_data['afiliacion']
            documento = form.cleaned_data['documento']
            code = codigoIngresoAportesColpensiones(afiliacion, documento)
            registro = IngresoAportesColpensiones(code=code, documento=int(documento), type="Ingreso Aportes Colpensiones")
            registro.save()
            return redirect("ingresoaportescolpensiones")
    return render(request, 'ingresoAportesColpensiones.html', {'form': form})

def retiroCreditoColpensiones(request):
    form = CreditoColpensiones()
    if request.method == "POST":
        form = CreditoColpensiones(request.POST)
        if form.is_valid():
            afiliacion = form.cleaned_data['afiliacion']
            documento = form.cleaned_data['documento']
            pagare = form.cleaned_data['pagare']
    
            code = codigoRetiroCreditoColpensiones(afiliacion, documento, pagare)

            if code == 404:
                error = 'No se encontro registro con ese numero de Cedula y Pagare'
                return render(request, 'ingresoCreditoColpensiones.html', {'form': form, 'error': error})
            
            registro = RetiroCreditoColpensiones(code=code, documento=int(documento), type="Retiro Credito Colpensiones")
            registro.save()
            return redirect("retirocreditocolpensiones")
    return render(request, 'retiroAportesColpensiones.html', {'form': form})

def ingresoCreditoColpensiones(request):
    form = CreditoColpensiones()
    if request.method == "POST":
        form = CreditoColpensiones(request.POST)
        if form.is_valid():
            afiliacion = form.cleaned_data['afiliacion']
            documento = form.cleaned_data['documento']
            pagare = form.cleaned_data['pagare']
    
            code = codigoIngresoCreditoColpensiones(afiliacion, documento, pagare)

            if code == 404:
                error = 'No se encontro registro con ese numero de Cedula y Pagare'
                return render(request, 'ingresoCreditoColpensiones.html', {'form': form, 'error': error})

            registro = IngresoCreditoColpensiones(code=code, documento=int(documento), type="Ingreso Credito Colpensiones")
            registro.save()
            return redirect("ingresocreditocolpensiones")
    return render(request, 'ingresoCreditoColpensiones.html', {'form': form})

def codeFopep(request):
    form = CodeFopep()
    if request.method == 'POST':
        form = CodeFopep(request.POST)
        if form.is_valid():
            typeDoc = form.cleaned_data['typeDoc']
            documento = form.cleaned_data['document']
            aplication = form.cleaned_data['aplication']
            aport = form.cleaned_data['aport']
            libranza = form.cleaned_data['libranza']
            code = codigoFopep(typeDoc, documento, aplication, aport, libranza)
            if code == 404:
                error = 'No se encontro registro con ese numero de Cedula y Pagare'
                return render(request, 'fopep.html', {'form': form, 'error': error})
            registerCode = RegistroFopep(code=code, documento=int(documento), type="Registro Fopep")
            registerCode.save()
            return redirect('fopep')
    return render(request, 'fopep.html', {'form': form})

def descargaFormato(request):
    form = DateForms()
    if request.method == "POST":
        form = DateForms(request.POST)
        if form.is_valid():
            typeCodes = form.cleaned_data['typeCodes']
            dateInit = form.cleaned_data['dateInit']
            dateEnd = form.cleaned_data['dateEnd']
            allDatas = []
            name = ""
            # Verifica cada tipo seleccionado
            if 'retiro_aportes' in typeCodes:
                name = "Retiro Aportes"
                allDatas += RetiroAportesColpensiones.objects.filter(date__range=[dateInit, dateEnd])
            if 'ingreso_aportes' in typeCodes:
                name = "Ingreso Aportes"
                allDatas += IngresoAportesColpensiones.objects.filter(date__range=[dateInit, dateEnd])
            if 'retiro_credito' in typeCodes:
                name = "Retico Credito"
                allDatas += RetiroCreditoColpensiones.objects.filter(date__range=[dateInit, dateEnd])
            if 'ingreso_credito' in typeCodes:
                name = "Ingreso Credito"
                allDatas += IngresoCreditoColpensiones.objects.filter(date__range=[dateInit, dateEnd])
            if 'registro_fopep' in typeCodes:
                name = "Codigos Fopep"
                allDatas += RegistroFopep.objects.filter(date__range=[dateInit, dateEnd])
            if len(allDatas) == 0:
                error = "No se econtraron registros en ese rango de Fechas"
                return render(request, 'download.html', {'form': form, 'error': error})
            contenido = "\n".join([str(data.code) for data in allDatas])
            response = HttpResponse(contenido, content_type="text/plain")
            response['Content-Disposition'] = f'attachment; filename="{name}.txt"'
            return response

    return render(request, 'download.html', {'form': form})
