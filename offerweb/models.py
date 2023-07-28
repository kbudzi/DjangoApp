from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from address.models import AddressField
from django.urls import reverse



class Kontrahent(models.Model):
    Nazwa= models.CharField(max_length=32, unique=True, null = False)
    miejscowosc = models.CharField(max_length=32, blank=True)
    ulica = AddressField(on_delete=models.CASCADE, blank=True,null = True)
    email = models.EmailField(null=False)
    tel = PhoneNumberField(blank=True, default = "+48 ")
    
    def __str__(self):
        return self.Nazwa + ' (' + self.email+')'
    

class Oferty(models.Model):
    stat={
        (0, "nowa"),
        (1, "w trakcie"),
        (2, "opracowana"),
        (3, "wysłana"),
    }
    
    Uwagi = models.TextField(default='')
    kontrahenci=models.ForeignKey(Kontrahent,on_delete=models.CASCADE)
    nr_zew = models.CharField(max_length=32)
    data = models.DateField(auto_now_add = True)
    status= models.PositiveBigIntegerField(default=0, choices=stat, blank=False,)
    def __str__(self):
        return self.numer_oferty()
    def numer_oferty(self):
            return "{} ({})".format(self.data, self.nr_zew)

 
class Indeksy(models.Model):
    mat={
        (0, "Tak"),
        (1, "Nie")
    }
    indeks= models.CharField(max_length=32,null=True)
    ilosc = models.IntegerField(null=True, blank=True)
    
    czy_mat = models.PositiveBigIntegerField(default=1, choices=mat)
    oferta=models.ForeignKey(Oferty,on_delete=models.CASCADE)
class Operacje(models.Model):
    typ = {
        (0, "Zwykła"),
        (1, "Kooperacja")
    }
    operacja = models.CharField(max_length=32)
    stawka=  models.CharField(max_length=32)
    typ_operacji = models.PositiveBigIntegerField(default=0, choices=typ)

class Technologia(models.Model):
    operacja=models.ManyToManyField(Operacje, related_name='technologie')