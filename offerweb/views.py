from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Kontrahent , Oferty, Indeksy, Operacje, Technologia, Gatunek, Kalkulator
from .forms import KontrahentForm, OfertaForm, IndeksForm,OperacjeForm, TechnologiaForm, GatunekForm, WalekForm,BlachaForm, Fgatunek
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.db.models import Q
from .filters import ListingFilter
from django.urls import reverse_lazy
from bootstrap_modal_forms.generic import BSModalCreateView
from django.template import loader
import math
from django.contrib import messages

def glowna(request):
    
    return render(request, 'home.html')


@login_required
def wszystkie_oferty(request):
    oferty =Oferty.objects.all()
    my_Filter = ListingFilter(request.GET, queryset=oferty)
    oferty = my_Filter.qs
    return render(request, 'oferty.html',{'oferty': oferty,"my_Filter": my_Filter})

#def filter(request):
 #   mydata = Oferty.objects.filter(Q(email='budzichowski@tes.com.pl')).values()
#    return render(request, 'oferty.html',{'mymembers': mydata})

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
    ofer = Oferty.objects.get(pk=oferty.id)
    indeksy = Indeksy.objects.filter(oferta=ofer)
    indeksy_form = IndeksForm(request.POST or None)#instance=oferty
    
    if oferta_form.is_valid():
        oferta_form.save()
        return redirect(wszystkie_oferty)
    return render(request, 'send_offer.html',{'oferta_form': oferta_form, 'indeksy':indeksy,'indeksy_form':indeksy_form,})
@login_required
def edytuj_oferte(request, id):
    oferty = get_object_or_404(Oferty, pk=id)
    t=oferty.id
    ofer = Oferty.objects.get(pk=oferty.id)
    kontrahenci = Kontrahent.objects.get(pk=oferty.kontrahenci.id)
    oferta_form =OfertaForm(request.GET or None, instance=oferty)
    indeksy = Indeksy.objects.filter(oferta=ofer)
    indeksy_form = IndeksForm(request.POST or None)#instance=oferty
    request.session['ofertaid'] = t
    if request.method == 'POST':
        if 'indeks' in request.POST:

            ind = indeksy_form.save(commit=False)
            ind.kontrahent = kontrahenci
            ind.save()
            b=ind.id
            ind = Indeksy.objects.get(id=b)
            ofe = ofer
            ind.oferta.add(ofe)
            ind.save()
            return HttpResponseRedirect(reverse("edytuj_oferte", args=[id]))
    #t=kontrahent.id  
    return render(request, 'edytuj_oferte.html',{'oferta_form': oferta_form, 'indeksy':indeksy, 'indeksy_form':indeksy_form, 't':t})


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
    return render(request, 'nowy_kontrahent.html',{'kontrahenci_form': kontrahenci_form})

def edytuj_kontrahent(request, id):
    kontrahenci = get_object_or_404(Kontrahent, pk=id)
    kontrahenci_form =KontrahentForm(request.POST or None, instance=kontrahenci)
    if kontrahenci_form.is_valid():
        kontrahenci_form.save()
        return redirect(kontrahent)
    return render(request, 'nowy_kontrahent.html',{'kontrahenci_form': kontrahenci_form})

@login_required
def indeksy_oferta(request, id):
    oferty = get_object_or_404(Oferty, pk=id)
    kontrahent = Kontrahent.objects.get(pk=oferty.kontrahenci.id)
    indeksy = Indeksy.objects.filter(kontrahent=kontrahent)
    oid=oferty.id
    kon=kontrahent.id
    request.session['oid'] = oid
    request.session['kon'] = kon
    return render(request, 'wybierz_indeks.html',{'indeksy': indeksy, 'oferty':oferty})

def add_new_indeks (request, **kwargs):

    oid = request.session.get('oid')
    oferty = get_object_or_404(Oferty, pk=self.id)
    indeksy_form = IndeksForm(request.POST or None)#instance=oferty
    kontrahenci = Kontrahent.objects.get(pk=oferty.kontrahenci.id)
    
    if request.method == 'POST':
        if 'indeks' in request.POST:
            
            of=Oferty.objects.get(id=oid)
            ind = indeksy_form.save(commit=False)
            ind.kontrahent = kontrahenci
            ind.oferta.add(of)
            ind.save()
            
            return HttpResponseRedirect(reverse("edytuj_oferte", args=[64])) 
    return render(request, 'add_new_indeks.html',{'indeksy_form':indeksy_form})
class BookCreateView(BSModalCreateView):
    template_name = 'add_new_indeks.html'
    form_class = IndeksForm
    success_message = 'Success: Book was created.'
    success_url = reverse_lazy('index')


#def dodaj_do_bazy():
@login_required
def add_indeks(request, id):
    indeksy = get_object_or_404(Indeksy, pk=id)
    oferty = Oferty.objects.all()
    
    if request.method == "POST":
        indeks_add = Indeksy.objects.get(id=id)
        oid = request.session.get('oid')
        #kon = request.session.get('kon')  #pobieram id kontrahenta
        of=Oferty.objects.get(id=oid)
        indeks_add.oferta.add(of)    
        indeks_add.save()
        return HttpResponseRedirect(reverse("edytuj_oferte", args=[oid]))
              
    return render(request, 'add_indeks.html',{'indeksy': indeksy, 'oferty':oferty})

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
    ofertaid = request.session.get('ofertaid')
    oferta_id = ofertaid
    if request.method == "POST":
        indeks.delete()
        #return redirect (wszystkie_oferty)
        return redirect("edytuj_oferte", id=oferta_id)
    return render(request, 'usun_indeks.html',{'indeks': indeks})

@login_required
def edytuj_indeks(request, id):
    indeks = get_object_or_404(Indeksy, pk=id)
    #oferta_id = indeks.oferta.id
    ofertaid = request.session.get('ofertaid')
    oferta_id = ofertaid
    indeksy_form = IndeksForm(request.POST or None, instance=indeks)
    techno_form = TechnologiaForm(request.POST or None)
    
    #oper = Technologia.objects.get(id=id)
    mytechno = Technologia.objects.filter(indeks=indeks)
    
    #technologia_form = TechnologiaForm(request.POST or None, instance=indeks)
    if all((indeksy_form.is_valid , techno_form.is_valid())):
        #indeksy_form.save()
        tech = techno_form.save(commit=False)
        tech.indeks = indeks
        
        tech.save()
        return redirect("edytuj_oferte", id=oferta_id)
    return render(request, 'edytuj_indeks.html',{'indeksy_form':indeksy_form, 'techno_form':techno_form, 'technologia':technologia})


@login_required
def operacje(request):
    operacje =Operacje.objects.all()
    return render(request, 'operacje.html',{'operacje': operacje})

def dodaj_operacje(request):
    operacje_form =OperacjeForm(request.POST or None)
    
    
    if operacje_form.is_valid():
        operacje_form.save()
        return redirect('operacje')
    return render(request, 'dodaj_operacje.html',{'operacje_form': operacje_form})

def usun_operacje(request,id):
    operacja = get_object_or_404(Operacje, pk=id)
    if request.method == "POST":
        operacja.delete()
        return redirect ('operacje')

    return render(request, 'usun_operacje.html',{'operacja': operacja})




def gatunek(request):
    gatunki = Gatunek.objects.all()
    return render(request, 'gatunek.html',{'gatunki': gatunki})
def nowy_gatunek(request):
    gatunek_form =GatunekForm(request.POST or None)
    if gatunek_form.is_valid():
        gatunek_form.save()
        return redirect('gatunek')
        
    return render(request, 'nowy_gatunek.html',{'gatunek_form': gatunek_form})

def usun_gatunek(request,id):
    gatunek = get_object_or_404(Gatunek, pk=id)
    if request.method == "POST":
        gatunek.delete()
        return redirect ('gatunek')

    return render(request, 'usun_gatunek.html',{'gatunek': gatunek})

def kalkulator(request):
    blacha_form= BlachaForm(request.POST or None)
    walek_form= WalekForm(request.POST or None)
    gatunek =Gatunek.objects.all()
    form = Fgatunek()
    info1 = ''
    info2 = ''
    info3 = ''
    info4 = ''
    result=0
    cost=0

    if request.method == 'POST':
        if request.method == 'POST':
            my_variable = request.POST.get('my_variable_name') #wybór profilu
            price = request.POST.get('cena') #cena z template
            
            if my_variable == 'Blacha':
                sz = request.POST.get('sz')
                gr = request.POST.get('gr')
                dl = request.POST.get('dl')
                g=request.POST.get('lista')#wybór gatunku
                for m in gatunek:
                    if g==m.nazwa:
                        choise=m.gestosc
                        choise_id=m.id
                result= round(float(sz)*float(gr)*float(dl)*float(choise)/1000000, 2)
                info1 = 'Blacha'+' - '+g
                info2 = 'Szerokość'+' - '+sz+' mm'
                info3 = 'Grubość'+' - '+gr+' mm'
                info4 = 'Długość'+' - '+dl+' mm'
                try:
                    cost= round(float(price)*float(result),2)
                except ValueError:
                    cost=0
                
                blach=Kalkulator(dlugosc=dl,grubosc=gr,szerokosc=sz,profil=my_variable,waga=result, wartosc=cost,gatunek_id=choise_id)
                blach.save()
            elif my_variable == 'Walek':
                sr = request.POST.get('sr')
                d = request.POST.get('d')
                g=request.POST.get('lista') #wybór gatunku
                for m in gatunek:
                    if g==m.nazwa:
                        choise=m.gestosc
                        choise_id=m.id
                result= round((float(sr)/2)**2*math.pi*float(d)*float(choise)/1000000,2)
                info1 = 'Pręt'+' - '+g
                info2 = 'Średnica'+' - '+sr+' mm'

                info3 = 'Długość'+' - '+d+' mm'
                info4 = ''
                try:
                    cost= round(float(price)*float(result),2)
                except ValueError:
                    cost=0
                blach=Kalkulator(dlugosc=d,srednica=sr,profil=my_variable,waga=result,wartosc=cost,gatunek_id=choise_id)
                blach.save()
              
            elif my_variable == 'Rura':
                rsr = request.POST.get('rsr')
                rgs = request.POST.get('rgs')
                rd = request.POST.get('rd')
                g=request.POST.get('lista') #wybór gatunku
                for m in gatunek:
                    if g==m.nazwa:
                        choise=m.gestosc
                        choise_id=m.id
                if float(rgs)<(float(rsr)/2):
                    result= round(((float(rsr)/2)**2*math.pi*float(rd)*float(choise)/1000000)-(((float(rsr)-(float(rgs)*2))/2)**2*math.pi*float(rd)*float(choise)/1000000),2)
                else:
                    print('podaj właściwą wartość')
                    messages.warning(request, 'Podaj właściwe wymiary!!!')

                info1 = 'Rura'+' - '+g
                info2 = 'Średnica'+' - '+rsr+' mm'

                info3 = 'Grubość ścianki'+' - '+rgs+' mm'
                info4 = 'Długość'+' - '+rd+' mm'
                try:
                    cost= round(float(price)*float(result),2)
                except ValueError:
                    cost=0
                blach=Kalkulator(dlugosc=rd,srednica=rsr,grubosc_scianki=rgs,profil=my_variable,waga=result,wartosc=cost,gatunek_id=choise_id)
                blach.save()

            elif my_variable == 'Rurakw':
                rsr = request.POST.get('bok')
                rgs = request.POST.get('rgs')
                rd = request.POST.get('rd')
                g=request.POST.get('lista') #wybór gatunku
                for m in gatunek:
                    if g==m.nazwa:
                        choise=m.gestosc
                        choise_id=m.id
                result= round(((float(rsr)/2)**2*math.pi*float(rd)*float(choise)/1000000)-(((float(rsr)-(float(rgs)*2))/2)**2*math.pi*float(rd)*float(choise)/1000000),2)
                try:
                    cost= round(float(price)*float(result),2)
                except ValueError:
                    cost=0
                messages.success(request, "cena 0" )
                blach=Kalkulator(dlugosc=rd,srednica=rsr,grubosc_scianki=rgs, profil=my_variable,waga=result,wartosc=cost,gatunek_id=choise_id)
                blach.save()
    else:
        print('STOP')
    return render(request, 'kalkulator.html', {'form': form, 'blacha_form':blacha_form, 'walek_form':walek_form,'result':result,'cost':cost,'info1':info1,'info4':info4,'info2':info2,'info3':info3,})