"""Fichier contenant tout ce qui concerne les niveaux et les tableaux de chaque niveau"""

# -*-coding:utf-8-*

__author__ = 'sofamaniac'
__copyright__ = 'Copyright 2015, Antoine Grimod'
__license__ = 'GPL'
__version__ = '0.0'
__maintainer__ = 'Antoine Grimod'
__email__ = ''
__status__ = 'Production'


class Level:

	def __init__(self, name):

		self.name = name  # contient le nom du niveau ainsi que son world sous la forme World.Level

		self.scenes = []  # contient les differentes scene du niveau


class Scene:

	def __init__(self, coords):

		self.coords = coords  # defintit la poisition de la scene dans le niveau

		self.background = 0  # contiendra le backgroud de la scene

		self.wall = []  # continedra les murs du niveau et les espaces vides

		self.entities = []  # Contiendra les différentes entités de la scène