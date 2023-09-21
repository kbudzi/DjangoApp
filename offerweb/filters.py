import django_filters
from .models import Oferty
                            
class ListingFilter(django_filters.FilterSet):
    class Meta:
        model = Oferty
        fields = ['Uwagi', 'nr_zew','kontrahenci','status','data']