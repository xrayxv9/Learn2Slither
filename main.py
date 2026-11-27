# import pygame
import argparse
from agent import Agent
from enums import Y, X, Update_map
from map import Map
from watcher import Watcher

parser = argparse.ArgumentParser(description='map size')

parser.add_argument('--size', action='store', dest='map_size', default=10, type=int)

args = parser.parse_args()

if (args.map_size > 20):
    print("For a display reason, any size above 20 are not authorized")
elif (args.map_size < 5):
    print("For a gameplay reason, any size under 5 are forbidden")
else:
    map = Map(args.map_size)
    snake_pos = map.snake_spawn()
    head = Agent(snake_pos[0][Y], snake_pos[0][X])
    head.spawn()
    env = Watcher(head, map)
    # print("======================================================")
    # head.go_right()
    env.update_env()
    map.print_map()

    inp = 'oui'
    exit_status: Update_map = Update_map.NOTHING
    while (inp != 'quit' and exit_status == Update_map.NOTHING):
        inp = input("what to do ? (a, s, d, w)")
        if (inp == 'a'):
            head.go_left()
        elif (inp == 's'):
            head.go_down()
        elif (inp == 'd'):
            head.go_right()
        else:
            head.go_up()
        exit_status = env.update_env()
        map.print_map()
        print("======================================================")
    if Update_map.WON == exit_status:
        print("You Won !")
    else:
        print(f"You lost due to: {'your tail' if exit_status == Update_map.TAIL else 'a wall'}")



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
