
import pygame
from pygame.constants import BLEND_RGB_MAX, BLEND_RGB_MIN, SRCALPHA
from pygame.time import Clock


BLACK = (0, 0, 0)

def drawRoundRect(surface, colour, rect, radius=0.4):
    """
    Draw an antialiased rounded filled rectangle on screen
    Parameters:
        surface (pygame.Surface): destination
        colour (tuple): RGB values for rectangle fill colour
        radius (float): 0 <= radius <= 1
    """

    rect = pygame.Rect(rect)
    colour = pygame.Color(*colour)
    alpha = colour.a
    colour.a = 0
    pos = rect.topleft
    rect.topleft = 0, 0
    rectangle = pygame.Surface(rect.size, SRCALPHA)

    circle = pygame.Surface([min(rect.size) * 3] * 2, SRCALPHA)
    pygame.draw.ellipse(circle, BLACK, circle.get_rect(), 0)
    circle = pygame.transform.smoothscale(
        circle, [int(min(rect.size)*radius)]*2)

    radius = rectangle.blit(circle, (0, 0))
    radius.bottomright = rect.bottomright
    rectangle.blit(circle, radius)
    radius.topright = rect.topright
    rectangle.blit(circle, radius)
    radius.bottomleft = rect.bottomleft
    rectangle.blit(circle, radius)

    rectangle.fill(BLACK, rect.inflate(-radius.w, 0))
    rectangle.fill(BLACK, rect.inflate(0, -radius.h))

    rectangle.fill(colour, special_flags=BLEND_RGB_MAX)
    rectangle.fill((255, 255, 255, alpha), special_flags=BLEND_RGB_MIN)

    surface.blit(rectangle, pos)



pygame.init()

surface = pygame.display.set_mode((400, 300))

color = (115, 147, 179)

drawRoundRect(surface, color, pygame.Rect(30, 30, 60, 60))


game_exit = False
while not game_exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True

    pygame.display.update()

    pygame.display.flip()
