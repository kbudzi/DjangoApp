from django.forms import ModelForm
from .models import  Kontrahent, Oferty

        
class OfertaForm(ModelForm):
    class Meta:
        model = Oferty
        fields = ['Uwagi',"kontrahenci"]

class KontrahentForm(ModelForm):
    class Meta:
        model = Kontrahent
        fields = ['Nazwa','email']