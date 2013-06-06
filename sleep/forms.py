from django import forms
from sleep.models import SleeperProfile, Sleep

class SleeperProfileForm(forms.ModelForm):
    class Meta:
        model = SleeperProfile
        fields = ['privacy','privacyLoggedIn','privacyFriends', 'use12HourTime', 'idealSleep']

class CreepSearchForm(forms.Form):
    username = forms.CharField(max_length=30)

class FriendSearchForm(forms.Form):
    username = forms.CharField(max_length=30)

class UpdateSleepForm(forms.ModelForm):
    forceOverlap = forms.BooleanField(required=False)
    class Meta:
        model = Sleep
        fields = ['start_time','end_time', 'date', 'comments']
