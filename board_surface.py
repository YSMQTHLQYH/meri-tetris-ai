import pygame

from board import *
from piece import *

class BoardSurface:
    def __init__(self, board, tile_size = 20):
        self.surface = pygame.Surface(((board.board_width + 10) * tile_size, board.board_height * tile_size))
        self.matrix_surface = pygame.Surface((board.board_width * tile_size, board.board_height * tile_size))
        self.board = board
        self.tile_size = tile_size
        print("height: ", self.matrix_surface.get_height())
        
        atlas = pygame.image.load("solidcolorfence.png").convert()
        scale = tile_size / atlas.get_height()

        atlas = pygame.transform.scale(atlas, (atlas.get_width() * scale, atlas.get_height() *  scale))

        self.hold_preview = PiecePreview(atlas)
        
        self.queue_preview = [PiecePreview(atlas), PiecePreview(atlas), PiecePreview(atlas), PiecePreview(atlas), PiecePreview(atlas)]
        
        self._sprite_atlas = atlas
    
    def update(self, board, piece):
        self.surface.fill((60, 60, 60))
        ts = self.tile_size
        
        #hold
        self.hold_preview.update(board.held_piece)
        self.surface.blit(self.hold_preview.surface)
        
        #queue
        for i in range(5):
            self.queue_preview[i].update(board.queue.q[i])
            self.surface.blit(self.queue_preview[i].surface, (ts * 16, ts * 5 * i))
        
        #board
        self.matrix_surface.fill((0, 0, 0))
        
        px = (0, 0)
        py = (0, 0)
        if piece is not None:
            ps = len(piece.matrix)
            px = (piece.pos[0], piece.pos[0] + ps)
            py = (piece.pos[1], piece.pos[1] + ps)
        
        for j in range(board.board_height - 1, -1, -1):
            for i in range(board.board_width):
                near_piece = False
                if (px[0] <= i < px[1]) and (py[0] <= j < py[1]):
                    #tile inside piece area
                    t = piece.matrix[j - piece.pos[1]][i - piece.pos[0]]
                    if t != 0:
                        #make falling piece different color? maybe later
                        c = t
                    else:
                        c = board.matrix[j][i]
                    near_piece = True
                        
                else:
                    #tile far from piece
                    c = board.matrix[j][i]
                
                #topout line
                if c == 0 and j == board.topout_height:
                    c = 12
                
                
                rect = pygame.rect.Rect(0, 0, ts - 1, ts)
                if c != 0:
                    self.matrix_surface.blit(self._sprite_atlas, rect.move(i * ts, (board.board_height - j - 1) * ts), rect.move((c - 1) * (ts + 1), 0))
        
        self.surface.blit(self.matrix_surface, (ts * 5, 0))        


class PiecePreview:
    def __init__(self, sprite_atlas, ts = 20):
        self.surface = pygame.Surface((ts * 4, ts * 4))
        self.atlas = sprite_atlas
        self.tile_size = ts
        self.surface.fill((0, 0, 0))
    
    def update(self, piece_type = 'z'):
        self.surface.fill((0, 0, 0))
        ts = self.tile_size
        
        if not PieceQueue.pieces_population.__contains__(piece_type):
            return
        
        p = Piece(piece_type)
        size = len(p.matrix)
        for j in range(size):
            for i in range(size):
                rect = pygame.rect.Rect(0, 0, ts - 1, ts)
                self.surface.blit(self.atlas, rect.move(i * ts, (size - j) * ts), rect.move((p.matrix[j][i] - 1) * (ts + 1), 0))