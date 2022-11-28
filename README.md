# Test d'entretien Gestform 💻

Ce programme permet de traiter une liste de nombres entiers aléatoires et d'afficher : 
 - Geste, si la valeur de la liste est divisible par 3
 - Forme, si la valeur de la liste est divisible par 5
 - Gestorme, si la valeur de la liste est divisible par 3 et par 5
 - l'entier de la liste si aucune des conditions n'est remplies

Le projet est structuré en microservice depuis le framework FastApi et conteneurisé par Docker. 
 


Crée par Eric Stuhlfauth

## Requirements
  - Python : 3.11+
  - Docker : dernière version

Les dépendences suivantes devraient s'installer au travers du docker : 
  - FastAPI : dernière version 
  - Uvicorn : dernière version

## Installation 👩‍💻

1. clonez ce repository.
2. vérifiez que vous disposez bien de la version de python 3.11, dans le cas contraire rendez vous sur:

<p align="center">
[// Your content](https://www.python.org/downloads/)
</p>
	
4. dans votre nouveau repository, naviguez vers la racine du projet.
5. lancez docker desktop 
6. lancez la commande suivant à la racine de votre projet :
```console
docker build -t nom_docker_test .
```
cela va permettre d'installer les requirements et de préparer le container
5. lancez le container avec la commande :
```console
docker run -p 8080:80 nom_docker_test
```
6. retournez sur docker desktop
7. vérifiez le container a pour status "running"
8. cliquez sur le lien de la colonne port(s)


