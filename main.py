# /ᐠ｡ꞈ｡ᐟ\

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
                

pieces = create_pieces(5)
print(pieces)

print("\n /\\     /\\\n/  0 A 0  \\")