from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Kontrahent
from .forms import KontrahentForm

@login_required
def wszystkie_oferty(request):
    #return HttpResponse('To jest test')
    return render(request, 'oferty.html')


def glowna(request):
    #return HttpResponse('To jest test')
    return render(request, 'home.html')

def kontrahent(request):
    kontrahenci = Kontrahent.objects.all()
    return render(request, 'kontrahent.html',{"kontrahenci":kontrahenci})

def nowy_kontrahent(request):
    kontrahenci_form =KontrahentForm(request.POST or None)
    if kontrahenci_form.is_valid():
        kontrahenci_form.save()
        return redirect(kontrahent)
    return render(request, 'nowy_kontrahent.html',{'kontrahenci': kontrahent})

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