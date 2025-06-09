class Piece:
    matrix = [[1, 1, 0],
              [0, 1, 1],
              [0, 0, 0]]
    
    piece_type = 'z'
    pos = (0, 0)
    rot = 0
    
    def __init__(self, _type = 'z', _pos = (0, 0), _rot = 0):
        piece_type = _type
        self.pos = _pos
        self.rot = _rot