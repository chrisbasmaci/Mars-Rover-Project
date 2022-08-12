from enum import Enum
import numpy as np
from itertools import chain
from typing import List
from retry import retry

global grid

class Grid:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __repr__(self):
        return self.x+','+self.y



    def get_axes(self):
        xy = [self.x, self.y]
        print('GRID:',xy)
        return xy

class Direction(Enum):
    LEFT = (0, 'L')
    RIGHT = (1, 'R')
    MOVE = (2, 'M')

    def __init__(self, number, shortname):
        self.number = number
        self.shortname = shortname

    @staticmethod
    def tolist():
        return list(map(lambda c: c.shortname, Direction))

class Compass(Enum):
    NORTH = (0, 'N')
    WEST = (1, 'W')
    SOUTH = (2, 'S')
    EAST = (3, 'E')
    def __init__(self, id, shortname):
        self.id = id
        self.shortname = shortname

    @staticmethod
    def tovalue():
        return list(map(lambda c: c.value, Compass))

    @staticmethod
    def tolist():
        return list(map(lambda c: c.shortname, Compass))

    @staticmethod
    def toint():
        return list(map(lambda c: c.id, Compass))

    def succ(self):
        int_list = Compass.toint()
        max_int = max(int_list)
        min_int = min(int_list)
        v = self.id +1
        if v > max_int:
            v = min_int

        for thing in self.tovalue():
            if v in thing:
                return thing

    def pred(self):

        int_list = Compass.toint()
        max_int = max(int_list)
        min_int = min(int_list)
        v = self.id - 1
        if v < min_int:
            v = max_int

        for thing in self.tovalue():
            if v in thing:
                return thing
class Rover:
    def __init__(self, x: int, y: int, compass):
        global grid
        self.x = x
        self.y = y
        self.compass = compass

        compass_pairs = Compass.tovalue()

        for varr in compass_pairs:
            if compass in varr:
                self.compass = Compass(varr)
                


    def left(self):
        new_compass = Compass((self.compass.succ()))
        self.compass = new_compass

    def right(self):
        new_compass = Compass((self.compass.pred()))
        self.compass = new_compass


    def check_input(self):
        compass_perimeter = False
        compass_limiter = Compass.tovalue()
        print(self.compass)

        for a in compass_limiter:
            if self.compass == a:
                compass_perimeter = True
                return compass_perimeter

        #if int(grid.x) < int(self.x) or int(self.y) < int(self.y):
        #    raise Exception('Outside range')
        #else:
        #    pass

        if compass_perimeter == False:
            raise Exception(f'Try using the directions {compass_limiter}')

        else:
            pass


    def move_forward(self):

        if self.compass == Compass.NORTH:
            self.y = self.y + 1
            return self.x,self.y
        elif self.compass == Compass.SOUTH:
            self.y = self.y - 1
            return self.x,self.y
        elif self.compass == Compass.WEST:
            self.x = self.x - 1
            return self.x,self.y
        elif self.compass == Compass.EAST:
            self.x = self.x + 1
            return self.x,self.y
        else:
            pass

    def explorer(self, *directive):
        self.directive = directive

        set_directive = set(*directive)

        move_options = Direction.tolist()
        set_move_options = set(move_options)

        inter = set_directive.difference(set_move_options)

        if inter != set():
         print(f'Hata patladın neden mi {move_options} komutları dışında başka bir komut gönderemezsin.')
        else:
            pass

        for a in list(*directive):
            if a == Direction.LEFT.shortname:
                self.left()
            elif a == Direction.RIGHT.shortname:
                self.right()
            elif a == Direction.MOVE.shortname:
                self.move_forward()

        print('Son Konum:',self.x, self.y, self.compass)
        return self.x, self.y


class InputManager:
    def __init__(self):
        self.rover1 = Rover(0,0,'N')
        self. directive_input = []

    def grid_input(self):
        grid = Grid(*input('Enter the Top right x and y coordinates of the grid\n'
                           '(separated wih a comma):\n ').split(','))
        print(grid)
        grid.x, grid.y = int(grid.x), int(grid.y)
    def rover_input(self):

        rover_values= input('Enter the x,y and the direction(N,E,W,S) of the rover:\n'
                                '(separated with a comma)\n')
        rover_values = rover_values.split(',')
        self.rover1 = Rover(int(rover_values[0]), int(rover_values[1]),str(rover_values[2]))

        self.rover1.check_input()
        print('ROVER:', rover_values, '\n')
        return self.rover1

    def movement_input(self):
        directivecore = input("Enter the movement chain for the rover:\n"
                              "(L: turn left)\n"
                              "(R: Turn right)\n"
                              "(M: Move forward)\n"
                              "(Separated with a comma)\n")
        self.directive_input = directivecore.split(",")
        return self.directive_input

    def moving_rover(self):
        self.rover1.explorer(self.directive_input)






if __name__ == '__main__':
    Printer = InputManager()
    # Grid user input
    Printer.grid_input()
    # Rover User input in a never ending loop
    Printer.rover_input()
    # movement of the rover
    Printer.movement_input()
    Printer.moving_rover()






##BASKA YONTEM----
#move_options = [y for x in a for y in x if isinstance(y, str)]
###L,M,L,M,L,M,L,M,M
#M,M,R,M,M,R,M,R,R,M