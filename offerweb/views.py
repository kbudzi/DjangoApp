from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Kontrahent , Oferty, Indeksy
from .forms import KontrahentForm, OfertaForm, IndeksForm


def glowna(request):
    
    return render(request, 'home.html')


@login_required
def wszystkie_oferty(request):
    oferty =Oferty.objects.all()
    return render(request, 'oferty.html',{'oferty': oferty})

def nowa_oferta(request):
    oferta_form =OfertaForm(request.POST or None)
    if oferta_form.is_valid():
        oferta_form.save()
        return redirect(wszystkie_oferty)
    return render(request, 'nowa_oferta.html',{'oferta_form': oferta_form})

def edytuj_top_oferty(request, id):
    oferty = get_object_or_404(Oferty, pk=id)
    oferta_form =OfertaForm(request.POST or None, instance=oferty)
    indeksy = Indeksy.objects.filter(Oferta=oferty)
    
    if oferta_form.is_valid():
        oferta_form.save()
        return redirect(wszystkie_oferty)
    return render(request, 'edytuj_oferte.html',{'oferta_form': oferta_form, 'indeksy':indeksy })

def edytuj_oferte(request, id):
    oferty = get_object_or_404(Oferty, pk=id)
    oferta_form =OfertaForm(request.GET or None, instance=oferty)
    indeksy = Indeksy.objects.filter(Oferta=oferty)
    
    if oferta_form.is_valid():
        oferta_form.save()
        return redirect(wszystkie_oferty)
    return render(request, 'edytuj_oferte.html',{'oferta_form': oferta_form, 'indeksy':indeksy})
    

def usun_oferte(request, id):
    oferty = get_object_or_404(Oferty, pk=id)
    if request.method == "POST":
        oferty.delete()
        return redirect (wszystkie_oferty)
    return render(request, 'usun_oferte.html',{'oferty': oferty})

def kontrahent(request):
    kontrahenci = Kontrahent.objects.all()
    return render(request, 'kontrahent.html',{"kontrahenci":kontrahenci})

def nowy_kontrahent(request):
    kontrahenci_form =KontrahentForm(request.POST or None)
    if kontrahenci_form.is_valid():
        kontrahenci_form.save()
        return redirect(kontrahent)
    return render(request, 'nowy_kontrahent.html',{'kontrahenci_form': kontrahenci_form})

def edytuj_kontrahent(request, id):
    kontrahenci = get_object_or_404(Kontrahent, pk=id)
    kontrahenci_form =KontrahentForm(request.POST or None, instance=kontrahenci)
    if kontrahenci_form.is_valid():
        kontrahenci_form.save()
        return redirect(kontrahent)
    return render(request, 'nowy_kontrahent.html',{'kontrahenci_form': kontrahenci_form})

def usun_kontrahenta(request, id):
    kontrahenci = get_object_or_404(Kontrahent, pk=id)
    if request.method == "POST":
        kontrahenci.delete()
        return redirect (kontrahent)

    return render(request, 'usun_kontrahenta.html',{'kontrahenci': kontrahenci})

def nowy_indeks(request):
    
    indeksy_form =IndeksForm(request.POST or None)
    if indeksy_form.is_valid():
        indeksy_form.save()
        
        return redirect(request.META.get('HTTP_REFERER'))
    return render(request, 'nowy_indeks.html',{'indeksy_form': indeksy_form})