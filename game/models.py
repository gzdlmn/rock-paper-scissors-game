from django.db import models
import random
# Create your models here.


def randomgame():
    list=['rock','paper','scissors']
    return random.choice(list)
class GameModel(models.Model):
    user = models.ForeignKey("auth.user", null=True, blank=False, on_delete=models.CASCADE)
    computer = models.CharField(default=randomgame, max_length=10, null=True, blank=False)
    gamer = models.CharField(default=randomgame, max_length=10, null=True, blank=False)

    class Meta:
        verbose_name_plural="Computer and Player"
    def __str__(self):
        return "{}-{}-{}".format(self.computer, self.gamer, self.user)

    def icon_computer(self):
        if self.computer == "rock":
            return '<i style="color:#ebc8b2;" class="fas fa-hand-rock"></i>'.format(self.computer)
        elif self.computer == "paper":
            return '<i style="color:#ebc8b2;" class="fas fa-hand-paper"></i>'.format(self.computer)
        elif self.computer == "scissors":
            return '<i style="color:#ebc8b2;" class="fas fa-hand-scissors"></i>'.format(self.computer)

    def icon_gamer(self):
        if self.gamer == "rock":
            return '<i style="color:#ebc8b2;" class="fas fa-hand-rock"></i>'.format(self.gamer)
        elif self.gamer == "paper":
            return '<i style="color:#ebc8b2;" class="fas fa-hand-paper"></i>'.format(self.gamer)
        elif self.gamer == "scissors":
            return '<i style="color:#ebc8b2;" class="fas fa-hand-scissors"></i>'.format(self.gamer)


    #gamer için kazanma kaybetme durumu
    def counter_gamer(self):
        if self.gamer == "rock":
            if self.computer == "rock":
                return '<i class="fas fa-equals"></i>'.format(self.gamer)
            elif self.computer == "paper":
                return '<i style="color:red;" class="fas fa-times"></i>'.format(self.gamer)
            else:
                return '<i style="color:green;" class="fas fa-check"></i>'.format(self.gamer)
        elif self.gamer == "paper":
            if self.computer == "paper":
                return '<i class="fas fa-equals"></i>'.format(self.gamer)
            elif self.computer == "rock":
                return '<i style="color:green;" class="fas fa-check"></i>'.format(self.gamer)
            else:
                return '<i style="color:red;" class="fas fa-times"></i>'.format(self.gamer)
        else:
            if self.computer == "scissors":
                return '<i class="fas fa-equals"></i>'.format(self.gamer)
            elif self.computer == "rock":
                return '<i style="color:red;" class="fas fa-times"></i>'.format(self.gamer)
            else:
                return '<i style="color:green;" class="fas fa-check"></i>'.format(self.gamer)






class GameModelYourself(models.Model):
    user = models.ForeignKey("auth.user", null=True, blank=False, on_delete=models.CASCADE)
    SELECT = (('rock','rock'), ('paper','paper'), ('scissors','scissors'))
    computer = models.CharField(default=randomgame, null=True, blank=False, max_length=10)
    gamer = models.CharField(choices=SELECT, null=True, blank=False, max_length=10)
    class Meta:
        verbose_name_plural="Computer and Player Yourself"
    def __str__(self):
        return "{}-{}-{}".format(self.computer, self.gamer, self.user)

    def icon_computer_yourself(self):
        if self.computer == "rock":
            return '<i style="color:#ebc8b2;" class="fas fa-hand-rock"></i>'.format(self.computer)
        elif self.computer == "paper":
            return '<i style="color:#ebc8b2;" class="fas fa-hand-paper"></i>'.format(self.computer)
        elif self.computer == "scissors":
            return '<i style="color:#ebc8b2;" class="fas fa-hand-scissors"></i>'.format(self.computer)

    def icon_gamer_yourself(self):
        if self.gamer == "rock":
            return '<i style="color:#ebc8b2;" class="fas fa-hand-rock"></i>'.format(self.gamer)
        elif self.gamer == "paper":
            return '<i style="color:#ebc8b2;" class="fas fa-hand-paper"></i>'.format(self.gamer)
        elif self.gamer == "scissors":
            return '<i style="color:#ebc8b2;" class="fas fa-hand-scissors"></i>'.format(self.gamer)

    def counter_gamer_yourself(self):
        if self.gamer == "rock":
            if self.computer == "rock":
                return '<i class="fas fa-equals"></i>'.format(self.gamer)
            elif self.computer == "paper":
                return '<i style="color:red;" class="fas fa-times"></i>'.format(self.gamer)
            else:
                return '<i style="color:green;" class="fas fa-check"></i>'.format(self.gamer)
        elif self.gamer == "paper":
            if self.computer == "paper":
                return '<i class="fas fa-equals"></i>'.format(self.gamer)
            elif self.computer == "rock":
                return '<i style="color:green;" class="fas fa-check"></i>'.format(self.gamer)
            else:
                return '<i style="color:red;" class="fas fa-times"></i>'.format(self.gamer)
        else:
            if self.computer == "scissors":
                return '<i class="fas fa-equals"></i>'.format(self.gamer)
            elif self.computer == "rock":
                return '<i style="color:red;" class="fas fa-times"></i>'.format(self.gamer)
            else:
                return '<i style="color:green;" class="fas fa-check"></i>'.format(self.gamer)
