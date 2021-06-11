import pygame as pg
import random
from settings import *
from os import path

game_folder = path.dirname(__file__)
img_folder = path.join(game_folder, 'img')

class Cube2(pg.sprite.Sprite):
	def __init__(self, game, image, x, y):
		self.groups = game.all_sprites, game.cubes
		self._layer = 8
		pg.sprite.Sprite.__init__(self, self.groups)
		self.game = game
		self.image = image
		#self.image = pg.Surface((TILESIZE, TILESIZE))
		#self.image.fill(PURPLE)
		self.rect = self.image.get_rect()
		self.clicked = False
		self.original_coords = [0, 1]
		self.active_tile = True
		self.x = x
		self.y = y
		self.rect.x = x * TILESIZE
		self.rect.y = y * TILESIZE

		# Testing for collison detection
		self.cube_list = game.cube_list
		self.cube_list.append([self.x, self.y])

	def move(self, dx, dy, ix, iy):
		if not self.collide_with_cubes(ix, iy):
			self.rect.x = dx
			self.rect.y = dy
			self.cube_list.remove([self.x, self.y])
			self.x = ix
			self.y = iy
			self.cube_list.append([self.x, self.y])




	def collide_with_cubes(self, ix, iy):
		if ([ix, iy] in self.cube_list):
		# for cube in self.game.all_sprites:
		# 	if cube.x == self.x + dx and cube.y == self.y + dy:
		# 		print(f'self.x = {self.x} , self.y = {self.y}, dx = {dx}, dy = {dy}')
		# 		print(f'cube.x = {cube.x} , cube.y = {cube.y}')
		# 		#print('Cant go there!')
				return True
class Traitor(pg.sprite.Sprite):
	def __init__(self, game, tile_type, tiles, x, y):
		self._layer = 3
		self.groups = game.all_sprites, game.cubes
		pg.sprite.Sprite.__init__(self, self.groups)
		self.game = game
		self.tile_type = tile_type
		self.tiles = tiles
		self.image = tiles[tile_type][1]
		self.rect = self.image.get_rect()
		self.x = x
		self.y = y
		self.rect.x = x * TILESIZE
		self.rect.y = y * TILESIZE



class Tile(pg.sprite.Sprite):
	def __init__(self, game, tile_type, names, tiles, first_tile, board_info, formation_board, x, y):
		self._layer = 3
		self.groups = game.all_sprites, game.cubes
		pg.sprite.Sprite.__init__(self, self.groups)
		self.game = game
		self.names = names
		self.tiles = tiles
		self.tile_type = tile_type
		# Is this the first tile to be placed?
		self.first_tile = first_tile
		self.board_info = board_info
		self.formation_board = formation_board
		self.image = tiles[tile_type][1]
		self.type = tiles[tile_type][2]
		self.shape = tiles[tile_type][3]
		self.indicator = tiles[tile_type][4]
		self.rect = self.image.get_rect()
		self.original_coords = [0, 1]
		self.active_tile = True
		self.x = x
		self.y = y
		self.rect.x = x * TILESIZE
		self.rect.y = y * TILESIZE

		# Testing for collison detection
		self.cube_list = game.cube_list
		self.cube_list.append([self.x, self.y])


	def move(self, dx, dy, ix, iy):
		if not self.collide_with_cubes(ix, iy):
			self.rect.x = dx
			self.rect.y = dy
			self.cube_list.remove([self.x, self.y])
			self.x = ix
			self.y = iy
			self.cube_list.append([self.x, self.y])


	def collide_with_cubes(self, ix, iy):
		# If the coordinates that I want to move my tile to already exist in cube_list, return True
		# If iy = 9, which is beyond the screen, return True
		# True because the move() function checks to see if not collide_with_cubes
		if ([ix, iy] in self.cube_list) or iy == 9:
			return True

	def valid_placement(self, ix, iy, second_ordeal_success):
		if self.first_tile == True:
			# If first tile
			if iy != 8:
				self.rect.x = 0
				self.rect.y = 0
			else:
				if ix >= 3 and ix < 9:
					return True
				else:
					self.rect.x = 0
					self.rect.y = 0
		else:

			if second_ordeal_success == False:

				if iy >= 3:
					#print('THIS IS FALSE!!!')

					if ([ix, iy]) == ([ix, 8]) and (ix >=3 and ix < 9):
						# If there is a tile one space to the left or right of your tile, return True
						if ([ix+1, iy] in self.cube_list) or ([ix-1, iy] in self.cube_list):
							return True
						else:
							self.rect.x = 0
							self.rect.y = 2
					# This is where you will need to figure out the shapes
					# Remember, board_info = [x, y] : [tile_type, shape]
					elif ([ix, iy+1] in self.cube_list):
						# Okay, this checks if there is a tile below, to the left or to the right that is equal in shape to the one being placed.
						if (ix, iy+1) in self.board_info or (ix-1, iy) in self.board_info or (ix, iy+1) in self.board_info or (ix, iy-1) in self.board_info:
							if self.board_info[ix, iy+1][1] == self.shape or ((ix+1, iy) in self.board_info and self.board_info[ix+1, iy][1] == self.shape) or ((ix-1, iy) in self.board_info and self.board_info[ix-1, iy][1] == self.shape):
								#print('There is an adjacent tile')
								# if (ix+1, iy) in self.board_info:
								# 	print('key exists')
								self.rect.x = 0
								self.rect.y = 2
								return False
							#print('Valid as a tile is below this')
							return True


					else:
						#print('I dont think so')
						self.rect.x = 0
						# Can't seem to get this to actually appear at y = 2
						self.rect.y = 2

				else:
					self.rect.x = 0
					self.rect.y = 2

			elif second_ordeal_success == True:
				#print('THIS IS TRUE!!!!')
				if iy >= 2:
					if ([ix, iy]) == ([ix, 8]) and (ix >=3 and ix < 9):
					# If there is a tile one space to the left or right of your tile, return True
						if ([ix+1, iy] in self.cube_list) or ([ix-1, iy] in self.cube_list):
							return True
						else:
							self.rect.x = 0
							self.rect.y = 2
					# This is where you will need to figure out the shapes
					# Remember, board_info = [x, y] : [tile_type, shape]
					elif ([ix, iy+1] in self.cube_list):
						# Okay, this checks if there is a tile below, to the left or to the right that is equal in shape to the one being placed.
						if (ix, iy+1) in self.board_info or (ix-1, iy) in self.board_info or (ix, iy+1) in self.board_info or (ix, iy-1) in self.board_info:
							if self.board_info[ix, iy+1][1] == self.shape or ((ix+1, iy) in self.board_info and self.board_info[ix+1, iy][1] == self.shape) or ((ix-1, iy) in self.board_info and self.board_info[ix-1, iy][1] == self.shape):
								#print('There is an adjacent tile')
								# if (ix+1, iy) in self.board_info:
								# 	print('key exists')
								self.rect.x = 0
								self.rect.y = 2
								return False
							#print('Valid as a tile is below this')
							return True

					else:
						#print('I dont thik so')
						self.rect.x = 0
						# Can't seem to get this to actually appear at y = 2
						self.rect.y = 2

				else:
					self.rect.x = 0
					self.rect.y = 2



			else:
				#print('This is triggering')
				self.rect.x = 0
				self.rect.y = 2


class Minion(pg.sprite.Sprite):
	def __init__(self, game, image, x, y):

		self.death1 = pg.image.load(path.join(img_folder, DEATH1)).convert_alpha()
		self.death2 = pg.image.load(path.join(img_folder, DEATH2)).convert_alpha()
		self.death3 = pg.image.load(path.join(img_folder, DEATH3)).convert_alpha()
		self.death4 = pg.image.load(path.join(img_folder, DEATH4)).convert_alpha()

		self.animate = [self.death1, self.death2, self.death3, self.death4]


		self._layer = 10
		self.groups = game.all_sprites, game.minions
		pg.sprite.Sprite.__init__(self, self.groups)

		self.game = game
		self.image_orig = image
		self.image = self.image_orig.copy()
		self.rect = self.image.get_rect()
		self.last_update = pg.time.get_ticks()
		self.rot = 0
		self.rot_speed = random.randrange(-8, 8)
		self.clicked = False
		self.x = x
		self.y = y
		self.rect.x = x * 10
		self.rect.y = y * 10

		# Test for animation
		self.animation_count = 0
		self.animation_frames = 10
		self.animation = False

	def start_animation(self):
		self.animation = True

	def rotate(self):
		now = pg.time.get_ticks()
		if now - self.last_update > 80:
			self.last_update = now


			self.rot = (self.rot + self.rot_speed) % 20

			#print(self.rot)

			new_image = pg.transform.rotate(self.image_orig, self.rot)
			old_center = self.rect.center
			self.image = new_image
			self.rect = self.image.get_rect()
			self.rect.center = old_center

	def update(self):
		self.rotate()
		if self.animation:
			#print('ANIMATION!')
			image_index = self.animation_count // self.animation_frames
			self.animation_count += 1

			if image_index < len(self.animate):
				self.image = self.animate[image_index]
				self.rect = self.image.get_rect(center = self.rect.center)


			else:
				self.kill()



class Defence(pg.sprite.Sprite):
	def __init__(self, game, image, x, y):
		self._layer = 10
		self.groups = game.all_sprites, game.defences
		pg.sprite.Sprite.__init__(self, self.groups)

		self.game = game
		self.image = image
		self.rect = self.image.get_rect()
		self.x = x
		self.y = y
		self.rect.x = x * 10
		self.rect.y = y * 10
		self.last_update = 0
		# This is for movement
		self.vx = 1



	def update(self):
		# This is for movement
		#now = pg.time.get_ticks()
		#if now - self.last_update > 90:
		#	self.last_update = now

		self.rect.x -= self.vx


class Window(pg.sprite.Sprite):
	def __init__(self, game, image, x, y):
		self._layer = 10
		self.groups = game.all_sprites, game.windows
		pg.sprite.Sprite.__init__(self, self.groups)
		self.game = game
		self.image = image
		self.rect = self.image.get_rect()
		self.x = x
		self.y = y
		self.rect.x = x
		self.rect.y = y

class Window2(pg.sprite.Sprite):
	def __init__(self, game, image, x, y):
		self._layer = 9
		self.groups = game.all_sprites, game.windows
		pg.sprite.Sprite.__init__(self, self.groups)
		self.game = game
		self.image = image
		self.rect = self.image.get_rect()
		self.x = x
		self.y = y
		self.rect.x = x
		self.rect.y = y

class Bars(pg.sprite.Sprite):
	def __init__(self, game, image, x, y):
		self._layer = 2.5
		self.groups = game.all_sprites, game.bars
		pg.sprite.Sprite.__init__(self, self.groups)
		self.game = game
		self.image = image
		self.rect = self.image.get_rect()
		self.x = x
		self.y = y
		self.rect.x = x
		self.rect.y = y



class Scroll(pg.sprite.Sprite):
	def __init__(self, game, image, x, y, speed):
		self._layer = 9.5
		self.groups = game.all_sprites, game.scrolls
		pg.sprite.Sprite.__init__(self, self.groups)
		self.game = game
		self.image = image
		self.rect = self.image.get_rect()
		self.last_update = 0

		self.x = x
		self.y = y
		self.rect.x = x
		self.rect.y = y
		# This is for movement
		self.velx = speed

	def update(self):
		# This is for movement
		now = pg.time.get_ticks()
		if now - self.last_update > 90:
			self.last_update = now

			self.rect.x -= 1


class Black(pg.sprite.Sprite):
	def __init__(self, game, image, x, y):
		self._layer = 5
		self.groups = game.all_sprites, game.bars
		pg.sprite.Sprite.__init__(self, self.groups)
		self.game = game
		self.image = image
		self.rect = self.image.get_rect()
		self.x = x
		self.y = y
		self.rect.x = x
		self.rect.y = y

class Slash(pg.sprite.Sprite):
	def __init__(self, game, image, x, y):
		self._layer = 4
		self.groups = game.all_sprites
		pg.sprite.Sprite.__init__(self, self.groups)
		self.game = game
		self.image = image
		self.rect = self.image.get_rect()
		self.x = x
		self.y = y
		self.rect.x = x * TILESIZE
		self.rect.y = y * TILESIZE
