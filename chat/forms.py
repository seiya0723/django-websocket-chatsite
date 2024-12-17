# == This code was created by https://noauto-nolife.com/post/django-auto-create-models-forms-admin/ == #

from django import forms
from .models import Room,ChatLog

class RoomForm(forms.ModelForm):
    class Meta:
        model	= Room
        fields	= [ "name" ]

class ChatLogForm(forms.ModelForm):
    class Meta:
        model	= ChatLog
        fields	= [ "message", "room" ]

