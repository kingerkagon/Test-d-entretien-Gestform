"""
Fichier pricipale de lancement de l'application
"""
from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.api.random_lists import random_list

# Initialise l'appli
app = FastAPI()

# Gestion des fichiers statiques, notamment .css
app.mount("/static",
          StaticFiles(directory=Path(__file__).parent.parent.absolute() /
                      "static"),
          name="static")

# Indique le routing vers l'api
app.include_router(random_list)
