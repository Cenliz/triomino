# /ᐠ｡ꞈ｡ᐟ\
import pieces_file, pygame, sys
import random
from pygame.locals import *

def test_room():
    screen.fill("purple")
    deck = pieces_file.create_pieces()
    rdm = random.randrange(56)
    pieces_file.display_piece(screen, font, deck[rdm], (500,500), 100)
    pieces_file.display_piece(screen, font, deck[10], (300,300), 100)

pygame.init()
pygame.display.set_caption('Triomino')
screen = pygame.display.set_mode((1200, 700))
clock = pygame.time.Clock()
fps = 1
state = 'test'
font = pygame.font.SysFont("Arial",24)
running = True



while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    
    match state:
        case 'test':
            test_room()

    clock.tick(fps)
    pygame.display.update()

pygame.quit()
sys.exit()
