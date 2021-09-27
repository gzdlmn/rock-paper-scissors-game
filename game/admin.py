from django.contrib import admin
from . models import GameModel,GameModelYourself

# Register your models here.
admin.site.register(GameModel)
admin.site.register(GameModelYourself)