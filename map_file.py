# /ᐠ｡ꞈ｡ᐟ\

class Point():
    def __init__(self, pos:tuple, direction:str):
        self.__pos = pos
        self.__direction = direction
        self.__state = "placable"

    def get_pos(self)->tuple:
        return self.__pos
    
    def get_direction(self)->str:
        return self.__direction
    
    def get_state(self)->str:
        return self.__state
    
    def change_state(self)->None:
        self.__state = "placed"
        return
    
class Board():
    def __init__(self):
        self.__points = [Point((500,500), "up")]
    
    def get_points(self):
        return self.__points
    
    def create_point(self, pos:tuple, pieces_size:float, direction:str):
        if direction == "up":
            self.__points.append(Point(pos, "up"))
        else:
            self.__points.append(Point(pos, "down"))
        return
    
    def check_point(self, point:Point)->str:
        return point.get_state()
    
    def check_pos(self, pos:tuple)->Point|None:
        for i in self.__points:
            if i.get_pos() == pos:
                return i
        return None

    def update_board(self, point:Point, pieces_size:float):
        point.change_state()
        size = pieces_size * 1.5
        x_offset = pieces_size*0.25
        y_offset = pieces_size*0.75

        if point.get_direction() == "up":
            if self.check_pos((point.get_pos()[0]+size-x_offset,point.get_pos()[1]-y_offset)) is None: # right
                self.create_point((point.get_pos()[0]+size-x_offset,point.get_pos()[1]-y_offset), pieces_size, "down")

            if self.check_pos((point.get_pos()[0]-size+x_offset,point.get_pos()[1]-y_offset)) is None: # left
                self.create_point((point.get_pos()[0]-size+x_offset,point.get_pos()[1]-y_offset), pieces_size, "down")

            if self.check_pos((point.get_pos()[0],point.get_pos()[1]+size)) is None : # down
                self.create_point((point.get_pos()[0],point.get_pos()[1]+size), pieces_size, "down")
        
        
        else:
            if self.check_pos((point.get_pos()[0]+size-x_offset,point.get_pos()[1]+y_offset)) is None: # right
                self.create_point((point.get_pos()[0]+size-x_offset,point.get_pos()[1]+y_offset), pieces_size, "up")

            if self.check_pos((point.get_pos()[0]-size+x_offset,point.get_pos()[1]+y_offset)) is None: # left
                self.create_point((point.get_pos()[0]-size+x_offset,point.get_pos()[1]+y_offset), pieces_size, "up")

            if self.check_pos((point.get_pos()[0],point.get_pos()[1]-size)) is None : # up
                self.create_point((point.get_pos()[0],point.get_pos()[1]-size), pieces_size, "up")