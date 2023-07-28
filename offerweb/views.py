from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Kontrahent , Oferty, Indeksy, Operacje
from .forms import KontrahentForm, OfertaForm, IndeksForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required

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

@login_required
def edytuj_top_oferty(request, id):
    oferty = get_object_or_404(Oferty, pk=id)
    oferta_form =OfertaForm(request.POST or None, instance=oferty)
    indeksy = Indeksy.objects.filter(Oferta=oferty)
    
    if oferta_form.is_valid():
        oferta_form.save()
        return redirect(wszystkie_oferty)
    return render(request, 'edytuj_oferte.html',{'oferta_form': oferta_form, 'indeksy':indeksy})
@login_required
def edytuj_oferte(request, id):
    oferty = get_object_or_404(Oferty, pk=id)
    oferta_form =OfertaForm(request.GET or None, instance=oferty)
    indeksy = Indeksy.objects.filter(oferta=oferty) # lista indeksów dla danej oferty
    indeksy_form = IndeksForm(request.POST or None)#instance=oferty
    if request.method == 'POST':
        if 'indeks' in request.POST:
            indeks = indeksy_form.save(commit=False)
            indeks.oferta = oferty
            indeks.save()
            return HttpResponseRedirect(reverse("edytuj_oferte", args=[id]))

    return render(request, 'edytuj_oferte.html',{'oferta_form': oferta_form, 'indeksy':indeksy, 'indeksy_form':indeksy_form})
@login_required
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
        return redirect('/')
        
        #try:
        #    return redirect(edytuj_oferte)
        #except :
        #    return redirect(kontrahent)
        
    return render(request, 'nowy_kontrahent.html',{'kontrahenci_form': kontrahenci_form})

def edytuj_kontrahent(request, id):
    kontrahenci = get_object_or_404(Kontrahent, pk=id)
    kontrahenci_form =KontrahentForm(request.POST or None, instance=kontrahenci)
    if kontrahenci_form.is_valid():
        kontrahenci_form.save()
        return redirect(kontrahent)
    return render(request, 'nowy_kontrahent.html',{'kontrahenci_form': kontrahenci_form})
@login_required
def usun_kontrahenta(request, id):
    kontrahenci = get_object_or_404(Kontrahent, pk=id)
    if request.method == "POST":
        kontrahenci.delete()
        return redirect (kontrahent)

    return render(request, 'usun_kontrahenta.html',{'kontrahenci': kontrahenci})
@login_required
def usun_indeks(request, id):
    indeks = get_object_or_404(Indeksy, pk=id)
    oferta_id = indeks.oferta.id
    if request.method == "POST":
        indeks.delete()
        #return redirect (wszystkie_oferty)
        return redirect("edytuj_oferte", id=oferta_id)
    return render(request, 'usun_indeks.html',{'indeks': indeks})

@login_required
def edytuj_indeks(request, id):
    indeks = get_object_or_404(Indeksy, pk=id)
    oferta_id = indeks.oferta.id
    indeksy_form = IndeksForm(request.POST or None, instance=indeks)
    if indeksy_form.is_valid():
        indeksy_form.save()
        return redirect("edytuj_oferte", id=oferta_id)
            
        

    return render(request, 'edytuj_indeks.html',{'indeksy_form':indeksy_form})


@login_required
def operacje(request):
    operacje =Operacje.objects.all()
    return render(request, 'operacje.html',{'operacje': operacje})

@login_required
def wybierz_indeks(request):
    operacje =Operacje.objects.all()
    return render(request, 'operacje.html',{'operacje': operacje})