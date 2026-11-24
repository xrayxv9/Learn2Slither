# import pygame
import argparse

from map import Map

parser = argparse.ArgumentParser(description='map size')

parser.add_argument('--size', action='store', dest='map_size', default=10, type=int)

args = parser.parse_args()

if (args.map_size > 20):
    print("For a display reason, any size above 20 are not authorized")
elif (args.map_size < 5):
    print("For a gameplay reason, any size under 5 are forbidden")
else:
    map = Map(args.map_size)
    print("BASIC MAP", end='\n\n\n\n')
    map.print_map()
    map.snake_spawn()
    print("\n\n\nSPAWN MAP")
    map.print_map()


# pygame.init()
# screen = pygame.display.set_mode((680, 800))
# clock = pygame.time.Clock()
# running = True
#
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_ESCAPE]:
#         running = False
