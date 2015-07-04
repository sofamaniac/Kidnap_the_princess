"""Fichier contenant les codes propres a la partie graphique du jeu"""

# -*-coding:utf-8-*

__author__ = 'sofamaniac'
__copyright__ = 'Copyright 2015, Antoine Grimod'
__license__ = 'GPL'
__version__ = '0.0'
__maintainer__ = 'Antoine Grimod'
__email__ = ''
__status__ = 'Production'

import pygame
from pygame.locals import *

pygame.init()


def create_window(taille, titre, logo):

	window = pygame.display.set_mode(taille)
	window.set_caption(titre)
	window.set_icon(logo)

	return window


def load_image(path):
	return pygame.image.load(path).convert_alpha()


def load_sound(path):
	return pygame.mixer.Sound(path)


def text_to_sprite(text, size):
	"""Transform a text into sprite"""
	font = pygame.font.Font(None, size)
	sprite = font.render(text, 1, (255, 255, 255))

	return sprite


def create_susfrace(image, line, colonnes):
	"""Fonction permettant de creer des subsurface egales a partir d'une image, du nb de ligne et du nombre de colonne"""
	width = image.get_width() / line
	height = image.get_height() / colonnes

	subsurfaces = []

	for x in range(line):
		for y in range(colonnes):
			subsurfaces.append(image.subsurface(width * x, height * y))

	return subsurfaces


def scroll():

	return


class InputBox:

	def __init__(self, surface, couleur, taille, txt, pos):

		self.box = (surface, couleur, taille)
		self.txt = txt
		self.pos = pos

		self.current_event = None

	def get_char(self):

		self.current_event = False

		while not self.current_event:

			self.current_event = pygame.event.wait()

			if self.current_event.type != KEYDOWN:
				self.current_event = False


def update(surface, elements, coords):
	"""Fonction mettant a jour une surface en blittant les element aux coordonnees donnees.
	Attend 2 list. Si les deux listes non pas la meme taille, return -1"""

	if len(elements) == len(coords):  # on verifie que les deux listes aient la meme taille

		for i in range(len(elements)):

			surface.blit(elements[i], coords[i])

		pygame.display.flip()

		return 0

	else:
		return -1