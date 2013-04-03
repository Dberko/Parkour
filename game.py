import pygame
import math
import random
import sys, os
from pygame import key

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True
pygame.init()

width = 800
height = 600
x_off = 0
y_off = 0
playerx = 0
playery = 0
player_speed = 5
player_width = 20
player_height = 60
gravity = 5
floor_height = 200
floor_width = 800

black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)


while running:

	keys = pygame.key.get_pressed()
	if keys[275]:
		playerx += player_speed
	if keys[276]:
		playerx += -player_speed


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	if playerx <= 0:
		playerx = 0
	if playerx >= width:
		playerx = width
	if playery >= height - player_height - floor_height:
		playery = height - player_height - floor_height

	playery += gravity
	if playery >= 400 - player_height:
		playery = 400 - player_height 

	screen.fill(black)
	pygame.draw.rect(screen, blue, [0, 400,800, 200], 0)
	pygame.draw.rect(screen, green, [playerx,playery,player_width,player_height], 0)


	pygame.display.flip()
	clock.tick(60)
	