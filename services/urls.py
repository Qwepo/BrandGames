from django.urls import path, include


from .views import *
from rest_framework import routers


routers = routers.SimpleRouter()
routers.register("game", GameViewSet, "game")
routers.register("user", UserViewSet, "user")

urlpatterns = [path("api/v1/", include(routers.urls))]
