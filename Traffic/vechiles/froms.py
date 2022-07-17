from django import forms
from vechiles.models import CheatModel, LostModel

class CheatForm(forms.ModelForm):
    class Meta:
        model=CheatModel
        fields ="__all__"

class LostForm(forms.ModelForm):
    class Meta:
        model=LostModel
        fields ="__all__"