"""Fichier contenant le code des différentes entities du jeu kidnap the princess, ennemis, boss, ..."""

# -*-coding:utf-8-*

__author__ = 'sofamaniac'
__copyright__ = 'Copyright 2015, Antoine Grimod'
__license__ = 'GPL'
__version__ = '0.0'
__maintainer__ = 'Antoine Grimod'
__email__ = ''
__status__ = 'Production'

import pygame

from globals import *


class Entity(pygame.sprite.Sprite):
	def __init__(self, name, pv, damage, sprites, position=(0, 0, 0, 0),
				 groupe=None):
		"""__init__(self, str, int, int, dict(str, pygame.Surface), list,
		pygame.sprite.Group)"""
		# Appel du constructeur de la classe Sprite
		pygame.sprite.Sprite.__init__(self)

		self.name = name  # optionnel

		self.pv = pv  # quantite max de pv
		self.damage = damage  # damage infliges par l'attaque de base

		self.position = position
		# definit le nombre de pixel dont on doit se deplacer
		self.direction = [0, None]

		self.sprites = sprites  # differents sprites de l'animation
		self.pos_sprite = 0  # position de l'image dans le dico
		self.image = self.sprites[self.direction][self.pos_sprite]
		self.rect = self.image.get_rect()

		if groupe:
			self.add(groupe)

	def update(self, animation):

		if self.direction[0] > 0:  # le joueur veut se deplacer vers la droite
			self.position[0] -= 1
			self.direction[0] -= 1  # reduit le nb de pixel qu'il reste à faire
			return

		if self.direction[0] < 0:  # si le joueur veut se deplacer a gauche
			self.position[0] += 1
			self.direction[0] += 1  # on remet le deplacement a 0
			return

		if self.direction[1] is not None:  # si le joueur saute/tombe
			self.position[1] += self.direction[1]
			self.direction[1] += 1

		# Pour faire l'animation on veut que les images apparaissent
		# regulierement

		if animation:

			if self.pos_sprite >= len(self.sprites[self.direction]):
				self.pos_sprite = -1
			# permet d'eviter les depassement en revenant au debut

			self.image = self.sprites[self.direction][self.pos_sprite + 1]


class Joueur(Entity):
	def __init__(self, name, pv, damage, sprites, position, vies,
				 damage_spec, groupe):
		Entity.__init__(self, name, pv, damage, sprites, position, groupe)

		self.vies = vies
		self.damage_spec = damage_spec


class Ennemy(Entity):
	def __init__(self, name, pv, damage, sprites, pos_debut, pos_fin, radius):
		Entity.__init__(self, name, pv, damage, sprites, pos_debut)

		self.pos_debut = pos_debut
		self.pos_fin = pos_fin

		self.radius = radius  # radius dans lequel est detecté un joueur


class Projectile(Entity):

	def __init__(self, name, pv, damage, sprites, position, emetteur):

		Entity.__init__(self, name, pv, damage, sprites, position)
		self.emetteur = emetteur  # permet de ne pas blesser l'emetteur s'il
		#  se prend son propre projectile


def collision(pos_entity, pos_objects):
	"""fonction dectectant si un objet entre en collision avec une liste
	d'objet, s'arrete des qu'il y a collision."""
	#todo: pour collision voir pygame.masks ou pygame.sprite.Sprite
	for obstacle in pos_objects:
		if pos_entity[0] == obstacle[0] and pos_entity[1] == obstacle[1]:
			return True

	return False