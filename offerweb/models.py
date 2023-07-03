from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from address.models import AddressField



class Kontrahent(models.Model):
    Nazwa= models.CharField(max_length=32, unique=True, null = False)
    miejscowosc = models.CharField(max_length=32, blank=True)
    ulica = AddressField(on_delete=models.CASCADE, blank=True,null = True)
    email = models.EmailField(null=False)
    tel = PhoneNumberField(blank=True, default = "+48 ")
    
    

    def __str__(self):
        return self.Nazwa + ' (' + self.email+')'
    

class Oferty(models.Model):

    Uwagi = models.TextField(default='')
    kontrahenci=models.ForeignKey(Kontrahent,on_delete=models.CASCADE)
    nr_zew = models.CharField(max_length=32)
    data = models.DateField(auto_now_add = True)
    
class Indeksy(models.Model):
    mat={
        (0, "Tak"),
        (1, "Nie")
    }
    indeks= models.CharField(max_length=32)
    ilosc = models.IntegerField()
    Oferta=models.ForeignKey(Oferty,on_delete=models.CASCADE)
    czy_mat = models.PositiveBigIntegerField(default=1, choices=mat)

class Operacje(models.Model):
    typ = {
        (0, "Zwykła"),
        (1, "Kooperacja")
    }
    operacja = models.CharField(max_length=32)
    stawka=  models.CharField(max_length=32)
    typ_operacji = models.PositiveBigIntegerField(default=0, choices=typ)

class Technologia(models.Model):
    operacja=models.ForeignKey(Operacje,on_delete=models.CASCADE)

'''
class DodatkoweInfo(models.Model):

    GATUNEK={
        (0, "Inne"),
        (1, "Horror"),
        (2, "Komedia"),
        (3, "Sci-fi"),
        (4, "Drama"),
        (5, "Romans"),
    }    
    czas_trwania = models.PositiveBigIntegerField(default=0)
    gatunek = models.PositiveBigIntegerField(default=0, choices=GATUNEK)


# Create your models here.
class Film(models.Model):
    tytul = models.CharField(max_length=64, blank=False, unique=True) #przechowywanie danych tekstowych, blank - czy może być pusty(false, nie może być pusty)
    rok = models.PositiveSmallIntegerField(default=2000)
    opis = models.TextField(default='')
    premiera = models.DateField(null=True, blank=True)
    imdb_rating = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    plakat = models.ImageField(upload_to='plakaty', null=True, blank=True)
    dodatkowe = models.OneToOneField(DodatkoweInfo, on_delete=models.CASCADE,null=True, blank=True) 
    def __str__(self):
        #return self.tytul + ' ('+str(self.rok)+')'
        return self.tytul_z_rokiem()
    
    def tytul_z_rokiem(self):
        return '{} ({})'.format(self.tytul, self.rok)


class Ocena(models.Model):
    recenzja = models.TextField(default="",blank=True)
    gwiazdki = models.PositiveSmallIntegerField(default=5)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)

class Aktor(models.Model):
    imie= models.CharField(max_length=32)
    nazwisko = models.CharField(max_length=32)
    filmy= models.ManyToManyField(Film, related_name="aktorzy")
'''