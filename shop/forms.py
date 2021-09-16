from django import forms

from shop.models import ColorModel


class ColorModelForm(forms.ModelForm):
    class Meta:
        model = ColorModel
        fields = '__all__'
        widgets = {
            'code': forms.TextInput(attrs={
                'type': 'color'
            })
        }
