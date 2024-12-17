from django.shortcuts import render,redirect
from django.views import View

from .models import Room,ChatLog
from .forms import RoomForm,ChatLogForm

class IndexView(View):
    def get(self, request, *args, **kwargs):

        context = {}
        context["rooms"]    = Room.objects.all()

        return render(request,"chat/index.html", context)

    def post(self, request, *args, **kwargs):
        form    = RoomForm(request.POST)

        if not form.is_valid():
            return redirect("chat:index")

        room    = form.save()

        return redirect("chat:room", room.id)

index   = IndexView.as_view()

class RoomView(View):

    def get(self,request, room_name, *args,**kwargs):
        context = {}
        context["room_name"]    = room_name

        context["room"]         = Room.objects.filter(id=room_name).first()
        context["chat_logs"]    = ChatLog.objects.filter(room=room_name).order_by("created_at")

        return render(request,"chat/room.html",context)

room    = RoomView.as_view()

