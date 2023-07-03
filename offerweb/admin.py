from django.contrib import admin
from .models import Kontrahent, Oferty, Indeksy,Technologia, Operacje

'''@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    #fields = ['tytul', 'opis','rok'] #
    #exclude=['opis'] # wszystkie poza opisem
    list_display = ["tytul", "imdb_rating",'rok']
    list_filter = ('rok',)
    search_fields = ('tytul','opis')'''
@admin.register(Kontrahent)
class KontrahentAdmin(admin.ModelAdmin):
    list_display = ["Nazwa","email"]

    

@admin.register(Oferty)   
class OfertyAdmin(admin.ModelAdmin):
    list_select_related = False
    list_display = ["Uwagi",'kontrahenci','data','status']        

admin.site.register(Indeksy)
admin.site.register(Technologia)
admin.site.register(Operacje)
