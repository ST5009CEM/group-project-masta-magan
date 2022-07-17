from django import forms
from user.models import UserInfoModel

class UserInfoForm(forms.ModelForm):
    class Meta:
        model=UserInfoModel
        fields ="__all__"

