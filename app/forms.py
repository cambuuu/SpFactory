from django import forms
from .models import Contacto, Producto

class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = '__all__'

class DateInput(forms.DateInput):
    input_type = 'date'

class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {
            'fecha_producto': DateInput()

        }