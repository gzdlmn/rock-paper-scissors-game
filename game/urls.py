from django.contrib import admin
from django.urls import path,include
from game import views

app_name="game"
urlpatterns=[
    path('withcomputer', views.create_game, name="withcomputer"),
    path('withyourself', views.create_game_yourself, name="withyourself"),
]