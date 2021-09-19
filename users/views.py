from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import UpdateView

from users.forms import ProfileModelForm
from users.models import ProfileModel


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    form_class = ProfileModelForm
    template_name = 'profile.html'

    def get_object(self, queryset=None):
        # _ -> bosh ozgaruvchi; xotira egallamaydi
        profile, _ = ProfileModel.objects.get_or_create(user=self.request.user)
        return profile

    def get_success_url(self):
        return reverse('profile:home')
