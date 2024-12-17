# == This code was created by https://noauto-nolife.com/post/django-auto-create-models-forms-admin/ == #

from django.contrib import admin
from .models import Room,ChatLog

class RoomAdmin(admin.ModelAdmin):
    list_display	= [ "id", "created_at", "name" ]

class ChatLogAdmin(admin.ModelAdmin):
    list_display	= [ "id", "created_at", "message", "room" ]


admin.site.register(Room,RoomAdmin)
admin.site.register(ChatLog,ChatLogAdmin)
