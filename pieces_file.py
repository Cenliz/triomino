# /ᐠ｡ꞈ｡ᐟ\
import pygame
from pygame.locals import *
import math

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

def display(screen:pygame.Surface, font:pygame.font.Font, pc:Piece, place:tuple, size:int)->None:
    pc_value = pc.get_values()

    p1 = (place[0], place[1] - size)
    p2 = (place[0] + size * math.cos(0.5), place[1] + size * math.sin(0.5))
    p3 = (place[0] - size * math.cos(0.5), place[1] + size * math.sin(0.5))
    n1 = font.render(str(pc_value[0]),True,(0,0,0))
    n2 = font.render(str(pc_value[1]),True,(0,0,0))
    n3 = font.render(str(pc_value[2]),True,(0,0,0))
    li = [p1,p2,p3]

    pygame.draw.polygon(screen, (255,255,255), li)
    screen.blit(n1, p1)
    screen.blit(n2, p2)
    screen.blit(n3, p3)