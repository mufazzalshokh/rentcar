from django.db.models.signals import pre_save
from django.dispatch import receiver

from shop.models import CarModel


@receiver(pre_save, sender=CarModel)
def real_price_calc(sender, instance, *args, **kwargs):
    if instance.is_discount():
        instance.real_price = instance.price - instance.price * instance.discount / 100
    else:
        instance.real_price = instance.price
