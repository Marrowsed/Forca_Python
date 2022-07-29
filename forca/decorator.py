from django.shortcuts import redirect

from forca.models import Player


def player_not_created(function):
    """
    Counts the players in the DB, if it's 0 then you have to create one
    """
    def wrap(request, *args, **kwargs):
        player = Player.objects.all().count()
        if player == 0:
            return function(request, *args, **kwargs)
        else:
            return redirect("/jogar")

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap


def player_created(function):
    """
    If the player is logged, he can't go back to Index
    """
    def wrap(request, *args, **kwargs):
        player = Player.objects.filter(user=2)
        if player.exists():
            return function(request, *args, **kwargs)
        else:
            return redirect("index")

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
