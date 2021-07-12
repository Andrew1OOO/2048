import pygame
from pygame.constants import BLEND_RGB_ADD, BLEND_RGB_MAX, BLEND_RGB_MIN, SRCALPHA

class Block:
    def __init__(self, size, color, rect):
        self.size = size
        self.color = color
        self.BLACK = (0, 0, 0)
        self.rect = rect
    def set_size(self, size):
        self.size = size
    
    def merge(self, block2):
        self.size += block2.size
        block2.destroy()

    def destroy(self):
        self.size = 0
        self.color = 0
    


    def draw(self, surface, radius=0.4):
        
        '''rect = self.rect
        colour = pygame.Color(*self.color)
        alpha = colour.a
        colour.a = 0
        pos = rect.topleft
        rect.topleft = 0, 0
        rectangle = pygame.Surface(rect.size, SRCALPHA)

        circle = pygame.Surface([min(rect.size) * 3] * 2, SRCALPHA)
        pygame.draw.ellipse(circle, self.BLACK, circle.get_rect(), 0)
        circle = pygame.transform.smoothscale(
            circle, [int(min(rect.size)*radius)]*2)

        radius = rectangle.blit(circle, (0, 0))
        radius.bottomright = rect.bottomright
        rectangle.blit(circle, radius)
        radius.topright = rect.topright
        rectangle.blit(circle, radius)
        radius.bottomleft = rect.bottomleft
        rectangle.blit(circle, radius)

        rectangle.fill(self.BLACK, rect.inflate(-radius.w, 0))
        rectangle.fill(self.BLACK, rect.inflate(0, -radius.h))

        rectangle.fill(colour, special_flags=BLEND_RGB_MAX)
        rectangle.fill((255, 255, 255, alpha), special_flags=BLEND_RGB_MIN)

        surface.blit(rectangle, pos)'''

        #print(self.rect.x)
        i=30
        while i > 5:
            pygame.draw.rect(surface, self.color,pygame.Rect(self.rect.x, self.rect.y,i,i),2,3)
            i -=1

    def erase_rect(self,surface):
        
        pygame.draw.rect(surface,(0,0,0),pygame.Rect(self.rect.x, self.rect.y,30,30))

    def move(self, surface, pos):
        self.erase_rect(surface)
        self.rect.center = (pos[0]+15, pos[1]+15)

