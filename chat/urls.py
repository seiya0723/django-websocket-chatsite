from django.urls import path
from . import views

app_name    = "chat"
urlpatterns = [
    path('', views.index, name="index"),
    path('chat/<int:room_name>/', views.room, name='room'),
]

