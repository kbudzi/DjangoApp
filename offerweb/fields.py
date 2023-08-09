from django.db import models
from django.core.exceptions import ObjectDoesNotExist

class OrderField(models.PositiveIntegerField):

    def pre_save (self, model_instance, add):
        if getattr(model_instance, self.attname) is None:
            try:
                obj = self.model.objects.latest(self.attname)
                value = obj.order + 1
            except ObjectDoesNotExist:
                value = 1
            return value
        else:
            return super().pre_save(model_instance, add)