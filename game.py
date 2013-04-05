import pygame
import threading
import math
import random
import sys
from pygame import key

def set_timeout(func, sec):     
    t = None
    def func_wrapper():
        func()  
        t.cancel()
    t = threading.Timer(sec, func_wrapper)
    t.start()


class game:
	def __init__(self):
		blocks = [200]
		for x in range(100):
			blocks.append(random.randint(100, 350))

		self.blocksy = blocks
		self.blocksx = 800
		self.block_speed = 20
		self.width = 800
		self.height = 600
		self.x_off = 0
		self.y_off = 0
		self.player_alive = True
		self.playerx = 0
		self.playery = 0
		self.player_speed = 10
		self.player_width = 20
		self.player_height = 60
		self.gravity = 5
		self.force = 15
		self.floor_height = 200
		self.floor_width = 800
		self.black = (0, 0, 0)
		self.red = (255, 0, 0)
		self.green = (0, 255, 0)
		self.blue = (0, 0, 255)
		self.white = (255, 255, 255)
		self.i = 0

	def init(self):
		self.screen = pygame.display.set_mode((800, 600))
		self.clock = pygame.time.Clock()
		try: 
			pygame.init()
			return True
		except:
			e = sys.exc_info()[0]
			return False
			print e
			sys.exit()

	def draw(self):
		self.screen.fill(self.black)
		pygame.draw.rect(self.screen, self.blue, [0, 400,800, 200], 0)
		pygame.draw.rect(self.screen, self.green, [self.playerx, self.playery, self.player_width, self.player_height], 0)
				
		pygame.draw.rect(self.screen, self.red, [self.blocksx, self.blocksy[self.i], 60, 20], 0)
		self.blocksx -= self.block_speed
		if self.blocksx<-80:
			self.blocksx = 800
			self.i += 1
		if self.i > 100:
			self.i = random.randint(1, 100)

	def loop(self, run):

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		keys = pygame.key.get_pressed()

		if keys[275]:
			self.playerx += self.player_speed
		if keys[276]:
			self.playerx += -self.player_speed
		if keys[273]:
			self.playery -= self.force

		if self.playerx <= 0:
			self.playerx = 0
		if self.playerx >= self.width:
			self.playerx = self.width
		if self.playery >= self.height - self.player_height - self.floor_height:
			self.playery = self.height - self.player_height - self.floor_height

		self.playery += self.gravity
		if self.playery >= 400 - self.player_height:
			self.playery = 400 - self.player_height 

		self.draw()
		pygame.display.update()
		pygame.display.flip()
		self.clock.tick(60)

game = game()
	
if __name__ == '__main__':
	run = game.init()

	while run:
		game.loop(run)
		

