from django import forms

class AportesColpensiones(forms.Form):
    afiliacion = forms.IntegerField()
    documento = forms.IntegerField()

class CreditoColpensiones(AportesColpensiones):
    pagare = forms.IntegerField()


class DateForms(forms.Form):
    CHOISES_TYPES = [
        ('retiro_aportes', 'Retiro Aportes Colpensiones'),
        ('ingreso_aportes', 'Ingreso Aportes Colpensiones'),
        ('retiro_credito', 'Retiro Credito Colpensiones'),
        ('ingreso_credito', 'Ingreso Credito Colpensiones'),
        ('registro_fopep', 'Registro Fopep'),
    ]

    typeCodes = forms.ChoiceField(choices=CHOISES_TYPES, label='Seleccione los codigos a descargar')
    dateInit = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    dateEnd = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))


class CodeFopep(forms.Form):
    CHOISES_DOC = [
        ('CC', 'CC'),
        ('CE', 'CE'),
    ]
    CHOISES_APLACATION = [
        ('0', 'Ingreso'),
        ('1', 'Retiro'),
        ('3', 'Mesadas Adicionales'),
    ]
    CHOISES_APORTE = [
        ('0', 'ASOCIACIÓN'),
        ('1', 'PRÉSTAMO'),
    ]
    typeDoc = forms.ChoiceField(choices=CHOISES_DOC, label="Seleccione Tipo Documento")
    document = forms.IntegerField()
    aplication = forms.ChoiceField(choices=CHOISES_APLACATION, label="Seleccione Tipo Aplicación")
    aport = forms.ChoiceField(choices=CHOISES_APORTE, label="Seleccione Aporte/Prestamo")
    libranza = forms.IntegerField()
    