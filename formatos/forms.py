from django import forms

class AportesColpensiones(forms.Form):
    afiliacion = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Numero de Afiliación'}))
    documento = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Numero de Documento'}))

class CreditoColpensiones(AportesColpensiones):
    pagare = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Numero de Pagare'}))


class DateForms(forms.Form):
    CHOISES_TYPES = [
        ('', '-- Seleccione los Codigos a Descargar --'),
        ('retiro_aportes', 'Retiro Aportes Colpensiones'),
        ('ingreso_aportes', 'Ingreso Aportes Colpensiones'),
        ('retiro_credito', 'Retiro Credito Colpensiones'),
        ('ingreso_credito', 'Ingreso Credito Colpensiones'),
        ('registro_fopep', 'Registro Fopep'),
    ]

    typeCodes = forms.ChoiceField(choices=CHOISES_TYPES, label='Seleccione los codigos a descargar')
    dateInit = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}), label="Fecha de Inicio")
    dateEnd = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}), label="Fecha Final")


class CodeFopep(forms.Form):
    CHOISES_DOC = [
        ('', '-- Seleccione Tipo Documneto -'),
        ('CC', 'CC'),
        ('CE', 'CE'),
    ]
    CHOISES_APLACATION = [
        ('', '-- Seleccione Tipo de Aplicación --'),
        ('0', 'Ingreso'),
        ('1', 'Retiro'),
        ('3', 'Mesadas Adicionales'),
    ]
    CHOISES_APORTE = [
        ('', '-- Seleccione Tipo de Aporte'),
        ('0', 'ASOCIACIÓN'),
        ('1', 'PRÉSTAMO'),
    ]
    typeDoc = forms.ChoiceField(choices=CHOISES_DOC, label="Seleccione Tipo Documento")
    document = forms.IntegerField(label="Documento", widget=forms.NumberInput(attrs={'placeholder': 'Numero de documento'}))
    aplication = forms.ChoiceField(choices=CHOISES_APLACATION, label="Seleccione Tipo Aplicación")
    aport = forms.ChoiceField(choices=CHOISES_APORTE, label="Seleccione Aporte/Prestamo")
    libranza = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Numero de Libranza'}))
    