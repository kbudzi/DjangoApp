
from django.urls import path
from offerweb.views import wszystkie_oferty, glowna, kontrahent, nowy_kontrahent, edytuj_kontrahent, usun_kontrahenta

urlpatterns = [
    path('oferty/', wszystkie_oferty),
    path('kontrahent/', kontrahent, name= "wszyscy_kontrahenci"),
    path('nowy_kontrahent/', nowy_kontrahent, name ="nowy_kontrahent"),
    path('edytuj_kontrahent/<int:id>/', edytuj_kontrahent, name ="edytuj_kontrahenta"),
    path('usun_kontrahent/<int:id>/', usun_kontrahenta, name="usun_kontrahenta"),
    path('', glowna),
]
