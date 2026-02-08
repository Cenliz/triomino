# /ᐠ｡ꞈ｡ᐟ\

import pieces_file, map_file, pygame, sys
import random
from pygame.locals import *   

pygame.init()
pygame.display.set_caption('Triomino')
screen = pygame.display.set_mode((1200, 700))
clock = pygame.time.Clock()
fps = 60
state = 'test'
font = pygame.font.SysFont("Arial",24)
loaded = False
pieces_size = 50

running = True

while running:

    match state:

        case 'test':
            if loaded == False:
                deck = pieces_file.create_pieces()
                board = map_file.Board()
                placed_pieces = []
                placed_pieces_location = []
                player1_deck = []
                for i in range(7): # 2p = 9piecces, 3+p = 7pieces 
                    player1_deck.append(deck.pop(random.randint(0,len(deck)-1)))
                loaded = True
            else:
                screen.fill("purple")
                for i in board.get_points():
                    pygame.draw.circle(screen, (0,0,0), i.get_pos(), 10)
                if len(placed_pieces) != 0:
                    for i in range(len(placed_pieces)):
                        pieces_file.display_piece(screen, font, placed_pieces[i], placed_pieces_location[i], pieces_size, board.check_pos(placed_pieces_location[i]).get_direction())
                for i in range(len(player1_deck)):
                    pieces_file.display_piece(screen,font,player1_deck[i],(150*i+100,650),pieces_size,"up")

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0] == True: # left click
                for i in board.get_points():
                    if i.get_pos()[0]-pieces_size*2/3 < pygame.mouse.get_pos()[0] < i.get_pos()[0]+pieces_size*2/3 and i.get_pos()[1]-pieces_size*2/3 < pygame.mouse.get_pos()[1] < i.get_pos()[1]+pieces_size*2/3 and board.check_point(i) == "placable":
                        if len(deck) == 0:
                            break
                        placed_pieces.append(deck.pop(random.randint(0,len(deck)-1)))
                        placed_pieces_location.append(i.get_pos())
                        board.update_board( i, pieces_size)
                        break

        if event.type == MOUSEWHEEL:
            y = event.y
            if  y != 0:
                pieces_size += y
            if pieces_size < 20:
                pieces_size = 20
            if pieces_size > 100:
                pieces_size = 100
        

                    

    clock.tick(fps)
    pygame.display.update()

pygame.quit()
sys.exit()