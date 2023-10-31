from django.forms import ModelForm, CheckboxInput
from .models import  Kontrahent, Oferty, Indeksy, Operacje, Technologia,Gatunek, Kalkulator

from django import forms
from django.utils.safestring import mark_safe


        
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
        fields = ['operacja','tj', 'tpz']
        

class GatunekForm(ModelForm):
    class Meta:
        model = Gatunek
        fields = ['nazwa', 'gestosc']

class WalekForm(ModelForm):
    class Meta:
        model = Kalkulator
        
        fields=[
        'gatunek',
        'srednica',
        'dlugosc',
        'waga',
        'wartosc',]
class BlachaForm(ModelForm):
    class Meta:
        model = Kalkulator
        
        fields=[
        'gatunek',
        'szerokosc',
        'grubosc',
        'dlugosc',
        'waga',
        'wartosc',]


class Fgatunek(forms.Form):
    fields = 'nazwa'
    #lista = forms.ModelChoiceField(queryset=Gatunek.objects.values_list(fields).distinct(),
    #empty_label=None)
    lista = forms.ModelChoiceField(queryset=Gatunek.objects.values_list("nazwa", flat=True),empty_label='--------', label='')

