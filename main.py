# /ᐠ｡ꞈ｡ᐟ\

import pygame
from pygame.locals import *

class piece():
    def __init__(self,up:int,right:int,left:int):
        self.__up = up
        self.__right = right
        self.__left = left

def create_pieces(max_number:int)->list:
    pieces = []
    for a in range(max_number + 1):
        for b in range(a,max_number + 1):
            for c in range(b,max_number + 1):
                pieces.append(piece(a,b,c))
    return pieces
                
pygame.init()
window = pygame.display.set_mode((640,480))
background = pygame.image.load("./Desktop/projects/triomino/media/stonks_dev.webp").convert()
window.blit(background,(0,0))
runing = True

pieces = create_pieces(5)

while runing == True:
    for event in pygame.event.get():
        if event.type == QUIT:
            runing = False
    pygame.display.update()

pygame.quit()

print("\n /\\     /\\\n/  0 A 0  \\")