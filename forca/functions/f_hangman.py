import random
import requests
from faker import Faker
from unidecode import unidecode

from forca.models import Words


def generate_db():
    """
    Function to Generate words for the Hangman Game
    """
    r = requests.get('https://api.dicionario-aberto.net/random')
    data = r.json()
    pal = data['word']
    final_word = unidecode(pal)
    Words.objects.create(word=final_word)
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
    w = Words.objects.all().count()
    number = random.randint(w, w + w)  # From the Final Index to Index * 2
    word = Words.objects.get(id=number)
    return word