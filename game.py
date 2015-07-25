"""Fichier contenant les codes propres a la phase de jeu"""

# -*-coding:utf-8-*

__author__ = 'sofamaniac'
__copyright__ = 'Copyright 2015, Antoine Grimod'
__license__ = 'GPL'
__version__ = '0.0'
__maintainer__ = 'Antoine Grimod'
__email__ = ''
__status__ = 'Production'

from globals_var import *
from graphics import *
import entities

def game(level):
	"""Fonction gerant la partie jeu en elle meme"""
	# Faire des raccourcis pour les listes de l'objet pour éviter level.liste

	animation = False

	player = entities.Joueur("pseudo", 0, 0, {}, (0, 0, 0, 0), 0, 0)

	scenes = level.scenes

	level_entities = level.entities

	while continuer:
		pygame.time.Clock.tick(60)  # on limite a 60 tps

		ticks += 1

		if ticks % 2 == 0:  # equivaut a 30 fps

			animation = True
			ticks = 0

		for event in pygame.event.get():
			#todo : faire gestion event
			test = 0

		#todo: gerer l'update avec les groups
		for i in level_entities:

			i.update()