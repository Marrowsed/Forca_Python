from .functions import *
import random

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


def generate(request):
    """
    Call the function to populate the DB
    """
    generate_db()
    return redirect("/jogar")

@player_created
def randomize(request, pk):
    """
    Receives the random word and the user can try to guess it before the hang
    """
    pal = Words.objects.get(id=pk)
    p = Player.objects.get(user=2)
    #print(p.life)
    tam = len(pal.word)
    blank = []
    for _ in range(tam):
        blank.append("_")
    acertos = Guess.objects.filter(words=pal)
    for a in acertos:
        count = pal.word.count(a.guess)
        i = pal.word.index(a.guess)
        blank[i] = a.guess
        if count > 1:
            j = pal.word.index(a.guess, i +1) # Validating for words with 2 or more equal letters
            blank[j] = a.guess
    data = {
            "palavra": pal, "blank": blank, "life": p.life
        }
    if p.life == 0:
        p.delete()  # Delete the player for another try !
        messages.error(request, "Você zerou as vidas ! Tente novamente com outra palavra !", extra_tags="alert alert-damger")
        return redirect("index")
    elif "_" not in blank:
        p.delete() # Delete the player for another try !
        messages.success(request, "Você venceu o jogo ! Tente novamente com outra palavra !", extra_tags="alert alert-sucess")
        return redirect("index")
    if request.method == 'POST':
        guess = request.POST['guess']
        if len(guess) <= 1:
            if guess in pal.word:
                Guess.objects.create(guess=guess, words=pal)
            else:
                p.life -= 1
                p.save()
                data.update({
                    "life": p.life
                })
        else:
            messages.error(request, "Somente 1 Letra !", extra_tags="alert alert-danger")
        return redirect(f"/jogar/regras/{pal.id}")
    return render(request, 'randomize.html', data)

