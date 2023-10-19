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
        fields = ['nazwa','gestosc', ]

class WalekForm(ModelForm):
    class Meta:
        model = Kalkulator
        
        fields=[
        'gatunek',
        'srednica',
        'dlugosc',]
class BlachaForm(ModelForm):
    class Meta:
        model = Kalkulator
        
        fields=[
        'gatunek',
        'szerokosc',
        'grubosc',
        'dlugosc',]

class YourForm(forms.Form):
    
        
        like = forms.ChoiceField(required = True,label='Profil',choices=Kalkulator.typ, widget=forms.RadioSelect(),initial=0)
        #like = forms.ChoiceField(choices=Kalkulator.typ, widget=forms.RadioSelect,initial={'No':'NO'})