
from django.urls import path
from offerweb.views import wszystkie_oferty, glowna, kontrahent

urlpatterns = [
    path('oferty/', wszystkie_oferty),
    path('kontrahent/', kontrahent),
    path('', glowna),
]
