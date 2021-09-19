from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _

UserModel = get_user_model()


class ProfileModel(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='profile')
    country = models.CharField(max_length=30, null=True, blank=True)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=30, null=True, blank=True)
    state = models.CharField(max_length=30, null=True, blank=True)
    postcode = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = _('profile')
        verbose_name_plural = _('profiles')
