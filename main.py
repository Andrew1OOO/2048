from board import Board
from block import Block
import create_blocks
import pygame as pg
from pygame.constants import BLEND_RGB_ADD, BLEND_RGB_MAX, SRCALPHA

game_exit = False
BLACK = (0 ,0, 0)
def round_rect(surf, rect, rad, color, thick=0):
	if not rad:
		pg.draw.rect(surf, color, rect, thick)
	elif rad > rect.width / 2 or rad > rect.height / 2:
		rad = min(rect.width/2, rect.height/2)

	if thick > 0:
		r = rect.copy()
		x, r.x = r.x, 0
		y, r.y = r.y, 0
		buf = pg.surface.Surface((rect.width, rect.height)).convert_alpha()
		buf.fill((0,0,0,0))
		round_rect(buf, r, rad, color, 0)
		r = r.inflate(-thick*2, -thick*2)
		round_rect(buf, r, rad, (0,0,0,0), 0)
		surf.blit(buf, (x,y))


	else:
		r  = rect.inflate(-rad * 2, -rad * 2)
		for corn in (r.topleft, r.topright, r.bottomleft, r.bottomright):
			pg.draw.circle(surf, color, corn, rad)
		pg.draw.rect(surf, color, r.inflate(rad*2, 0))
		pg.draw.rect(surf, color, r.inflate(0, rad*2))

pg.init()
surface = pg.display.set_mode((450, 450))
clock = pg.time.Clock()
blue = (115, 147, 179)



board = pg.Surface((300, 300))

#board.fill((146 ,146, 146))

rect = pg.Rect(0,0,300,300)
round_rect(board,rect, 10,(100,100,100))
surface.blit(board, (75, 75))

pos = (-5,0)



board1 =[[0,create_blocks.block3,0,create_blocks.block2],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]]


act_board = Board(board1)


for i in range(len(board1)):
    for j in range(len(board1[0])):
        k=60
        while k > 5:
            pg.draw.rect(board, (146,146,146),pg.Rect((j*75)+8, (i*75)+8, k,k),2,3)
            k -=1


while not game_exit:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_exit = True
        if event.type == pg.MOUSEBUTTONDOWN:
            if(event.button == 1):
                pos = pg.mouse.get_pos()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                act_board.shift_left()

            if event.key == pg.K_RIGHT:
                act_board.shift_right()
            if event.key == pg.K_DOWN:
                act_board.shift_vertical(False)
            if event.key == pg.K_UP:
                act_board.shift_vertical(True)

    surface.blit(board, (75, 75))


    act_board.paint(board)



    pg.display.update()
    
    pg.display.flip()
    clock.tick(30)