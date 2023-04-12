import redis
import json
from django.shortcuts import render
from django.conf import settings
from rest_framework import viewsets
from rest_framework.response import Response

from .models import *
from .serializers import *

cache = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0, decode_responses=True)


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    def list(self, request, *args, **kwargs):
        game = map(json.loads, cache.hvals("all_game"))
        return Response({"game": game})

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.get("pk")

        return Response(json.loads(cache.hget("all_game", pk)))

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        pk = response.data["id"]
        cache.hset("all_game", pk, json.dumps(response.data))
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)

        pk = kwargs.get("pk")
        cache.hset("all_game", pk, json.dumps(response.data))
        return response

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        pk = kwargs.get("pk")
        cache.hdel("all_game", pk)
        return response


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        game = map(json.loads, cache.hvals("all_game"))

        return Response({"user": serializer.data, "games": game})
