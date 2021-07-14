import pygame
from color_constants import Colors
import pygame.freetype

class Block:
    def __init__(self, size, rect, dMode):
        self.size = size
        self.colors = Colors(dMode)
        self.color = self.find_color(self.size, dMode)
        self.dMode = dMode
        self.BLACK = (0, 0, 0)
        self.rect = rect
        
    def set_size(self, size):
        self.size = size

    def find_color(self,size, darkMode):
        color = (0,0,0)
        
        if(size == 2):
            color = self.colors.block_2
        if(size == 4):
            color = self.colors.block_4
        if(size == 8):
            color = self.colors.block_8
        if(size == 16):
            color = self.colors.block_16
        if(size == 32):
            color =self.colors.block_32
        if(size == 64):
            color = self.colors.block_64
        if(size == 128):
            color = self.colors.block_128
        if(size == 256):
            color =self.colors.block_256
        if(size == 512):
            color = self.colors.block_512
        if(size == 1024):
            color = self.colors.block_1024
        if(size == 2048):
            color = self.colors.block_2048
        return color

    def destroy(self):
        self.size = 0
        self.color = self.colors.block_E
    
    def set_color(self,color):
        self.color = color

    def draw(self, surface, board, scoreSurface, score):
        Font = pygame.freetype.SysFont('Sans', 15)

        #score = 0
        if(self.size > 0):
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if(board[i][j] != 0):
                        pos = self.decrypt(j, i)
                        #score += board[i][j].size
                        k=60
                        
                        while k > 5:
                            
                            pygame.draw.rect(surface, self.find_color(board[i][j].size, self.dMode),pygame.Rect(pos[0],pos[1],k,k),2,3)
                            k -=1
                        
                            
                        sized_rect = Font.get_rect(str(board[i][j].size))
                        width = sized_rect.width
                        height = sized_rect.height
                        sized_rect.center = (pos[0]+(60-width)/2,pos[1]+(60-height)/2)
                        sized = Font.render_to(surface, sized_rect.center, str(board[i][j].size), self.colors.letter)
                            #surface.blit(sized, (pos[0]+(60-width)/2,pos[1]+(60-height)/2) )

                    self.repaint(surface, board)
            self.repaintSurface(scoreSurface)
            score_rect = Font.get_rect(str(score))
            swidth = score_rect.width
            sheight = score_rect.height
            score_rect.center = (245+(100-swidth)/2,43+(30-sheight)/2)
            scored = Font.render_to(scoreSurface, score_rect.center, str(score), self.colors.letter)
            
    def repaint(self,surface,board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if(board[i][j] != 0):
                    pass
                else:
                    pos = self.decrypt(j, i)
                    k=60
                    while k > 5:
                        pygame.draw.rect(surface, self.colors.block_E,pygame.Rect(pos[0],pos[1],k,k),2,3)
                        k -=1
    def repaintSurface(self,surface):
        scoreboard = pygame.Rect(245,40,100,30)
        self.round_rect(surface, scoreboard, 4, self.colors.scoreboard)

    def decrypt(self, i,j):
        return (i*75+8,j*75+8)
    

    def round_rect(self, surf, rect1, rad, color, thick=0):
        if not rad:
            pygame.draw.rect(surf, color, rect1, thick)
        elif rad > rect1.width / 2 or rad > rect1.height / 2:
            rad = min(rect1.width/2, rect1.height/2)

        if thick > 0:
            
            r = rect1.copy()
            
            x, r.x = r.x, 0
            y, r.y = r.y, 0
            buf = pygame.surface.Surface((rect1.width, rect1.height)).convert_alpha()
            buf.fill((0,0,0,0))
            self.round_rect(buf, r, rad, color, 0)
            r = r.inflate(-thick*2, -thick*2)
            self.round_rect(buf, r, rad, (0,0,0,0), 0)
            surf.blit(buf, (x,y))


        else:
            
            r  = rect1.inflate(-rad * 2, -rad * 2)
            for corn in (r.topleft, r.topright, r.bottomleft, r.bottomright):
                pygame.draw.circle(surf, color, corn, rad)
                
            pygame.draw.rect(surf, color, r.inflate(rad*2, 0))
            pygame.draw.rect(surf, color, r.inflate(0, rad*2))