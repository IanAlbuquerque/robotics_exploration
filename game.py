import hero
import grid
import direction
import action

import skimage.io as skio
import matplotlib.pyplot as plt

class Game:

	def __init__(self, walls_grid, game_hero):

		if not isinstance(walls_grid,grid.Grid):
			raise ValueError("Invalid type for game grid.")
		if not isinstance(game_hero,hero.Hero):
			raise ValueError("Invalid type for game hero.")

		if not game_hero.isInRange(0,walls_grid.shape[0],0,walls_grid.shape[1]):
			raise ValueError("Game hero out of the bounds of the grid.")

		self.hero = game_hero
		self.walls = walls_grid


	def toImage(self):
		image = self.walls.toImage()

		hero_position = self.hero.getPosition()
		hero_direction = self.hero.getDirection()

		hero_next_cell = hero_position + hero_direction.toVector()

		hero_color = [1,0,0]

		if not self.walls.exists(hero_next_cell):
			hero_facing_color = [0.5,0,0]
		else:
			hero_facing_color = [0.5,0.7,0.7]

		image[hero_position.y,hero_position.x] = hero_color
		image[hero_next_cell.y,hero_next_cell.x] = hero_facing_color

		return image

	def doAction(self,action_taken):
		if not isinstance(action_taken,action.Action):
			raise ValueError("Invalid type for action.")

		hero_next_state = self.hero.copy()
		hero_next_state.doAction(action_taken)

		hero_next_position = hero_next_state.getPosition()

		if not self.walls.exists(hero_next_position):
			self.hero = hero_next_state
		

