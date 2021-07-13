import tkinter as tk
from tkinter import *
import tkinter
import os

from pygame.constants import QUIT
from board import Board
from block import Block
import copy
import random
import pygame as pg


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


def find_best_move(board, amount):
    possible_moves = ["L", "R", "U", "D"]
    totalSims = amount

    simScore = [0,0,0,0]
    inter = 0
    for i in range(int(totalSims)):
        #print("New simulation")
        if(inter == 4):
            inter = 0
        simulation = Board()
        simulation.board = copy.deepcopy(board)
        
        simulation.move(possible_moves[inter])
        simulation.add_block(Block(2 * random.randint(1,2), pg.Rect(0,0, 60, 60)))

        while((simulation.game_over() == False)):
            simulation.move(possible_moves[random.randint(0,3)])
            simulation.add_block(Block(2 * random.randint(1,2), pg.Rect(0,0, 60, 60)))


        simScore[inter] += simulation.get_score()
        inter += 1
    topScore = max(simScore)
    #print("SimScore",simScore)
    #print("possile",possible_moves)

    index = simScore.index(topScore)
    bestMove = possible_moves[index]

    return bestMove




def QUIT():
    root.destroy()





global amount_sims
amount_sims = 0
def game():

    game_exit = False
    BLACK = (0 ,0, 0)

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











    act_board = Board() 
    play = False

    for i in range(4):
        for j in range(4):
            k=60
            while k > 5:
                pg.draw.rect(board, (146,146,146),pg.Rect((j*75)+8, (i*75)+8, k,k),2,3)
                k -= 1



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
                    act_board.add_block(Block(2 * random.randint(1,2), pg.Rect(0,0, 60, 60)))
                if event.key == pg.K_RIGHT:
                    act_board.shift_right()
                    act_board.add_block(Block(2 * random.randint(1,2), pg.Rect(0,0, 60, 60)))
                if event.key == pg.K_DOWN:
                    act_board.shift_vertical(False)
                    act_board.add_block(Block(2 * random.randint(1,2), pg.Rect(0,0, 60, 60)))
                if event.key == pg.K_UP:
                    act_board.shift_vertical(True)
                    act_board.add_block(Block(2 * random.randint(1,2), pg.Rect(0,0, 60, 60)))
                if event.key == pg.K_c:
                    act_board.clear()

        #this is the code that makes the computer play, change play to True to play the game, play if defined above the while
        if(not play):
            l = find_best_move(act_board.board, amount_sims)
            act_board.move(l)
            act_board.add_block(Block(2 * random.randint(1,2), pg.Rect(0,0, 60, 60)))

        surface.blit(board, (75, 75))


        act_board.paint(board)


        pg.display.update()
        
        pg.display.flip()
        clock.tick(30)



root = tkinter.Tk()
embed = tk.Frame(root, width = 500, height = 300)
embed.grid(columnspan = (600), rowspan = 500) 
embed.pack(side = tk.LEFT) 
buttonwin = tk.Frame(root, width = 75, height = 500)
buttonwin.pack(side = tk.LEFT)

lbl=Label(root, text="2048 Monte Carlo Simulations", fg='black', font=("Ariel", 16))
lbl.place(x=60, y=50)
root.title('2048 Monte Carlo Simulations')

def change_amount(x):
    x = txtfld.get()
    global amount_sims
    amount_sims = x

txtfld = Entry(root)
txtfld.bind('<Return>', change_amount)
txtfld.place(x=80, y=150)


button1 = Button(buttonwin,text = 'Quit',  command=QUIT)
button1.pack(side=LEFT, padx=15, pady=20)

button2 = Button(buttonwin,text = '2048~AI',  command=game)
button2.pack(side=RIGHT, padx=15, pady=20)


root.mainloop()