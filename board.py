import random
from enum import Enum
class InputAction(Enum):
    NOP = 0
    MOVE_LEFT = 1
    MOVE_RIGHT = 2
    DAS_LEFT = 3
    DAS_RIGHT = 4
    ROTATE_LEFT = 5
    ROTATE_RIGHT = 6
    ROTATE_180 = 7
    HOLD = 8
    TAP_DOWN = 9
    SOFT_DROP = 10
    HARD_DROP = 11
    
class PieceQueue:
    _pieces_population = ["z", "l", "o", "s", "i", "j", "t"]
    
    def __init__(self, rng_seed = None):
        self.rng = random.Random(rng_seed)
        self.q = []
        self.generate_next_bag()
    
    def generate_next_bag(self):
        self.q += self.rng.sample(self._pieces_population, 7)
    
    def get_next_piece(self):
        p = self.q.pop(0)
        if len(self.q) < 10:
            self.generate_next_bag()
        return p

class Board:
    board_width = 10
    board_height = 24
    topout_height = 20
    
    def __init__(self, rng_seed = None):
        self.matrix = [[0] * self.board_width for _ in range(self.board_height)]
        self.current_piece = None
        self.queue = PieceQueue(rng_seed)
        
    def place_piece(self, piece):
        if piece is None:
            return

        for j in range(len(piece.matrix)):
            for i in range(len(piece.matrix[j])):
                t = piece.matrix[j][i]
                if t != 0:
                    self.matrix[j + piece.pos[1]][i + piece.pos[0]] = t
        
        self.current_piece = None
    
    #returns true if piece moved by offset intersects with anything in the board
    #also returns true if piece has any tile outside of the board
    def check_piece_collision(self, piece, offset = (0, 0)):
        if piece is None:
            return False
        
        for j in range(len(piece.matrix)):
            for i in range(len(piece.matrix[j])):
                
                if piece.matrix[j][i] == 0:
                    continue
                
                x = i + piece.pos[0] + offset[0]
                y = j + piece.pos[1] + offset[1]
                
                if x >= 0 and x < self.board_width and y >= 0 and y < self.board_height:
                    if self.matrix[y][x] != 0:
                        print("collision in: ", x, " ",y)
                        return True
                else:
                    return True
                
        return False
        
    #moves piece by distance, returns true if the piece was moved, false if it intersected the board            
    def move_piece(self, piece, offset = (0, 0)):
        if piece is None:
            return False
        
        if self.check_piece_collision(piece, offset):
            return False
        else:
            #stoopid python why is tuple + operator concatenation instead of addition?
            piece.pos = piece.pos[0] + offset[0], piece.pos[1] + offset[1]
            return True
    
    #das/hard drop movement
    def auto_move_piece(self, piece, direction = (0, 0)):
        if piece is None:
            return
        
        while self.move_piece(piece, direction):
            pass
    
    def print_matrix(self, piece = None):
        print("\n", self.queue.q, "\n")
        px = (0, 0)
        py = (0, 0)
        if piece is not None:
            ps = len(piece.matrix)
            px = (piece.pos[0], piece.pos[0] + ps)
            py = (piece.pos[1], piece.pos[1] + ps)
        
        for j in range(self.board_height - 1, -1, -1):
            out = "|"
            for i in range(self.board_width):
                if (px[0] <= i < px[1]) and (py[0] <= j < py[1]):
                    #tile inside piece area
                    t = piece.matrix[j - piece.pos[1]][i - piece.pos[0]]
                    if t != 0:
                        c = -1
                    else:
                        c = self.matrix[j][i]
                        
                else:
                    #tile far from piece
                    c = self.matrix[j][i]
                
                #topout line
                if c == 0 and j == self.topout_height:
                    c = -2
                
                match c:
                    case 0:
                        out += " . "
                    case -1:
                        out += " X "
                    case -2:
                        out += "---"
                    case _:
                        out += "|" + str(c) + "|"
            out += "|"
            print(out)
    
    def handle_input_action(self, cmd:InputAction):
        match cmd:
            case InputAction.NOP:
                pass
            
            case InputAction.MOVE_LEFT:
                self.move_piece(self.current_piece, (-1, 0))
                
            case InputAction.MOVE_RIGHT:
                self.move_piece(self.current_piece, (1, 0))
            
            case InputAction.DAS_LEFT:
                self.auto_move_piece(self.current_piece, (-1, 0))
                
            case InputAction.DAS_RIGHT:
                self.auto_move_piece(self.current_piece, (1, 0))
            
            case InputAction.TAP_DOWN:
                self.move_piece(self.current_piece, (0, -1))
                
            case InputAction.SOFT_DROP:
                self.auto_move_piece(self.current_piece, (0, -1))
            
            case InputAction.HARD_DROP:
                self.auto_move_piece(self.current_piece, (0, -1))
                self.place_piece(self.current_piece)
            
            case InputAction.HOLD:
                pass
            
            case InputAction.ROTATE_LEFT:
                pass
            
            case InputAction.ROTATE_RIGHT:
                pass
            
            case InputAction.ROTATE_180:
                pass