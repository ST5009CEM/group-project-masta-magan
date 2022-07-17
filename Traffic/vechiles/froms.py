from django import forms
from vechiles.models import CheatModel

class CheatForm(forms.ModelForm):
    class Meta:
        model=CheatModel
        fields ="__all__"