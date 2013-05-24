from django import forms
from sleep.models import SleeperProfile

class SleeperProfileForm(forms.ModelForm):
    class Meta:
        model = SleeperProfile
        fields = ['privacy','privacyLoggedIn']

class CreepSearchForm(forms.Form):
    username = forms.CharField(max_length=30)
