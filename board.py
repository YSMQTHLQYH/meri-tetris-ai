import random
from enum import Enum
from piece import *

class InputAction(Enum):
    NOP = 0
    MOVE_LEFT = 1
    MOVE_RIGHT = 2
    DAS_LEFT = 3
    DAS_RIGHT = 4
    ROTATE_CCW = 5
    ROTATE_CW = 6
    ROTATE_180 = 7
    HOLD = 8
    TAP_DOWN = 9
    SOFT_DROP = 10
    HARD_DROP = 11

class ClearType(Enum):
    SKIM = 0
    ALL_SPIN = 1
    T_SPIN_MINI = 2
    T_SPIN = 3
    
class PieceQueue:
    pieces_population = ["z", "l", "o", "s", "i", "j", "t"]
    
    def __init__(self, rng_seed = None):
        self.rng = random.Random(rng_seed)
        self.q = []
        self.generate_next_bag()
    
    def generate_next_bag(self):
        self.q += self.rng.sample(self.pieces_population, 7)
    
    def get_next_piece(self):
        p = self.q.pop(0)
        if len(self.q) < 10:
            self.generate_next_bag()
        return p

class Board:
    board_width = 10
    board_height = 25
    topout_height = 20
    
    def __init__(self, rng_seed = None):
        self.matrix = [[0] * self.board_width for _ in range(self.board_height)]
        self.current_piece = None
        self.held_piece = None
        self.queue = PieceQueue(rng_seed)
        
        self.can_hold:bool = True #true if last piece was from hold, so you cant swap the same two pieces forever
        self.combo_count =  0
        self._last_move_was_rotate:bool = False #used for checking T-spins
        self._last_move_kick = 0 #used for checking T-spins
    
    
    def spawn_piece(self, p):
        self.current_piece = Piece(p, (4, self.topout_height + 1), PieceRotation.UP)
    
    def spawn_next_piece(self):
        self.spawn_piece(self.queue.get_next_piece())
        self.can_hold = True 
    
    #retuns number of lines cleared, does actually do the line clear
    def check_line_clear(self):
        clear_count = 0
        for j in range(self.board_height - 1, -1, -1):
            line_full = True
            for i in range(self.board_width):
                if self.matrix[j][i] == 0:
                    line_full = False
            
            if line_full:
                print("Line: ", j, "Clear: ", line_full)
                for k in range(j, self.board_height - 1):
                    self.matrix[k] = self.matrix[k + 1][:]
                
                clear_count += 1
        
        return clear_count
        
    def place_piece(self, piece):
        if piece is None:
            return

        #T-spin check
        clear_type:ClearType = ClearType.SKIM
        if self._last_move_was_rotate:
            if piece.piece_type == 't':
                corners = (
                    self.get_tile(piece.pos[0], piece.pos[1] + 2),      #top left
                    self.get_tile(piece.pos[0] + 2, piece.pos[1] + 2),  #top right
                    self.get_tile(piece.pos[0] + 2, piece.pos[1]),      #bottom right
                    self.get_tile(piece.pos[0], piece.pos[1])           #bottom left
                )
                
                if corners.count(0) <= 1:
                    if self._last_move_kick >= 3:
                        clear_type = ClearType.T_SPIN #execption for tst kick
                    else:
                        tspin_full = False
                        match piece.rot:
                            case PieceRotation.UP:
                                tspin_full = corners[0] and corners[1]
                            case PieceRotation.RIGHT:
                                tspin_full = corners[1] and corners[2]
                            case PieceRotation.DOWN:
                                tspin_full = corners[2] and corners[3]
                            case PieceRotation.LEFT:
                                tspin_full = corners[3] and corners[0]
                        if tspin_full:
                            clear_type = ClearType.T_SPIN
                        else:
                            clear_type = ClearType.T_SPIN_MINI
                    print("tspin: ", clear_type)
            else:
                #all spins might need a better check dunno
                if self.check_piece_collision(piece, (1, 0)) and self.check_piece_collision(piece, (-1, 0)):
                    clear_type = ClearType.ALL_SPIN
        
        print("Spin? ",clear_type)

        #actually place piece
        for j in range(len(piece.matrix)):
            for i in range(len(piece.matrix[j])):
                t = piece.matrix[j][i]
                if t != 0:
                    self.matrix[j + piece.pos[1]][i + piece.pos[0]] = t
        self.current_piece = None
        
        #check line clears
        lines_cleared = self.check_line_clear()
        print("lines_cleared: ",lines_cleared)
        if lines_cleared:
            self.combo_count += 1
        else:
            self.combo_count = 0
        print("combo count: ",self.combo_count)
        
        
        #check for perfect clear
        pc:bool = True
        for i in range(self.board_height):
            if any(self.matrix[i]):
                pc = False
                break
        print("is pc test: ", pc)
        
    
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

    #returns 10 if outside of board, as it's considered as occupied
    def get_tile(self, x, y):
        if x < 0 or x >= self.board_width or y < 0 or y >= self.board_height:
            return 10
        return self.matrix[y][x]
        
    #moves piece by distance, returns true if the piece was moved, false if it intersected the board            
    def move_piece(self, piece, offset = (0, 0)):
        if piece is None:
            return False
        
        if self.check_piece_collision(piece, offset):
            return False
        else:
            #stoopid python why is tuple + operator concatenation instead of addition?
            piece.pos = piece.pos[0] + offset[0], piece.pos[1] + offset[1]
            self._last_move_was_rotate = False
            self._last_move_kick = 0
            return True
    
    #das/hard drop movement
    def auto_move_piece(self, piece, direction = (0, 0)):
        if piece is None:
            return
        
        while self.move_piece(piece, direction):
            pass
    
    #returns tuple, first is if the rotation was successful and second is kick number (0 if no kick needed)
    def rotate_piece(self, piece, target_rot:PieceRotation):
        if piece is None:
            return
        
        start_rot = piece.rot
        if start_rot == target_rot:
            return
        
        success = False
        
        piece.rot = target_rot
        piece.update_matrix()
        
        i = 0
        for i in range(6):
            print("kick: ", i, " offset: ", piece.get_kick_offset(start_rot, target_rot, i))
            success = self.move_piece(piece, piece.get_kick_offset(start_rot, target_rot, i))
            print("success: ", success)
            if success:
                break
        
        
        if success:
            self._last_move_kick = i
            
            self._last_move_was_rotate = True
            return (True, i)
        else:
            piece.rot = start_rot
            piece.update_matrix()
            return (False, 0)
    

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
                if not self.can_hold:
                    return
                
                t = self.current_piece.piece_type
                if self.held_piece in PieceQueue.pieces_population:
                    self.spawn_piece(self.held_piece)
                else:
                    self.spawn_next_piece()
                self.held_piece = t
                self.can_hold = False
            
            case InputAction.ROTATE_CCW:
                match self.current_piece.rot:
                    case PieceRotation.UP:
                        self.rotate_piece(self.current_piece, PieceRotation.LEFT)
                    case PieceRotation.RIGHT:
                        self.rotate_piece(self.current_piece, PieceRotation.UP)
                    case PieceRotation.DOWN:
                        self.rotate_piece(self.current_piece, PieceRotation.RIGHT)
                    case PieceRotation.LEFT:
                        self.rotate_piece(self.current_piece, PieceRotation.DOWN)     
            
            case InputAction.ROTATE_CW:
                match self.current_piece.rot:
                    case PieceRotation.UP:
                        self.rotate_piece(self.current_piece, PieceRotation.RIGHT)
                    case PieceRotation.RIGHT:
                        self.rotate_piece(self.current_piece, PieceRotation.DOWN)
                    case PieceRotation.DOWN:
                        self.rotate_piece(self.current_piece, PieceRotation.LEFT)
                    case PieceRotation.LEFT:
                        self.rotate_piece(self.current_piece, PieceRotation.UP)
            
            case InputAction.ROTATE_180:
                match self.current_piece.rot:
                    case PieceRotation.UP:
                        self.rotate_piece(self.current_piece, PieceRotation.DOWN)
                    case PieceRotation.RIGHT:
                        self.rotate_piece(self.current_piece, PieceRotation.LEFT)
                    case PieceRotation.DOWN:
                        self.rotate_piece(self.current_piece, PieceRotation.UP)
                    case PieceRotation.LEFT:
                        self.rotate_piece(self.current_piece, PieceRotation.RIGHT)
    
    def print_matrix(self, piece = None):
        print("\n", self.queue.q, "\n")
        print("hold: ", self.held_piece, "\n")
        px = (0, 0)
        py = (0, 0)
        if piece is not None:
            ps = len(piece.matrix)
            px = (piece.pos[0], piece.pos[0] + ps)
            py = (piece.pos[1], piece.pos[1] + ps)
        
        for j in range(self.board_height - 1, -1, -1):
            out = "|"
            for i in range(self.board_width):
                near_piece = False
                if (px[0] <= i < px[1]) and (py[0] <= j < py[1]):
                    #tile inside piece area
                    t = piece.matrix[j - piece.pos[1]][i - piece.pos[0]]
                    if t != 0:
                        c = -1
                    else:
                        c = self.matrix[j][i]
                    near_piece = True
                        
                else:
                    #tile far from piece
                    c = self.matrix[j][i]
                
                #topout line
                if c == 0 and j == self.topout_height:
                    c = -2
                
                match c:
                    case 0:
                        if near_piece: out += "| |"
                        else: out += " . "
                    case -1:
                        out += "|X|"
                    case -2:
                        if near_piece: out += "| |"
                        else: out += "---"
                    case _:
                        if near_piece: out += "|" + str(c) + "|"
                        else: out += ":" + str(c) + ":"
            out += "|"
            print(out)