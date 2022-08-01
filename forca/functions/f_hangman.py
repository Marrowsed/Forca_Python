import random
import requests
from faker import Faker
from unidecode import unidecode

from forca.models import Words


def generate_word():
    """
    Function to Generate words for the Hangman Game
    """
    r = requests.get('https://api.dicionario-aberto.net/random')
    data = r.json()
    pal = data['word']
    final_word = unidecode(pal)
    return Words.objects.create(word=final_word)
    """
    fake = Faker('pt_BR')
    Faker.seed(0)
    for _ in range(10):
        pal = fake.safe_color_name()
        state = fake.estado_nome()
        Words.objects.create(word=pal)
        Words.objects.create(word=state)
    """

def randomize_word():
    """
    Randomize words from db
    """
    word = generate_word()
    print(word)
    w = Words.objects.get(word=word)
    final_word = Words.objects.get(id=w.id)
    print(final_word)
    return final_word

def generate_hang(word):
    """
    Generate the "_"
    """
    blank = []
    for _ in list(word):
        if _ == "-" or _ == " ":
            blank.append(_)
        else:
            blank.append("_")
    return blank