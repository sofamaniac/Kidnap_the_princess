"""Fichier contenant les codes propres a la phase de jeu"""

# -*-coding:utf-8-*

__author__ = 'sofamaniac'
__copyright__ = 'Copyright 2015, Antoine Grimod'
__license__ = 'GPL'
__version__ = '0.0'
__maintainer__ = 'Antoine Grimod'
__email__ = ''
__status__ = 'Production'

from globals import *
from graphics import *
import entities

def game(level):
	"""Fonction gerant la partie jeu en elle meme"""
	# Faire des raccourcis pour les différentes listes de l'objet pour éviter level.liste

	player = entities.Joueur("pseudo", 0, 0, {}, (0, 0, 0), 0, 0)

	scenes = level.scenes

	while continuer:

		ticks += 1

		if ticks % 30 == 0:

			#faire affichage
			ticks = 0