"""
Modèle permettant la gestion des objets et du stockage de données
"""
from pydantic import BaseModel
from typing import List


class length_input(BaseModel):
    """
    Modèle permettant de gérer la taille des listes
    """
    length: List[int]
