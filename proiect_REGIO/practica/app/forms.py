from django import forms
from .models import Bypass

class BypassForm(forms.ModelForm):
    class Meta:
        model = Bypass
        fields = ['motiv', 'sofer', 'transportator', 'cisterna', 'tip', 'tip_statie', 'utilizator', 'observatii']

    # Define the 'observatii' field explicitly with the desired widget
    observatii = forms.CharField(
        widget=forms.Textarea(attrs={
            'id': 'id_observatii',
            'maxlength': 300,
            'required': 'required',
            'placeholder': 'Introduceți observațiile...',
            'rows': 6,  # Adjust the height of the textarea if needed
            'cols': 40,  # Adjust the width of the textarea if needed
        }),
        label='Observații'
    )

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(BypassForm, self).__init__(*args, **kwargs)
        if user is not None:
            self.fields['utilizator'].initial = user
            self.fields['utilizator'].disabled = True  # Blochează câmpul 'utilizator'
