Read Me - Le Grand Duel

Introduction

Le Grand Duel est un jeu type RPG dans lequel deux joueurs s'affrontent avec des personnages de différentes classes (Guerrier, Barbare, Clerc). Le but du jeu est de réduire les points de vie de l'adversaire à zéro.

Structure du Projet

Le projet est construit sur un modèle MVC :

    character.py : Ce fichier contient la définition des classes de personnages, à savoir Character, Warrior, Barbarian, et Cleric.

    view.py : La classe View est définie ici pour gérer l'affichage du jeu, notamment les règles, les messages de combat, et l'annonce du gagnant.

    controller.py : La classe Controller prend en charge la logique du jeu, la création des personnages, le déroulement des tours, et la détermination du gagnant.


Classes Principales

    Character : Classe de base abstraite définissant les caractéristiques de base pour chaque personnage.

    Warrior : Classe représentant le Guerrier, avec des attaques régulières et une attaque sécurisée.

    Barbarian : Classe représentant le Barbare, capable d'entrer en mode furie ce qui déverouille une nouvelle attaque plus puissante.

    Cleric : Classe représentant le Clerc, avec la capacité de se soigner tout en infligeant des dégâts.

Bonne partie !