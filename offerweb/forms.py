from django.forms import ModelForm
from .models import  Kontrahent, Oferty, Indeksy
from address.models import AddressField

        
class OfertaForm(ModelForm):
    class Meta:
        model = Oferty
        fields = ['nr_zew','Uwagi',"kontrahenci","status"]

class KontrahentForm(ModelForm):
    class Meta:
        model = Kontrahent
        fields = ['Nazwa','ulica','miejscowosc','email','tel',]
        ulica = AddressField()

class IndeksForm(ModelForm):
    class Meta:
        model = Indeksy
        fields = ['indeks','ilosc','czy_mat']
