from django import forms
from .models import Artist


class ArtistForm(forms.ModelForm):
    """
    Creates an artist form
    """
    class Meta:
        model = Artist
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
