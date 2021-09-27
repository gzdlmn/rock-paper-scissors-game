from django.shortcuts import render,redirect,reverse
from . models import GameModel,GameModelYourself
from . forms import GameModelForm,GameModelYourselfForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import pygame


# Create your views here.

def home_page(request):
    return render(request, "home.html")

@login_required(login_url="user:login")
def create_game(request):
    gamemodels = GameModel.objects.filter(user=request.user)
    while gamemodels.count() <= 5:
        form = GameModelForm(request.POST or None)
        if form.is_valid():
            gamemodel = form.save(commit=False)
            gamemodel.user = request.user
            if gamemodel.computer == "rock" and gamemodel.gamer == "rock":
                if gamemodels.count() == 5:
                    GameModel.objects.filter(user=request.user).delete()
                    messages.info(request, 'Game over')
                    return redirect('home')
                else:
                    gamemodel.save()
                    return HttpResponseRedirect(reverse('game:withcomputer'))
            elif gamemodel.computer == "rock" and gamemodel.gamer == "paper":
                if gamemodels.count() == 5:
                    GameModel.objects.filter(user=request.user).delete()
                    messages.info(request, 'Game over')
                    return redirect('home')
                else:
                    gamemodel.save()
                    return HttpResponseRedirect(reverse('game:withcomputer'))
            elif gamemodel.computer == "rock" and gamemodel.gamer == "scissors":
                if gamemodels.count() == 5:
                    GameModel.objects.filter(user=request.user).delete()
                    messages.info(request, 'Game over')
                    return redirect('home')
                else:
                    gamemodel.save()
                    return HttpResponseRedirect(reverse('game:withcomputer'))
            elif gamemodel.computer == "paper" and gamemodel.gamer == "paper":
                if gamemodels.count() == 5:
                    GameModel.objects.filter(user=request.user).delete()
                    messages.info(request, 'Game over')
                    return redirect('home')
                else:
                    gamemodel.save()
                    return HttpResponseRedirect(reverse('game:withcomputer'))
            elif gamemodel.computer == "paper" and gamemodel.gamer == "rock":
                if gamemodels.count() == 5:
                    GameModel.objects.filter(user=request.user).delete()
                    messages.info(request, 'Game over')
                    return redirect('home')
                else:
                    gamemodel.save()
                    return HttpResponseRedirect(reverse('game:withcomputer'))
            elif gamemodel.computer == "paper" and gamemodel.gamer == "scissors":
                if gamemodels.count() == 5:
                    GameModel.objects.filter(user=request.user).delete()
                    messages.info(request, 'Game over')
                    return redirect('home')
                else:
                    gamemodel.save()
                    return HttpResponseRedirect(reverse('game:withcomputer'))
            elif gamemodel.computer == "scissors" and gamemodel.gamer == "rock":
                if gamemodels.count() == 5:
                    GameModel.objects.filter(user=request.user).delete()
                    messages.info(request, 'Game over')
                    return redirect('home')
                else:
                    gamemodel.save()
                    return HttpResponseRedirect(reverse('game:withcomputer'))
            elif gamemodel.computer == "scissors" and gamemodel.gamer == "paper":
                if gamemodels.count() == 5:
                    GameModel.objects.filter(user=request.user).delete()
                    messages.info(request, 'Game over')
                    return redirect('home')
                else:
                    gamemodel.save()
                    return HttpResponseRedirect(reverse('game:withcomputer'))
            elif gamemodel.computer == "scissors" and gamemodel.gamer == "scissors":
                if gamemodels.count() == 5:
                    GameModel.objects.filter(user=request.user).delete()
                    messages.info(request, 'Game over')
                    return redirect('home')
                else:
                    gamemodel.save()
                    return HttpResponseRedirect(reverse('game:withcomputer'))
        return render(request, "withcomputer.html", {'form': form, 'gamemodels': gamemodels})


@login_required(login_url="user:login")
def create_game_yourself(request):
    gamemodelyourselflast = GameModelYourself.objects.filter(user=request.user).last()
    form = GameModelYourselfForm(request.POST or None)
    if form.is_valid():
        gamemodelyourself = form.save(commit=False)
        gamemodelyourself.user = request.user
        gamemodelyourself.save()
        return HttpResponseRedirect(reverse('game:withyourself'))
    gamemodelyourselfall = GameModelYourself.objects.filter(user=request.user).all()
    gamemodelyourselfall.delete()
    return render(request, "withyourself.html", {"form":form, 'gamemodelyourselflast':gamemodelyourselflast})
