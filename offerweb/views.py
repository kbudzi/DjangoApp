from django.shortcuts import render
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
    #return HttpResponse('To jest test')
    kontrahenci = Kontrahent.objects.all()
    return render(request, 'kontrahent.html',{"kontrahenci":kontrahenci})