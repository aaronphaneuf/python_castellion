import threading
import webbrowser
import os
import random
import sys
import pygame as pg
import numpy as np
from os import path
from settings import *
from sprites import *
from functions import *
from randcode import *

class Game:
	def __init__(self):
		self.screen = pg.display.set_mode((WIDTH, HEIGHT))
		pg.display.set_caption(TITLE)
		self.clock = pg.time.Clock()
		pg.key.set_repeat(500, 100)
		pg.mixer.init()
		self.load_data()

	def load_data(self):
		# Create a df containing saved wins and losses
		self.df2 = create_dfs()
		create_pi(self.df2)
		self.df2['Wins'][0] += 1
		self.f = open('stats.html','w')
		self.message = ("""
		<html>
		<head>
		<title>'Castellion Stats'</title>
		<link rel="stylesheet" type="text/css"
		href="style.css" />
		</head>
		<body>
		<div class="container">
		<div class="grid-item item-1"><img src="logo.png">
		<br><h1>Castellion Stats</h1></div>
		<div class="grid-item item-15">
		<h1>Castellion Stats</h1></div>
		<div class="grid-item item-2"><h1>
		"""+str(self.df2['Games'][0])+
		"""</h1><h2>Games Played</h2></div>
		<div class="grid-item item-3">
		<img src="piechart.png"></div>
		<div class="grid-item item-4"><h1>
		""" +str(self.df2['Wins'][0])+
		"""</h1><h2>Victories</h2></div>
		<div class="grid-item item-5">Calendar Heatmap<br>
		<br><img src="heatmap.png"></div>
		</div>
		</body>
		</html>""")
		self.f.write(self.message)
		self.f.close()


		# Declare game folder
		game_folder = path.dirname(__file__)
		img_folder = path.join(game_folder, 'img')

		# Load ordeal cards
		self.ordeal1 = pg.image.load(
			path.join(img_folder, CARD1)).convert_alpha()
		self.ordeal2 = pg.image.load(
			path.join(img_folder, CARD2)).convert_alpha()
		self.ordeal3_1 = pg.image.load(
			path.join(img_folder, CARD3_1)).convert_alpha()
		self.ordeal3_2 = pg.image.load(
			path.join(img_folder, CARD3_2)).convert_alpha()
		self.ordeal3_3 = pg.image.load(
			path.join(img_folder, CARD3_3)).convert_alpha()

		# Load main image and logo
		self.new_border = pg.image.load(
			path.join(img_folder, NEW_BORDER)).convert_alpha()
		self.castellion = pg.image.load(
			path.join(img_folder, MAIN)).convert_alpha()

		# load tiles
		self.traitor_tile = pg.image.load(
			path.join(img_folder, TRAITOR_TILE)).convert_alpha()
		self.chameleon_square = pg.image.load(
			path.join(img_folder, CHAMELEON_SQUARE)).convert_alpha()
		self.chameleon_circle = pg.image.load(
			path.join(img_folder, CHAMELEON_CIRCLE)).convert_alpha()
		self.chameleon_triangle = pg.image.load(
			path.join(img_folder, CHAMELEON_TRIANGLE)).convert_alpha()
		self.seer_square = pg.image.load(
			path.join(img_folder, SEER_SQUARE)).convert_alpha()
		self.seer_circle = pg.image.load(
			path.join(img_folder, SEER_CIRCLE)).convert_alpha()
		self.seer_triangle = pg.image.load(
			path.join(img_folder, SEER_TRIANGLE)).convert_alpha()
		self.pyro_square = pg.image.load(
			path.join(img_folder, PYRO_SQUARE)).convert_alpha()
		self.pyro_circle = pg.image.load(
			path.join(img_folder, PYRO_CIRCLE)).convert_alpha()
		self.pyro_triangle = pg.image.load(
			path.join(img_folder, PYRO_TRIANGLE)).convert_alpha()
		self.juggler_square = pg.image.load(
			path.join(img_folder, JUGGLER_SQUARE)).convert_alpha()
		self.juggler_circle = pg.image.load(
			path.join(img_folder, JUGGLER_CIRCLE)).convert_alpha()
		self.juggler_triangle = pg.image.load(
			path.join(img_folder, JUGGLER_TRIANGLE)).convert_alpha()

		# Load dream tiles
		self.dream_chameleon_square = pg.image.load(
			path.join(img_folder, DREAM_CHAMELEON_SQUARE)).convert_alpha()
		self.dream_chameleon_circle = pg.image.load(
			path.join(img_folder, DREAM_CHAMELEON_CIRCLE)).convert_alpha()
		self.dream_chameleon_triangle = pg.image.load(
			path.join(img_folder, DREAM_CHAMELEON_TRIANGLE)).convert_alpha()
		self.dream_seer_square = pg.image.load(
			path.join(img_folder, DREAM_SEER_SQUARE)).convert_alpha()
		self.dream_seer_circle = pg.image.load(
			path.join(img_folder, DREAM_SEER_CIRCLE)).convert_alpha()
		self.dream_seer_triangle = pg.image.load(
			path.join(img_folder, DREAM_SEER_TRIANGLE)).convert_alpha()
		self.dream_pyro_square = pg.image.load(
			path.join(img_folder, DREAM_PYRO_SQUARE)).convert_alpha()
		self.dream_pyro_circle = pg.image.load(
			path.join(img_folder, DREAM_PYRO_CIRCLE)).convert_alpha()
		self.dream_pyro_triangle = pg.image.load(
			path.join(img_folder, DREAM_PYRO_TRIANGLE)).convert_alpha()
		self.dream_juggler_square = pg.image.load(
			path.join(img_folder, DREAM_JUGGLER_SQUARE)).convert_alpha()
		self.dream_juggler_circle = pg.image.load(
			path.join(img_folder, DREAM_JUGGLER_CIRCLE)).convert_alpha()
		self.dream_juggler_triangle = pg.image.load(
			path.join(img_folder, DREAM_JUGGLER_TRIANGLE)).convert_alpha()

		# Load window images for ordeal
		self.window = pg.image.load(
			path.join(img_folder, WINDOW)).convert_alpha()
		self.window2 = pg.image.load(
			path.join(img_folder, WINDOW2)).convert_alpha()
		self.scroll = pg.image.load(
			path.join(img_folder, SCROLL)).convert_alpha()

		# Load minion images
		self.minion1 = pg.image.load(
			path.join(img_folder, MINION)).convert_alpha()
		self.minion2 = pg.image.load(
			path.join(img_folder, MINION2)).convert_alpha()
		self.minion3 = pg.image.load(
			path.join(img_folder, MINION3)).convert_alpha()

		# Load defences images
		self.tower = pg.image.load(
			path.join(img_folder, TOWER)).convert_alpha()
		self.line = pg.image.load(
			path.join(img_folder, LINE)).convert_alpha()
		self.bastion = pg.image.load(
			path.join(img_folder, BASTION)).convert_alpha()

		# Load button images
		self.draw_button = pg.image.load(
			path.join(img_folder, DRAW_BUTTON)).convert_alpha()
		self.discard_button = pg.image.load(
			path.join(img_folder, DISCARD_BUTTON)).convert_alpha()
		self.dream_tile_button = pg.image.load(
			path.join(img_folder, DREAM_TILE_BUTTON)).convert_alpha()
		self.ordeal_button = pg.image.load(
			path.join(img_folder, ORDEAL_BUTTON)).convert_alpha()
		self.restart_button = pg.image.load(
			path.join(img_folder, RESTART_BUTTON)).convert_alpha()
		self.quit_button = pg.image.load(
			path.join(img_folder, QUIT_BUTTON)).convert_alpha()
		self.home_button = pg.image.load(
			path.join(img_folder, HOME_BUTTON)).convert_alpha()
		self.stats_button = pg.image.load(
			path.join(img_folder, STATS_BUTTON)).convert_alpha()

		# Load slash image
		self.slash = pg.image.load(
			path.join(img_folder, SLASH)).convert_alpha()

		self.game_over = False


	def new(self):
		#determine the third ordeal card
		self.third_ordeal_list = [
			self.ordeal3_1, self.ordeal3_2, self.ordeal3_3]
		self.third_ordeal_nums = [0, 1, 2]
		self.third_ordeal_choice = random.choice(self.third_ordeal_nums)
		# bastions, towers, lines
		self.third_ordeal_dict = {0: [12, 0, 8], 1: [0, 8, 12], 2: [8, 12, 0]}
		self.dream_counter = 12
		self.tiles_remaining = 71

		# Set this to False for final game
		self.second_ordeal_success = False
		self.third_ordeal_success = False
		self.force_ordeal = 0
		self.force_ordeal_check = 0

		# For the purpose of this board the numbers will assign to:
		# 1 = seer, 2 = chameleon, 3 = pyro, 4 = juggler
		self.formation_board = np.zeros((9,9))
		self.traitors_y = 3
		self.traitors_x = 9
		self.traitor_count = 0
		self.no_more_tiles = False

		self.names = ['seer_triangle', 'seer_circle', 'seer_square',
					  'chameleon_square', 'chameleon_triangle',
					  'chameleon_circle', 'pyro_triangle', 'pyro_square',
					  'pyro_circle', 'juggler_square', 'juggler_circle',
					  'juggler_triangle', 'traitor']

		self.dream_names = ['seer_triangle', 'seer_circle', 'seer_square',
							'chameleon_square', 'chameleon_triangle',
							'chameleon_circle', 'pyro_triangle', 'pyro_square',
							'pyro_circle', 'juggler_square', 'juggler_circle',
							'juggler_triangle']

		self.dream_tiles = {'seer_triangle' :
						        [1, self.dream_seer_triangle, 'seer',
							    'triangle', 1],
							'seer_circle' :
						   	    [1, self.dream_seer_circle,
								 'seer', 'circle', 1],
		 					'seer_square' :
								[1, self.dream_seer_square, 'seer',
								 'square', 1],
							'chameleon_circle' :
								[1, self.dream_chameleon_circle,
								 'chameleon', 'circle', 2],
		 					'chameleon_triangle' :
								[1, self.dream_chameleon_triangle,
								 'chameleon', 'triangle', 2],
							'chameleon_square' :
								[1, self.dream_chameleon_square, 'chameleon',
								 'square', 2],
		 					'pyro_square' :
								[1, self.dream_pyro_square, 'pyro',
								 'square', 3],
							'pyro_circle' :
								[1, self.dream_pyro_circle,
								 'pyro', 'circle', 3],
		 					'pyro_triangle' :
							 	[1, self.dream_pyro_triangle,
								 'pyro', 'triangle', 3],
							'juggler_square' :
								[1, self.dream_juggler_square, 'juggler',
								 'square', 4],
		 					'juggler_circle' :
							 	[1, self.dream_juggler_circle, 'juggler',
								 'circle', 4],
							'juggler_triangle' :
								[1, self.dream_juggler_triangle, 'juggler',
								 'triangle', 4]}

		self.tiles = {'seer_triangle' :
					      [6, self.seer_triangle, 'seer', 'triangle', 1],
					  'seer_circle' :
					      [6, self.seer_circle, 'seer', 'circle', 1],
		 			  'seer_square' :
					      [6, self.seer_square, 'seer', 'square', 1],
					  'chameleon_circle' :
					      [6, self.chameleon_circle, 'chameleon', 'circle', 2],
		 			  'chameleon_triangle' :
					  	  [6, self.chameleon_triangle, 'chameleon',
						   'triangle', 2],
					  'chameleon_square' :
					      [6, self.chameleon_square, 'chameleon', 'square', 2],
		 			  'pyro_square' :
					  	  [6, self.pyro_square, 'pyro', 'square', 3],
					  'pyro_circle' :
					  	  [6, self.pyro_circle, 'pyro', 'circle', 3],
		 			  'pyro_triangle' :
					  	  [6, self.pyro_triangle, 'pyro', 'triangle', 3],
					  'juggler_square' :
					  	  [6, self.juggler_square, 'juggler', 'square', 4],
		 			  'juggler_circle' :
					  	  [6, self.juggler_circle, 'juggler', 'circle', 4],
					  'juggler_triangle' :
					  	  [6, self.juggler_triangle, 'juggler', 'triangle', 4],
		 			  'traitor':
					      [12, self.traitor_tile, 'traitor'] }

		# This is to track where all your tiles are
		self.board_info = {}

		# Declare groups
		self.all_sprites = pg.sprite.Group()
		self.all_sprites = pg.sprite.LayeredUpdates()
		self.cubes = pg.sprite.Group()
		self.minions = pg.sprite.Group()
		self.defences = pg.sprite.Group()
		self.windows = pg.sprite.Group()
		self.bars = pg.sprite.Group()
		self.scrolls = pg.sprite.Group()

		# Assigning a list for collison detection
		self.cube_list = []

		# Spawn a test cube2 until I determine my buttons
		self.draw_tile_button = Cube2(self, self.draw_button, 0.4, 2.5)
		self.discard_tile_button = Cube2(self, self.discard_button, 1.52, 2.5)
		self.dream_tile_button2 = Cube2(self, self.dream_tile_button, 0.4, 2.81)
		self.ordeal_button2 = Cube2(self, self.ordeal_button, 1.52, 2.81)
		self.restart_button2 = Cube2(self, self.restart_button, 0.4, 3.12)
		self.quit_button2 = Cube2(self, self.quit_button, 1.52, 3.12)
		self.stats_button2 = Cube2(self, self.stats_button, 0.4, 3.42 )

		self.random_choice = random.choice(self.names)
		self.true_or_false = True
		while self.true_or_false:
			self.random_choice = random.choice(self.names)
			if self.random_choice != 'traitor':
				self.tile1 = Tile(self, self.random_choice, self.names,
								  self.tiles, True, self.board_info,
								  self.formation_board, 1,1)
				self.true_or_false = False

		self.left_button = 0
		self.current_image = None
		self.image_released = None

		# Main logo and top bar
		self.new_border_background = Bars(self, self.new_border, 0, 0)
		#self.top_bar_background = Bars(self, self.top_bar, 270, 0)
		self.castellion_logo = Bars(self, self.castellion, 340, 50)

		self.ordeal1_imgae = Bars(self, self.ordeal1, 810, 90)
		self.ordeal2_image = Bars(self, self.ordeal2, 900, 90)
		self.ordeal3_image = Bars(self,
								  self.third_ordeal_list[
								      self.third_ordeal_choice], 990, 90)

	def run(self):
		self.playing = True
		while self.playing:
			self.dt = self.clock.tick(FPS) / 1000
			self.events()
			self.update()
			self.draw()

	def quit(self):
		pg.quit()
		sys.exit()

	def update(self):
		self.all_sprites.update()

		# Check to see if a defence collides with a minion
		hits = pg.sprite.groupcollide(self.minions, self.defences, False, False)
		counter = 0

		if ((self.traitor_count >= 5 and self.traitor_count <=7)
		     or self.force_ordeal == 1):
			if (self.bastion_sum >= 4 and self.tower_sum >= 4
			    and self.line_sum >= 4):
				for hit in hits:
					if self.def1.rect.x == 375:
						self.min1.start_animation()
						self.min4.start_animation()
						self.min8.start_animation()
					if self.def2.rect.x == 359:
						self.min3.start_animation()
						self.min5.start_animation()
						self.min7.start_animation()
					if self.def3.rect.x == 359:
						self.min2.start_animation()
						self.min6.start_animation()
						self.min9.start_animation()

						def time_func():
							self.def1.kill()
							self.def2.kill()
							self.def3.kill()
							self.window1.kill()
							self.window2_1.kill()
							self.scroll1.kill()
							self.fade_to_black.kill()
							self.fade_to_black2.kill()
							self.fade_to_black3.kill()
							self.fade_to_black4.kill()
						timer = threading.Timer(2.0, time_func)
						timer.start()
			else:
				self.playing = False

		if self.traitor_count == 12 or self.force_ordeal_check >=2:
			if (self.bastion_sum >= self.third_ordeal_dict
			[self.third_ordeal_choice][0] and self.tower_sum >=
			self.third_ordeal_dict[self.third_ordeal_choice][1] and
			self.line_sum >= self.third_ordeal_dict[
			self.third_ordeal_choice][2]):
				for hit in hits:
					if self.def1.rect.x == 375:
						self.min1.start_animation()
						self.min4.start_animation()
						self.min8.start_animation()
					if self.def2.rect.x == 359:
						self.min3.start_animation()
						self.min5.start_animation()
						self.min7.start_animation()
					if self.def3.rect.x == 359:
						self.min2.start_animation()
						self.min6.start_animation()
						self.min9.start_animation()

						def time_func():
							self.def1.kill()
							self.def2.kill()
							self.def3.kill()
							self.window1.kill()
							self.scroll1.kill()
							self.fade_to_black.kill()
							self.fade_to_black2.kill()
							self.fade_to_black3.kill()
							self.fade_to_black4.kill()
						timer = threading.Timer(2.0, time_func)
						timer.start()
				self.third_ordeal_success = True
				self.df2['Wins'][0] += 1
				self.playing = False
			else:
				self.playing = False

	def draw_grid(self):
		for x in range(0, WIDTH, TILESIZE):
			pg.draw.line(self.screen, WHITE, (x, 0), (x, HEIGHT))
		for y in range(0, HEIGHT, TILESIZE):
			pg.draw.line(self.screen,WHITE,( 0, y), (WIDTH, y))

	def draw(self):
		self.screen.fill(BGCOLOUR)
		self.draw_grid()
		self.screen.blit(FADE_TO_BLACK, (0,0))
		self.all_sprites.draw(self.screen)
		self.text1 = FONT.render(
			'Dream Tiles : ' + str(self.dream_counter), True, BROWN)
		self.textRect1 = self.text1.get_rect()
		self.textRect1.center = (100, 380)
		self.text2 = FONT.render(
			'Tiles : ' + str(self.tiles_remaining), True, BROWN)
		self.textRect2 = self.text2.get_rect()
		self.textRect2.center = (75, 360)
		self.text3 = FONT.render(
			'Traitors : ' + str(12 - int(self.traitor_count)), True, BROWN)
		self.textRect3 = self.text2.get_rect()
		self.textRect3.center = (75, 400)
		self.screen.blit(self.text1, self.textRect1)
		self.screen.blit(self.text2, self.textRect2)
		self.screen.blit(self.text3, self.textRect3)
		pg.display.flip()


	def events(self):
		def ordeal_check():
			formation_check()
			if self.force_ordeal_check == 1:
				formation_check()
				draw_for_check()
				self.force_ordeal = 1
				if self.traitor_count == 5:
					if self.force_ordeal == 1:
						pass
			if self.traitor_count == 5:
				formation_check()
				draw_for_check()
				self.force_ordeal_check = 1
			if self.traitor_count == 7 or self.force_ordeal == 1:
				second_ordeal()
				if self.second_ordeal_success:
					self.force_ordeal = 2
				else:
					self.playing = False # This is game over

			if self.traitor_count == 12 or self.force_ordeal_check == 2:
				formation_check()
				draw_for_check()
				if self.bastion_sum >= (self.third_ordeal_dict[
					self.third_ordeal_choice][0] and self.tower_sum >=
					self.third_ordeal_dict[self.third_ordeal_choice][1] and
					self.line_sum >= self.third_ordeal_dict[
					self.third_ordeal_choice][2]):
						self.third_ordeal_success = True
						self.df2['Wins'][0] += 1
						self.f = open('stats.html','w')
						self.message = ("""
		  					<html>
		  					<head>
							<title>'Castellion Stats'</title>
							<link rel="stylesheet" type="text/css"
							    href="style.css" />
		  					</head>
		  					<body>
							<div class="container">
							<div class="grid-item item-1"><img src="logo.png">
		    					<br><h1>Castellion Stats</h1></div>
							<div class="grid-item item-15">
							    <h1>Castellion Stats</h1></div>
							<div class="grid-item item-2"><h1>
							"""+str(self.df2['Games'][0])+
							"""</h1><h2>Games Played</h2></div>
							<div class="grid-item item-3">
							    <img src="piechart.png"></div>
							<div class="grid-item item-4"><h1>
							""" +str(self.df2['Wins'][0])+
							"""</h1><h2>Victories</h2></div>
							<div class="grid-item item-5">Calendar Heatmap<br>
							<br><img src="heatmap.png"></div>
		  					</div>
		  					</body>
		  					</html>""")
						self.f.write(self.message)
						self.f.close()

		def draw_tile():
			# This bit checks if the dictionary values of tiles are 0.
			#If they are then we are out of tiles.
			counter = 0
			for x in self.tiles:
				if x == 'traitor':
					pass
				else:
					counter += self.tiles[x][0]
			if counter == 0:
				self.no_more_tiles = True
				self.playing = False

			while self.current_image == 1 and not self.no_more_tiles:
				self.random_choice = random.choices(self.names,
					  weights=[.07,.07,.07,.07,.07,.07,.07,
					           .07,.07,.07,.07,.07,.14 ],k=1)
				self.random_choice = str(self.random_choice[0])
				if (self.random_choice == 'traitor'
				    and self.tiles['traitor'][0] > 0):
					self.traitor_count += 1
					if self.traitor_count == 5:
						if self.force_ordeal_check == 0:
							ordeal_check()
					if self.traitor_count == 6:
						self.traitors_y = 3
						self.traitors_x = 10
					if self.traitor_count == 7:
						second_ordeal()
						if not self.second_ordeal_success:
							self.playing = False
						self.traitors_x = 10
					if self.traitor_count == 8:
						self.traitors_y = 3
						self.traitors_x = 11
					if self.traitor_count == 12:
						ordeal_check()
						self.traitors_y = 3
						self.traitors_x = 11
					self.tile1 = Traitor(self, self.random_choice,
					                     self.tiles, self.traitors_x,
										 self.traitors_y)
					self.traitors_y += 1
					self.tiles[self.tile1.tile_type][0] -= 1
				if (self.tiles[self.random_choice][0] > 0
					and self.random_choice != 'traitor'):
					self.tile1 = Tile(self, self.random_choice, self.names,
									  self.tiles, False, self.board_info,
									  self.formation_board, 1,1)
					self.tiles_remaining -= 1
					self.current_image = None

		def draw_dream_tile():
			if self.dream_counter != 0:
				self.random_choice = random.choices(self.dream_names)
				self.random_choice = str(self.random_choice[0])
				self.dream_names.remove(self.random_choice)
				self.tile1 = Tile(self, self.random_choice, self.dream_names,
								  self.dream_tiles, False, self.board_info,
								  self.formation_board, 1,1)
				self.dream_counter -= 1
				self.current_image = None
				print(self.dream_counter)
			else:
				pass

		def formation_check():
			# First, assign new_board to the old formation board
			# but with the first 3 columns deleted.
			if self.second_ordeal_success == True:
				self.new_board = np.delete(self.formation_board,
										   np.s_[0:3], axis=1)
				self.new_board = np.delete(self.new_board, np.s_[0:2], axis=0)
				self.new_board = np.delete(self.new_board, np.s_[6], axis=0)
			else:
				self.new_board = np.delete(self.formation_board,
										   np.s_[0:3], axis=1)
				self.new_board = np.delete(self.new_board, np.s_[0:3], axis=0)
			# Now delete all 2, 3, 4 from this board to build the seer board
			self.seer_board = np.where(self.new_board > 1, 0, self.new_board)

			# Similar logic for the other boards:
			self.chameleon_board = np.where(self.new_board > 2, 0,
										    self.new_board)
			self.chameleon_board = np.where(self.chameleon_board == 1, 0,
											self.chameleon_board)
			self.chameleon_board = np.where(self.chameleon_board == 2, 1,
											self.chameleon_board)
			self.pyro_board = np.where(self.new_board > 3, 0, self.new_board)
			self.pyro_board = np.where(self.pyro_board <= 2, 0, self.pyro_board)
			self.pyro_board = np.where(self.pyro_board == 3, 1, self.pyro_board)

			self.juggler_board = np.where(self.new_board < 4, 0, self.new_board)
			self.juggler_board = np.where(self.new_board == 4, 1,
										  self.juggler_board)
			# Assign the variables
			self.bastion_sum = 0
			self.tower_sum = 0
			self.line_sum = 0
			# Check for bastions
			self.bastion_sum += bastions(self.seer_board)
			self.bastion_sum += bastions(self.chameleon_board)
			self.bastion_sum += bastions(self.pyro_board)
			self.bastion_sum += bastions(self.juggler_board)
			# Check for towers
			self.tower_sum += towers(self.seer_board.T)
			self.tower_sum += towers(self.chameleon_board.T)
			self.tower_sum += towers(self.pyro_board.T)
			self.tower_sum += towers(self.juggler_board.T)
			# Check for lines
			self.line_sum += line(self.seer_board)
			self.line_sum += line(self.chameleon_board)
			self.line_sum += line(self.pyro_board)
			self.line_sum += line(self.juggler_board	)

		# This is going to be the function that will draw
		# lines through the bottom row
		def second_ordeal():
			top_bottom = [[3,8],[4,8], [5,8], [6,8], [7,8], [8,8], [3,7],
						  [4,7], [5,7], [6,7], [7,7], [8,7]]
			# First, we need to check if the bottom row and the
			# row above it is filled.
			if all(item in self.cube_list for item in top_bottom):
			# if [3,8] and [4,8] and [5,8] and [6,8] and [7,8] and [8,8] and
			# [3,7] and [4,7] and [5,7] and [6,7] and [7,7] and [8,7]
			# in self.cube_list:
				x_cnt = 3
				for x in range(6):
					Slash(self, self.slash, x_cnt, 8)
					x_cnt += 1
				self.second_ordeal_success = True
					# You should set a variable to confirm that you did
					# infact complete the second ordeal.
					# Then use it to determine
					# if you can place tiles elsewhere (above the limit)
					# or use for the new formation check.
			else:
				pass

		def draw_for_check():
			self.window2_1 = Window2(self, self.window2, 0 ,200)
			self.min1 = Minion(self,random.choice(
							   [self.minion1, self.minion2, self.minion3]),
							   35,36)
			self.min2 = Minion(self,random.choice(
							   [self.minion1, self.minion2, self.minion3]),
							   37,36)
			self.min3 = Minion(self,random.choice(
							   [self.minion1, self.minion2, self.minion3]),
							   31,34)
			self.min4 = Minion(self,random.choice(
							   [self.minion1, self.minion2, self.minion3]),
							   33,34)
			self.min5 = Minion(self,random.choice(
							   [self.minion1, self.minion2, self.minion3]),
							   33,36)
			self.min6 = Minion(self,random.choice(
							   [self.minion1, self.minion2, self.minion3]),
							   37,35)
			self.min7 = Minion(self,random.choice(
							   [self.minion1, self.minion2, self.minion3]),
							   35,33)
			self.min8 = Minion(self,random.choice(
							   [self.minion1, self.minion2, self.minion3]),
							   31,36)
			self.min9 = Minion(self, random.choice(
							   [self.minion1, self.minion2, self.minion3]),
							   36,38)
			self.def1 = Defence(self, self.tower, 70, 30)
			self.def2 = Defence(self, self.line, 90, 36)
			self.def3 = Defence(self, self.bastion, 110, 34)
			self.minions.draw(self.screen)
			self.defences.draw(self.screen)
			self.window1 = Window(self, self.window, 0 ,200)
			self.scroll1 = Scroll(self, self.scroll, 220, 220, .05)
			self.fade_to_black = Black(self, FADE_TO_BLACK2, 0, 0)
			self.fade_to_black2 = Black(self, FADE_TO_BLACK3, 0, 400)
			self.fade_to_black3 = Black(self, FADE_TO_BLACK4, 0, 200)
			self.fade_to_black4 = Black(self, FADE_TO_BLACK5, 810, 200)

		for event in pg.event.get():
			if event.type == pg.QUIT:
				self.quit()
			if event.type == pg.MOUSEBUTTONDOWN:
				if self.draw_tile_button.rect.collidepoint(event.pos):
					draw_tile()
				if self.discard_tile_button.rect.collidepoint(event.pos):
					self.discard_tile_button.clicked = True
					self.tiles[self.tile1.tile_type][0] -= 1
					# Must remove the coords from the cube list if you're
					# deleting the tile as well. Otherwise it thinks there is
					# a cube there and you cannot place a tile there.
					try:
						self.cube_list.remove([self.tile1.x, self.tile1.y])
						self.tile1.kill()
						self.random_choice = random.choice(self.names)
						self.current_image = 1
					except:
						pass
				if self.tile1.rect.collidepoint(event.pos):
					self.current_image = 1
				if self.ordeal_button2.rect.collidepoint(event.pos):
					self.force_ordeal_check += 1
					ordeal_check()
				if self.restart_button2.rect.collidepoint(event.pos):
					self.new()
				if self.quit_button2.rect.collidepoint(event.pos):
					pg.quit()
				if self.dream_tile_button2.rect.collidepoint(event.pos):
					draw_dream_tile()
				if self.stats_button2.rect.collidepoint(event.pos):
					url = 'file:///'+os.getcwd()+'/' + 'stats.html'
					webbrowser.open(url)
			if event.type == pg.MOUSEMOTION:
				if event.buttons[self.left_button]:
					if self.current_image == 1 and self.image_released == None:
						self.x, self.y = pg.mouse.get_pos()
						self.ix = self.x // TILESIZE
						self.iy = self.y // TILESIZE
						self.cx, self.cy = (self.ix
						    * TILESIZE, self.iy * TILESIZE)
					try:
						self.tile1.move(self.cx, self.cy, self.ix, self.iy)
					except:
						pass
			if event.type == pg.MOUSEBUTTONUP:
				# If the sprite is the current image and the original
				# coordinates are not equal to the current x and y
				# basically saying if the original coordinates are not equal
				# to the original coordinates, then stop movement
				# (the tile has moved)
				if (self.current_image == 1 and self.tile1.original_coords !=
				    [self.tile1.x, self.tile1.y] and self.image_released != 1):
					if self.tile1.valid_placement(self.tile1.x, self.tile1.y,
					    self.second_ordeal_success):
						self.board_info[self.tile1.x, self.tile1.y] = ([
						    self.tile1.type, self.tile1.shape])
						self.formation_board[self.tile1.y, self.tile1.x] = (
						    self.tile1.indicator)
						self.tile1.valid_placement(self.tile1.x, self.tile1.y,
						    self.second_ordeal_success)
						# Once the placement is valid, subtract 1 from the
						# total amount of remaining tiles
						self.tiles[self.tile1.tile_type][0] -= 1
						self.image_released = 1
						self.tile1.active_tile = False
						self.image_released = None

			#if event.type == pg.KEYDOWN:
				#self.playing = False
	def show_start_screen(self):
		pass

	def show_go_screen(self):
		if not self.playing:
			self.screen.blit(FADE_TO_BLACK, (0,0))
			self.screen.blit(BACKGROUND, BACKGROUND_RECT)
			if self.third_ordeal_success:
				self.text4 = FONT2.render(('You Won!'), True, WHITE)
			else:
				self.text4 = FONT2.render(('Game Over'), True, WHITE)
			self.text5 = FONT.render(('Press Any Key To Restart'), True, WHITE)
			self.textRect5 = self.text5.get_rect()
			self.textRect5.center = (WIDTH/2, 420)
			self.screen.blit(self.text5, self.textRect5)
			self.textRect4 = self.text4.get_rect()
			self.textRect4.center = (WIDTH/2, 370)
			self.screen.blit(self.text4, self.textRect4)
			pg.display.flip()
			waiting = True
			while waiting:
				self.clock.tick(FPS)
				for event in pg.event.get():
					if event.type == pg.QUIT:
						waiting = False
						self.playing = False
					if event.type == pg.KEYDOWN:
						waiting = False
g = Game()
g.show_start_screen()

while True:
	g.new()
	g.run()
	g.show_go_screen()
