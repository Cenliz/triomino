# /ᐠ｡ꞈ｡ᐟ\

def create_board()->dict:
    board = {}
    board[(500,500)] = "placable"
    return board

def update_board(board:dict, point:tuple, pieces_size:int):
    right, left, up, down = False, False, False, False
    for i in board:

        if i == (point[0]+pieces_size,point[1]):
            right = True
        if i == (point[0]-pieces_size,point[1]):
            left = True
        if i == (point[0],point[1]+pieces_size):
            down = True
        if i == (point[0]-pieces_size,point[1]-pieces_size):
            up = True

    if not right:
        board[(point[0]+pieces_size*2,point[1])] = "placable"
    if not left:
        board[(point[0]-pieces_size*2,point[1])] = "placable"
    if not down:
        board[(point[0],point[1]+pieces_size*2)] = "placable"
    if not up:
        board[(point[0],point[1]-pieces_size*2)] = "placable"
    return board