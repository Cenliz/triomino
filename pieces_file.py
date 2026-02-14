# /ᐠ｡ꞈ｡ᐟ\

import pygame, math
from pygame.locals import *

class Piece():
    def __init__(self, up:int, left:int, right:int)->None:
        self.__upper_value = up
        self.__left_value = left
        self.__right_value = right
    
    def get_values(self):
        return (self.__upper_value, self.__left_value, self.__right_value)

def create_pieces()->list:
    deck = []
    for a in range(6):
        for b in range(a, 6):
            for c in range(b, 6):
                deck.append(Piece(a,b,c))
    return deck

def display_piece(screen:pygame.Surface, font:pygame.font.Font, pc:Piece, place:tuple, size:float,direction:str)->None:
    pc_value = pc.get_values()
    if direction == "up":
        t1 = (place[0], place[1] - size)
        t2 = (place[0] + size * math.cos(0.5), place[1] + size * math.sin(0.5))
        t3 = (place[0] - size * math.cos(0.5), place[1] + size * math.sin(0.5))
    else:
        t1 = (place[0], place[1] + size)
        t2 = (place[0] - size * math.cos(0.5), place[1] - size * math.sin(0.5))
        t3 = (place[0] + size * math.cos(0.5), place[1] - size * math.sin(0.5))
    li = [t1,t2,t3]

    n1 = font.render(str(pc_value[0]),True,(0,0,0))
    n2 = font.render(str(pc_value[1]),True,(0,0,0))
    n3 = font.render(str(pc_value[2]),True,(0,0,0))

    pygame.draw.circle(screen, (255,255,255), (t1[0] + 1,t1[1] + 1), 10)
    pygame.draw.circle(screen, (255,255,255), (t2[0] + 1,t2[1] + 1), 10)
    pygame.draw.circle(screen, (255,255,255), (t3[0] + 1,t3[1] + 1), 10)
    pygame.draw.polygon(screen, (255,255,255), li, 22) # outer border
    pygame.draw.polygon(screen, (255,255,255), li) # inner body
    screen.blit(n1, (t1[0] - 5, t1[1] - 12))
    screen.blit(n2, (t2[0] - 5, t2[1] - 12))
    screen.blit(n3, (t3[0] - 5, t3[1] - 12))

    return