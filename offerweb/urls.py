
from django.urls import path
from offerweb.views import wszystkie_oferty,nowa_oferta, glowna,edytuj_top_oferty,edytuj_oferte, kontrahent, nowy_kontrahent, edytuj_kontrahent, usun_kontrahenta, usun_oferte ,usun_indeks, edytuj_indeks

urlpatterns = [
    path('oferty/', wszystkie_oferty, name="oferty"),
    path('nowa_oferta/', nowa_oferta, name= "nowa_oferta"),
    path('edytuj_top_oferty//<int:id>/', edytuj_top_oferty, name= "edytuj_top_oferty"),
    path('edytuj_oferte//<int:id>/', edytuj_oferte, name= "edytuj_oferte"),
    path('usun_oferte/<int:id>/', usun_oferte, name="usun_oferte"),
    path('kontrahent/', kontrahent, name= "wszyscy_kontrahenci"),
    path('nowy_kontrahent/', nowy_kontrahent, name ="nowy_kontrahent"),
    path('edytuj_kontrahent/<int:id>/', edytuj_kontrahent, name ="edytuj_kontrahenta"),
    path('usun_kontrahent/<int:id>/', usun_kontrahenta, name="usun_kontrahenta"),
    path('usun_indeks/<int:id>/', usun_indeks, name="usun_indeks"),
    path('edytuj_indeks//<int:id>/', edytuj_indeks, name= "edytuj_indeks"),

    
    path('', glowna),
]
