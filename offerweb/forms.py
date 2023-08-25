from django.forms import ModelForm
from .models import  Kontrahent, Oferty, Indeksy, Operacje, Technologia
from address.models import AddressField
from django import forms


        
class OfertaForm(ModelForm):
    class Meta:
        model = Oferty
        fields = ['nr_zew','Uwagi',"kontrahenci","status"]
        widgets = {
          'Uwagi': forms.Textarea(attrs={'rows':2, 'cols':15}),
        }

class KontrahentForm(ModelForm):
    class Meta:
        model = Kontrahent
        fields = ['Nazwa','ulica','miejscowosc','email','tel',]
        ulica = AddressField()

class IndeksForm(ModelForm):
    class Meta:
        model = Indeksy
        fields = ['indeks','ilosc','czy_mat']

class OperacjeForm(ModelForm):
    class Meta:
        model = Operacje
        fields = ['operacja','stawka','typ_operacji']
class TechnologiaForm(ModelForm):
    class Meta:
        model = Technologia
        fields = ['indeks','operacja','tj', 'tpz']
      