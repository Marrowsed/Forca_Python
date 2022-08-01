from django.urls import path
from .views import *

urlpatterns = [
                  path('', index, name="index"),
                  path('jogar', jogar, name="jogar"),
                  path('jogar/regras/<str:pk>', randomize, name="randomize"),
              ]