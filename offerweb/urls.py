
from django.urls import path
from offerweb.views import wszystkie_oferty, glowna, kontrahent, nowy_kontrahent, edytuj_kontrahent, usun_kontrahenta

urlpatterns = [
    path('oferty/', wszystkie_oferty),
    path('kontrahent/', kontrahent),
    path('nowy_kontrahent/', nowy_kontrahent),
    path('edytuj_kontrahent/<int:id>/', edytuj_kontrahent),
    path('usun_kontrahent/<int:id>/', usun_kontrahenta),
    path('', glowna),
]
