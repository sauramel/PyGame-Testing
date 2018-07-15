#!/usr/bin/env python
import os
import pygame
from pygame.locals import *

def main():
    color = [0, 0, 0]
    color_change_map = {K_r: lambda: }
    changed = False
    blendtype = 0
    step = 5

    pygame.init ()
    screen = pygame.display.set_mode ((640, 480), 0, 32)
    screen.fill ((100, 100, 100))

    pygame.display.flip ()
    pygame.key.set_repeat (500, 30)

    going = True
    while going:
        for event in pygame.event.get():
            if event.type == QUIT:
                going = False

            if event.type == KEYDOWN:
                #event.unicode is a string representation
                # of the key pressed

                #the K_x values are provided by pygame.locals
                # and represent each individual key on the keyboard
                
                if event.key == K_ESCAPE:
                    going = False

                if event.key == K_r:
                    color[0] += step
                    if color[0] > 255:
                        color[0] = 0
                    changed = True

                elif event.key == K_g:
                    color[1] += step
                    if color[1] > 255:
                        color[1] = 0
                    changed = True

                elif event.key == K_b:
                    color[2] += step
                    if color[2] > 255:
                        color[2] = 0
                    changed = True

            if changed:
                screen.fill ((100, 100, 100))
                print ("Color: %s, Pixel (0,0): %s" %
                       (tuple(color),
                        [screen.get_at ((0, 0))]))
                changed = False
                pygame.display.flip ()

    pygame.quit()

if __name__ == '__main__':
    main()
