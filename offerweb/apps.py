from django.apps import AppConfig


class OfferwebConfig(AppConfig):
    name = 'offerweb'
    
    def ready(self):
        import offerweb.signals