from django.contrib.auth.models import User
from django.db import models


class Words(models.Model):
    word = models.CharField(max_length=200)

    def __str__(self):
        return self.word


class Guess(models.Model):
    guess = models.CharField(max_length=1)
    words = models.ForeignKey(Words, on_delete=models.CASCADE)

    def __str__(self):
        return f"Letra {self.guess} da palavra {self.words}"


class Player(models.Model):
    state = (
        ('P', 'Jogando'),
        ('D', 'Perdeu'),
        ('W', 'Ganhou')
    )
    name = models.CharField(max_length=200)
    life = models.IntegerField(default=6)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
