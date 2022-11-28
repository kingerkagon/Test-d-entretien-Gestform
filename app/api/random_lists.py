"""
Api permettant la gestion des listes et le traitement en chaine de caractères
"""

import random

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.api.models import length_input

# Génération de la liste
ma_liste = random.sample(range(-1000, 1000), 3)
random_list_db = [{'value': ma_liste}]

# Routing de l'API
random_list = APIRouter()

# indique où trouver les ressources html
templates = Jinja2Templates(directory="templates")

# Taille de la liste standard
list_length = [20]


def create_random_list(list_lenght: list):
    """ Permet de créer une liste composé de nombres
    entiers compris entre -1000 et 1000

    Args:
        list_lenght (int): taille de la liste à créer
    return:
        my_liste (list): liste aléatoire
    """
    try:
        my_liste = random.sample(range(-1000, 1000), list_lenght[0])
    except TypeError:
        my_liste = [0]

    return my_liste


def parse_list_data(list_to_parse: list):
    """Traite une liste et pour retourner une liste composé
    de chaines de charactère en fonction de la valeur de la liste

    Args:
        list_to_parse (list): liste de nombres entiers aléatoire à traiter

    Returns:
        result_list (list) : liste d'output composé de strings
    """
    result_list = []

    if list_to_parse is None:
        result_list = ["La liste d'entrée est vide"]
    else:
        # Logique de traitement de la liste
        for number in list_to_parse:
            try:
                if (number % 3 == 0 and number % 5 == 0):
                    result_list.append("GestForm")
                elif number % 3 == 0:
                    result_list.append("Gest")
                elif number % 5 == 0:
                    result_list.append("Form")
                else:
                    result_list.append(str(number))
            except TypeError:
                result_list.append("-/-")

    return result_list


@random_list.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """ Requête html permettant de communiquer entre le model et l'interface

    Returns:
        random_list_data (list) : données d'entrées,
        output_list (list) : données traités
    """
    # Création de la liste aléatoire
    input_list_data = create_random_list(list_length)

    # Traitement de la liste aléatoire
    output_list = parse_list_data(input_list_data)

    return templates.TemplateResponse("index.html",
                                      context={
                                          "request": request,
                                          "random_list_data": input_list_data,
                                          "output_list": output_list
                                      })


@random_list.post('/', status_code=201)
async def add_list(payload: length_input):
    """Permet d'ajouter une ligne à la liste

    Returns:
        string : affiche la nouvelle taille de la liste
    """
    list_length[0] += 1

    return {'length': list_length}
