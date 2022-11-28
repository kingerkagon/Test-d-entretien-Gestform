"""_summary_

Raises:
    HTTPException: _description_
    HTTPException: _description_

Returns:
    _type_: _description_
"""

import random

from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# from app.api.models import length_input

# Génération de la liste
ma_liste = random.sample(range(-1000, 1000), 3)
random_list_db = [{'value': ma_liste}]

# Routing de l'API
random_list = APIRouter()

templates = Jinja2Templates(directory="templates")

list_length = 5


def create_random_list(list_lenght: int):
    """ Permet de créer une liste composé de nombres
    entiers compris entre -1000 et 1000

    Args:
        list_lenght (int): taille de la liste à créer
    return:
        my_liste (list): liste aléatoire
    """
    my_liste = random.sample(range(-1000, 1000), list_lenght)

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

    # Logique de traitement de la liste
    for number in list_to_parse:
        if (number % 3 == 0 and number % 5 == 0):
            result_list.append("GestForm")
        elif number % 3 == 0:
            result_list.append("Gest")
        elif number % 5 == 0:
            result_list.append("Form")
        else:
            result_list.append(str(number))

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


# @random_list.post('/', status_code=201)
# async def add_list(payload: length_input):
#     """_summary_

#     Args:
#         payload (RandomList): _description_

#     Returns:
#         _type_: _description_
#     """
#     list_length = 69

#     return {'length': list_length}

# @random_list.post('/', status_code=201)
# async def add_list(payload: RandomList):
#     """_summary_

#     Args:
#         payload (RandomList): _description_

#     Returns:
#         _type_: _description_
#     """
#     list_length
#     random_list_db.append(random_list)
#     return {'id': len(random_list_db) - 1}

# @random_list.put('/{id}')
# async def update_list(id: int, payload: RandomList):
#     """_summary_

#     Args:
#         id (int): _description_
#         payload (RandomList): _description_

#     Raises:
#         HTTPException: _description_

#     Returns:
#         _type_: _description_
#     """
#     random_list = payload.dict()
#     random_list_length = len(random_list_db)
#     if 0 <= id <= random_list_length:
#         random_list_db[id] = random_list
#         return None

#     raise HTTPException(
#         status_code=404,
#         detail=f"La liste portant l'id : {id} n a pas été trouvé")

# @random_list.delete('/{id}')
# async def delete_list(id: int):
#     """_summary_

#     Args:
#         id (int): _description_

#     Raises:
#         HTTPException: _description_

#     Returns:
#         _type_: _description_
#     """
#     random_list_length = len(random_list_db)

#     if 0 <= id <= random_list_length:
#         del random_list_db[id]
#         return None

#     raise HTTPException(
#         status_code=404,
#         detail=(f"La liste portant l'id : {id} n a pas été trouvé"))
