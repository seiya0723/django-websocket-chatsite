from django.db import models
from django.utils import timezone


class Room(models.Model):
    created_at  = models.DateTimeField(verbose_name="投稿日時",default=timezone.now)
    name        = models.CharField(verbose_name="部屋名", max_length=200, unique=True)

class ChatLog(models.Model):
    created_at  = models.DateTimeField(verbose_name="投稿日時",default=timezone.now)
    message     = models.CharField(verbose_name="メッセージ", max_length=200)
    room        = models.ForeignKey(Room , verbose_name="部屋", on_delete=models.CASCADE)
    


