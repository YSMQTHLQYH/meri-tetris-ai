from enum import Enum
class PieceRotation(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

class Piece:
    matrix = [[0, 0, 0],
              [0, 8, 0],
              [0, 0, 0]]
    
    piece_type = 'z'
    pos = (0, 0)
    rot:PieceRotation = PieceRotation.UP
    
    def __init__(self, _type = 'z', _pos = (0, 0), _rot:PieceRotation = PieceRotation.UP):
        self.piece_type = _type
        self.pos = _pos
        self.rot = _rot
        
        self.update_matrix()
    
    def update_matrix(self):
        match self.piece_type:
            case 'z':
                #everything flipped because (0, 0) is bottom left
                match self.rot:
                    case PieceRotation.UP:
                        self.matrix = [
                            [ 0, 0, 0],
                            [ 0, 1, 1],
                            [ 1, 1, 0]
                        ]
                        #effectve_origin = (0, 0)
                    case PieceRotation.RIGHT:
                        self.matrix = [
                            [ 0, 1, 0],
                            [ 0, 1, 1],
                            [ 0, 0, 1]
                        ]
                        #effectve_origin = (1, 0)
                    case PieceRotation.DOWN:
                        self.matrix = [
                            [ 0, 1, 1],
                            [ 1, 1, 0],
                            [ 0, 0, 0]
                        ]
                        #effectve_origin = (0, 1)
                    case PieceRotation.LEFT:
                        self.matrix = [
                            [ 1, 0, 0],
                            [ 1, 1, 0],
                            [ 0, 1, 0]
                        ]
                        #effectve_origin = (0, 0)
            case 'l':
                match(self.rot):
                    case PieceRotation.UP:
                        self.matrix = [
                            [ 0, 0, 0],
                            [ 2, 2, 2],
                            [ 0, 0, 2]
                        ]
                        #effectve_origin = (0, 0)
                    case PieceRotation.RIGHT:
                        self.matrix = [
                            [ 0, 2, 2],
                            [ 0, 2, 0],
                            [ 0, 2, 0]
                        ]
                        #effectve_origin = (1, 0)
                    case PieceRotation.DOWN:
                        self.matrix = [
                            [ 2, 0, 0],
                            [ 2, 2, 2],
                            [ 0, 0, 0]
                        ]
                        #effectve_origin = (0, 1)
                    case PieceRotation.LEFT:
                        self.matrix = [
                            [ 0, 2, 0],
                            [ 0, 2, 0],
                            [ 2, 2, 0]
                        ]
                        #effectve_origin = (0, 0)
            case 'o':
                self.matrix = [
                    [ 3, 3],
                    [ 3, 3]
                ]
                #effectve_origin = (0, 0)
            case 's':
                match(self.rot):
                    case PieceRotation.UP:
                        self.matrix = [
                            [ 0, 0, 0],
                            [ 4, 4, 0],
                            [ 0, 4, 4]
                        ]
                        #effectve_origin = (0, 0)
                    case PieceRotation.RIGHT:
                        self.matrix = [
                            [ 0, 0, 4],
                            [ 0, 4, 4],
                            [ 0, 4, 0]
                        ]
                        #effectve_origin = (1, 0)
                    case PieceRotation.DOWN:
                        self.matrix = [
                            [ 4, 4, 0],
                            [ 0, 4, 4],
                            [ 0, 0, 0]
                        ]
                        #effectve_origin = (0, 1)
                    case PieceRotation.LEFT:
                        self.matrix = [
                            [ 0, 4, 0],
                            [ 4, 4, 0],
                            [ 4, 0, 0]
                        ]
                        #effectve_origin = (0, 0)
            case 'i':
                match(self.rot):
                    case PieceRotation.UP:
                        self.matrix = [
                            [ 0, 0, 0, 0],
                            [ 0, 0, 0, 0],
                            [ 5, 5, 5, 5],
                            [ 0, 0, 0, 0]
                        ]
                        #effectve_origin = (0, 1)
                    case PieceRotation.RIGHT:
                        self.matrix = [
                            [ 0, 0, 5, 0],
                            [ 0, 0, 5, 0],
                            [ 0, 0, 5, 0],
                            [ 0, 0, 5, 0]
                        ]
                        #effectve_origin = (2, 0)
                    case PieceRotation.DOWN:
                        self.matrix = [
                            [ 0, 0, 0, 0],
                            [ 5, 5, 5, 5],
                            [ 0, 0, 0, 0],
                            [ 0, 0, 0, 0]
                        ]
                        #effectve_origin = (0, 2)
                    case PieceRotation.LEFT:
                        self.matrix = [
                            [ 0, 5, 0, 0],
                            [ 0, 5, 0, 0],
                            [ 0, 5, 0, 0],
                            [ 0, 5, 0, 0]
                        ]
                        #effectve_origin = (1, 0)
            case 'j':
                match(self.rot):
                    case PieceRotation.UP:
                        self.matrix = [
                            [ 0, 0, 0],
                            [ 6, 6, 6],
                            [ 6, 0, 0]
                        ]
                        #effectve_origin = (0, 0)
                    case PieceRotation.RIGHT:
                        self.matrix = [
                            [ 0, 6, 0],
                            [ 0, 6, 0],
                            [ 0, 6, 6]
                        ]
                        #effectve_origin = (1, 0)
                    case PieceRotation.DOWN:
                        self.matrix = [
                            [ 0, 0, 6],
                            [ 6, 6, 6],
                            [ 0, 0, 0]
                        ]
                        #effectve_origin = (0, 1)
                    case PieceRotation.LEFT:
                        self.matrix = [
                            [ 6, 6, 0],
                            [ 0, 6, 0],
                            [ 0, 6, 0]
                        ]
                        #effectve_origin = (0, 0)
            case 't':
                match(self.rot):
                    case PieceRotation.UP:
                        self.matrix = [
                            [ 0, 0, 0],
                            [ 7, 7, 7],
                            [ 0, 7, 0]
                        ]
                        #effectve_origin = (0, 0)
                    case PieceRotation.RIGHT:
                        self.matrix = [
                            [ 0, 7, 0],
                            [ 0, 7, 7],
                            [ 0, 7, 0]
                        ]
                        #effectve_origin = (1, 0)
                    case PieceRotation.DOWN:
                        self.matrix = [
                            [ 0, 7, 0],
                            [ 7, 7, 7],
                            [ 0, 0, 0]
                        ]
                        #effectve_origin = (0, 1)
                    case PieceRotation.LEFT:
                        self.matrix = [
                            [ 0, 7, 0],
                            [ 7, 7, 0],
                            [ 0, 7, 0]
                        ]
                        #effectve_origin = (0, 0)
    
    def get_kick_offset(self, start_rot:PieceRotation, target_rot:PieceRotation, check):
        check_array = [(0, 0)]
        if(self.piece_type == 'o'):
            return (0, 0)
        elif(self.piece_type == 'i'):
            match start_rot:
                case PieceRotation.UP:
                    match(target_rot):
                        case PieceRotation.RIGHT:
                            check_array = [(0, 0), (-2, 0), (1, 0), (-2, -1), (1, 2)]
                        case PieceRotation.LEFT:
                            check_array = [(0, 0), (-1, 0), (2, 0), (-1, 2), (2, -1)]
                        case PieceRotation.DOWN:
                            check_array = [(0, 0), (-1, 0), (-2, 0), (1, 0), (2, 0), (0, 1)]
                case PieceRotation.RIGHT:
                    match(target_rot):
                        case PieceRotation.DOWN:
                            check_array = [(0, 0), (-1, 0), (2, 0), (-1, 2), (2, -1)]
                        case PieceRotation.UP:
                            check_array = [(0, 0), (2, 0), (-1, 0), (2, 1), (-1, -2)]
                        case PieceRotation.LEFT:
                            check_array = [(0, 0), (0, 1), (0, 2), (0, -1), (0, -2), (-1, 0)]
                case PieceRotation.DOWN:
                    match(target_rot):
                        case PieceRotation.LEFT:
                            check_array = [(0, 0), (2, 0), (-1, 0), (2, 1), (-1, -2)]
                        case PieceRotation.RIGHT:
                            check_array = [(0, 0), (1, 0), (-2, 0), (1, -2), (-2, 1)]
                        case PieceRotation.UP:
                            check_array = [(0, 0), (1, 0), (2, 0), (-1, 0), (-2, 0), (0, -1)]
                case PieceRotation.LEFT:
                    match(target_rot):
                        case PieceRotation.UP:
                            check_array = [(0, 0), (1, 0), (-2, 0), (1, -2), (-2, 1)]
                        case PieceRotation.DOWN:
                            check_array = [(0, 0), (-2, 0), (1, 0), (-2, -1), (1, 2)]
                        case PieceRotation.RIGHT:
                            check_array = [(0, 0), (0, 1), (0, 2), (0, -1), (0, -2), (1, 0)]
        else:
            match start_rot:
                case PieceRotation.UP:
                    match(target_rot):
                        case PieceRotation.RIGHT:
                            check_array = [(0, 0), (-1, 0), (-1, 1), (0, -2), (-1, -2)]
                        case PieceRotation.LEFT:
                            check_array = [(0, 0), (1, 0), (1, 1), (0, -2), (1, -2)]
                        case PieceRotation.DOWN:
                            check_array = [(0, 0), (0, 1), (1, 1), (-1, 1), (1, 0), (-1, 0)]
                case PieceRotation.RIGHT:
                    match(target_rot):
                        case PieceRotation.DOWN:
                            check_array = [(0, 0), (1, 0), (1, -1), (0, 2), (1, 2)]
                        case PieceRotation.UP:
                            check_array = [(0, 0), (1, 0), (1, -1), (0, 2), (1, 2)]
                        case PieceRotation.LEFT:
                            check_array = [(0, 0), (1, 0), (1, 2), (1, 1), (0, 2), (0, 1)]
                case PieceRotation.DOWN:
                    match(target_rot):
                        case PieceRotation.LEFT:
                            check_array = [(0, 0), (1, 0), (1, 1), (0, -2), (1, -2)]
                        case PieceRotation.RIGHT:
                            check_array = [(0, 0), (-1, 0), (-1, 1), (0, -2), (-1, -2)]
                        case PieceRotation.UP:
                            check_array = [(0, 0), (0, -1), (-1, -1), (1, -1), (-1, 0), (1, 0)]
                case PieceRotation.LEFT:
                    match(target_rot):
                        case PieceRotation.UP:
                            check_array = [(0, 0), (-1, 0), (-1, -1), (0, 2), (-1, 2)]
                        case PieceRotation.DOWN:
                            check_array = [(0, 0), (-1, 0), (-1, -1), (0, 2), (-1, 2)]
                        case PieceRotation.RIGHT:
                            check_array = [(0, 0), (-1, 0), (-1, 2), (-1, 1), (0, 2), (0, 1)]
        if len(check_array) > check:
            return check_array[check]
        else:
            return check_array[-1]