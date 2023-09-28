from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver, Signal
from .models import Oferty
from django.core.signals import request_finished

@receiver ([post_save, pre_save], sender=Oferty)   
def order_po_zapisaniu (sender, instance, **kwargs):
     print("własnie stworzyłem numer oferty")    
     print(instance.nr_zew)
post_save.connect(order_po_zapisaniu,sender=Oferty) 

@receiver (request_finished, sender=Oferty)   
def order_po_zapisaniu (sender, instance, **kwargs):
     print("własnie stworzyłem numer oferty")    
     print(instance.nr_zew)
post_save.connect(order_po_zapisaniu,sender=Oferty) 