
from django.urls import path
from offerweb.views import wszystkie_oferty,usun_gatunek, nowa_oferta,add_indeks, gatunek,nowy_gatunek, glowna, kalkulator, dodaj_operacje,add_new_indeks,usun_operacje,indeksy_oferta ,edytuj_top_oferty,edytuj_oferte, operacje, kontrahent, nowy_kontrahent, edytuj_kontrahent, usun_kontrahenta, usun_oferte ,usun_indeks, edytuj_indeks

urlpatterns = [
    path('oferty/', wszystkie_oferty, name="oferty"),
    path('nowa_oferta/', nowa_oferta, name= "nowa_oferta"),
    path('edytuj_top_oferty/<int:id>/', edytuj_top_oferty, name= "edytuj_top_oferty"),
    path('edytuj_oferte/<int:id>/', edytuj_oferte, name= "edytuj_oferte"),
    path('usun_oferte/<int:id>/', usun_oferte, name="usun_oferte"),

    path('kontrahent/', kontrahent, name= "wszyscy_kontrahenci"),
    path('nowy_kontrahent/', nowy_kontrahent, name ="nowy_kontrahent"),
    path('edytuj_kontrahent/<int:id>/', edytuj_kontrahent, name ="edytuj_kontrahenta"),
    #path('edytuj_kontrahent/indeksy/<int:id>/', indeksy_kontrahent, name ="indeksy_kontrahent"), #id kontrahenta
    path('edytuj_oferte/indeksy/<int:id>/', indeksy_oferta, name ="indeksy_oferta"), #id oferty
    path('usun_kontrahent/<int:id>/', usun_kontrahenta, name="usun_kontrahenta"),

    path('usun_indeks/<int:id>/', usun_indeks, name="usun_indeks"),
    path('edytuj_indeks//<int:id>/', edytuj_indeks, name= "edytuj_indeks"),
    path('add_indeks//<int:id>/', add_indeks, name= "add_indeks"),
    path('add_new_indeks/', add_new_indeks, name= "add_new_indeks"),

    path('operacje/', operacje, name="operacje"),
    path('dodaj_operacje/', dodaj_operacje, name ="dodaj_operacje"),
    path('usun_operacje/<int:id>/', usun_operacje, name="usun_operacje"),
    
    path('kalkulator/', kalkulator, name= "kalkulator"),
    path('gatunek', gatunek, name= "gatunek"),
    path('nowy_gatunek', nowy_gatunek, name= "nowy_gatunek"),
    path('usun_gatunek/<int:id>/', usun_gatunek, name="usun_gatunek"),

    path('', glowna),
]
