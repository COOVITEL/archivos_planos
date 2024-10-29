from django import forms

class AportesColpensiones(forms.Form):
    afiliacion = forms.IntegerField()
    documento = forms.IntegerField()

class CreditoColpensiones(AportesColpensiones):
    pagare = forms.IntegerField()

from django import forms

CHOISES_TYPES = (
    ('retiro_aportes', 'Retiro Aportes Colpensiones'),
    ('ingreso_aportes', 'Ingreso Aportes Colpensiones'),
    ('retiro_credito', 'Retiro Credito Colpensiones'),
    ('ingreso_credito', 'Ingreso Credito Colpensiones'),
)

class DateForms(forms.Form):
    typeCodes = forms.MultipleChoiceField(
        choices=CHOISES_TYPES,
        widget=forms.SelectMultiple(attrs={'class': 'form-control'})  # Opcional: agrega clases CSS si lo deseas
    )
    dateInit = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    dateEnd = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
