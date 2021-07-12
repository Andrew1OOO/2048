from block import Block
import pygame as pg
from pygame.constants import BLEND_RGB_ADD, BLEND_RGB_MAX, SRCALPHA

game_exit = False
BLACK = (0, 0, 0)


pg.init()
surface = pg.display.set_mode((500, 500))
clock = pg.time.Clock()
blue = (115, 147, 179)

block = Block(2, blue, pg.Rect(30, 30, 60, 60))



pos = (0,0)



board =[(0,0,0,0),
        (0,0,0,0),
        (0,0,0,0),
        (0,0,0,0)]


while not game_exit:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_exit = True
        if event.type == pg.MOUSEBUTTONDOWN:
            if(event.button == 1):
                pos = pg.mouse.get_pos()
                print("pos" + str(pos))
    block.move(surface,pos)
    block.draw(surface)
    pg.display.update()

    pg.display.flip()
    clock.tick(30)