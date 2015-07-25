"""Fichier contenant les variables globales a tout le programme"""

# -*-coding:utf-8-*

__author__ = 'sofamaniac'
__copyright__ = 'Copyright 2015, Antoine Grimod'
__license__ = 'GPL'
__version__ = '0.0'
__maintainer__ = 'Antoine Grimod'
__email__ = ''
__status__ = 'Production'

from pygame.locals import *

game_speed = 60  # definit le nombre de tours/seconde de la boucle principale
screen_speed = 30  # definit le nombre d'image par seconde

ticks = 0  # Définti un temps universel pour tout le programme

continuer = True  # permet de savoir si l'on continue le jeu ou pas

taille_case = 0  # todo a determiner en fonction de l'image d'une case
				# le faire avec une fonction

controls = {[0, taille_case * 2] : K_UP,
			[taille_case, 0] : K_RIGHT,
			[-taille_case] : K_LEFT,
			"attack" : K_z,
			"spec" : K_e}