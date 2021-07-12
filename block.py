from board import Board
import pygame
import color_constants


class Block:
    def __init__(self, size, rect):
        self.size = size
        self.color = self.find_color(self.size)
        
        self.BLACK = (0, 0, 0)
        self.rect = rect
    def set_size(self, size):
        self.size = size

    def find_color(self,size):
        color = (0,0,0)
        if(size == 2):
            color = color_constants.block_2
        if(size == 4):
            color = color_constants.block_4
        if(size == 8):
            color = color_constants.block_8
        if(size == 16):
            color = color_constants.block_16
        if(size == 32):
            color = color_constants.block_32
        if(size == 64):
            color = color_constants.block_64
        if(size == 128):
            color = color_constants.block_128
        if(size == 256):
            color = color_constants.block_256
        if(size == 512):
            color = color_constants.block_512
        if(size == 1024):
            color = color_constants.block_1024
        if(size == 2048):
            color = color_constants.block_2048
        return color
    def merge(self, block2):
        self.size += block2.size
        block2.destroy()

    def destroy(self):
        self.size = 0
        self.color = (146,146,146)
    
    def set_color(self,color):
        self.color = color

    def draw(self, surface, board):
        if(self.size > 0):
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if(board[i][j] != 0):
                        pos = Board.center(Board.decrypt(Board, j, i))
                        k=50
                        while k > 5:
                            
                            pygame.draw.rect(surface, self.find_color(board[i][j].size),pygame.Rect(pos[0],pos[1],k,k),2,3)
                            k -=1
                    self.repaint(surface, board)
    def repaint(self,surface,board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if(board[i][j] != 0):
                    pass
                else:
                    pos = Board.decrypt(Board, j, i)
                    k=55
                    while k > 5:
                        pygame.draw.rect(surface, (146,146,146),pygame.Rect(pos[0],pos[1],k,k),2,3)
                        k -=1
    
