# /ᐠ｡ꞈ｡ᐟ\
# TODO:
# [V] correct the rotation of the "down" pieces,
# [] choose a piece to mettre sur the board,
# [] add a way to rotate properly,
# [] check if placable,
# [] check for points,
# [] add multiplayer(?),
# [] add bots

import pieces_file, map_file, pygame, sys
import random
from pygame.locals import *   

pygame.init()
pygame.display.set_caption("Triomino")
screen = pygame.display.set_mode((1200, 700))
clock = pygame.time.Clock()
fps = 60
state = "test"
game_state = "draw"
font = pygame.font.SysFont("Arial",24)
loaded = False
pieces_size = 50
player_number = 1
pieces_per_deck = 7 # Temp, rm that when menu added
running = True

while running:

    match state:

        case "test":
            if not loaded:
                deck = pieces_file.create_pieces()
                board = map_file.Board()
                #rack = map_file.Rack()
                placed_pieces = []
                placed_pieces_location = []
                players_decks = []
                selected_piece = None # pice's number in the player's deck
                if player_number == 2:
                    pieces_per_deck = 9
                elif 3 <= player_number <= 4:
                    pieces_per_deck = 7 
                for pn in range(player_number):
                    players_decks.append([])
                    for i in range(pieces_per_deck): # 2p = 9piecces, 3-4p = 7pieces 
                        players_decks[pn].append(deck.pop(random.randint(0,len(deck)-1)))
                
                loaded = True
                the_player_deck = players_decks[0] # Temps, the player we play as is the 0th
                game_state = "players_turn"
                player_turn = 0
            elif game_state == "players_turn":

                screen.fill("purple")
                for i in board.get_points():
                    pygame.draw.circle(screen, (0,0,0), i.get_pos(), 10)
                if len(placed_pieces) != 0:
                    for i in range(len(placed_pieces)):
                        pieces_file.display_piece(screen, font, placed_pieces[i], placed_pieces_location[i], pieces_size, board.check_pos(placed_pieces_location[i]).get_direction())
                for i in range(len(the_player_deck)):
                    pieces_file.display_piece(screen,font,the_player_deck[i],(150*i+100,650),pieces_size,"up")

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]: # left click
                if selected_piece is not None:
                    for i in board.get_points():
                        if i.get_pos()[0]-pieces_size*2/3 < pygame.mouse.get_pos()[0] < i.get_pos()[0]+pieces_size*2/3 and i.get_pos()[1]-pieces_size*2/3 < pygame.mouse.get_pos()[1] < i.get_pos()[1]+pieces_size*2/3 and board.check_point(i) == "placable":
                            if len(players_decks[player_turn]) == 0:
                                break
                            placed_pieces.append(players_decks[player_turn].pop(selected_piece)) ################################### player's deck
                            placed_pieces_location.append(i.get_pos())
                            board.update_board( i, pieces_size)
                            break
                #else:
                #    for i in rack.get_points(): # Rack +/- = Board but for the player's deck
                #        if i.get_pos()[0]-pieces_size*2/3 < pygame.mouse.get_pos()[0] < i.get_pos()[0]+pieces_size*2/3 and i.get_pos()[1]-pieces_size*2/3 < pygame.mouse.get_pos()[1] < i.get_pos()[1]+pieces_size*2/3 and board.check_point(i) == "placable":
                #            selected_piece = i.get_number()
                #            break

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