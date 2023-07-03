from django.forms import ModelForm
from .models import  Kontrahent, Oferty
from address.models import AddressField

        
class OfertaForm(ModelForm):
    class Meta:
        model = Oferty
        fields = ['Uwagi',"kontrahenci","status"]

class KontrahentForm(ModelForm):
    class Meta:
        model = Kontrahent
        fields = ['Nazwa','ulica','miejscowosc','email','tel',]
        ulica = AddressField()