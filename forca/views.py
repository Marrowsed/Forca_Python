from .functions import *
import random
import re

from django.contrib.auth.models import User
from django.shortcuts import render
from .decorator import *
from django.contrib import messages

# Create your views here.
from forca.decorator import player_created, \
    player_not_created  # Decorators to prevent the player to going back to Index or Entering the Index before the game finishes
from .models import Guess


@player_not_created
def index(request):
    """
    Index where the player creates his alias as a visitor
    """
    user = User.objects.get(id=2)
    if request.method == 'POST':
        name = request.POST['playerName']
        if Player.objects.filter(name=name).exists():
            messages.error(request, "Conta já existente !", extra_tags="alert alert-danger")
            return redirect("index")
        else:
            Player.objects.create(name=name, user=user)
            return redirect("/jogar")
    return render(request, "index.html")


@player_created
def jogar(request):
    """
    The visitor play the Hangman with his alias
    """
    w = Words.objects.all().count()
    p = Player.objects.get(user=2)  # User ID 2 is Visitor
    data = {
        "p": p, "w": w
    }
    final_word = randomize_word()
    data.update({
        'palavra': final_word
    })
    return render(request, "jogar.html", data)


@player_created
def randomize(request, pk):
    """
    Receives the random word and the user can try to guess it before the hang
    """
    pal = Words.objects.get(id=pk)
    p = Player.objects.get(user=2)
    pal_lower = pal.word.lower()
    # print(p.life)
    blank = generate_hang(pal_lower)
    guesses = []
    acertos = Guess.objects.filter(words=pal)  # Filter by word !
    for a in acertos:
        guesses.append(a.guess)
        indexes = [i.start() for i in re.finditer(a.guess, pal_lower)]  # Find all the index from the guess
        for i in indexes:
            blank[i] = a.guess
    data = {
        "palavra": pal, "blank": blank, "life": p.life, 'guesses': guesses
    }
    if p.life == 0:
        p.delete()  # Delete the player for another try !
        messages.error(request, f"Você zerou as vidas ! A palavra era: {pal.word.upper()} Tente novamente com outra palavra !",
                       extra_tags="alert alert-danger")
        return redirect("index")
    elif "_" not in blank:
        p.delete()  # Delete the player for another try !
        messages.success(request, f"Você venceu o jogo ! A palavra era: {pal.word.upper()} Tente novamente com outra palavra !",
                         extra_tags="alert alert-success")
        return redirect("index")
    if request.method == 'POST':
        guess = request.POST['guess']
        guesses.append(guess)
        if len(guess) <= 1 and guess != " ":  # If you try to put more than a letter or a blak space
            Guess.objects.create(guess=guess, words=pal)
            if guess not in pal_lower:
                p.life -= 1
                p.save()
                data.update({
                    "life": p.life,
                })
        else:
            messages.error(request, "Tentativa Errada !", extra_tags="alert alert-danger")  # Error message
        return redirect(f"/jogar/regras/{pal.id}")
    return render(request, 'randomize.html', data)
