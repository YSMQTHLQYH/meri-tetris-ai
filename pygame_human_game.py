import pygame

from board_surface import *
from board import *
from piece import *

class PygameHumanGame:
    def __init__(self):
        self.player = Board()
        self.player.current_piece = Piece(self.player.queue.get_next_piece(), (4, 21), PieceRotation.UP)
        self.surface = BoardSurface(self.player)

    def loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_LEFT:
                        if event.mod & pygame.KMOD_LSHIFT:
                            self.player.handle_input_action(InputAction.DAS_LEFT)
                        else:
                            self.player.handle_input_action(InputAction.MOVE_LEFT)
                    case pygame.K_RIGHT:
                        if event.mod & pygame.KMOD_LSHIFT:
                            self.player.handle_input_action(InputAction.DAS_RIGHT)
                        else:
                            self.player.handle_input_action(InputAction.MOVE_RIGHT)
                    case pygame.K_DOWN:
                        if event.mod & pygame.KMOD_LSHIFT:
                            self.player.handle_input_action(InputAction.SOFT_DROP)
                        else:
                            self.player.handle_input_action(InputAction.TAP_DOWN)
                            
                    case pygame.K_SPACE:
                        self.player.handle_input_action(InputAction.HARD_DROP)
                        
                    case pygame.K_c:
                        self.player.handle_input_action(InputAction.HOLD)
                    
                    case pygame.K_z:
                        self.player.handle_input_action(InputAction.ROTATE_CCW)
                    case pygame.K_x:
                        self.player.handle_input_action(InputAction.ROTATE_CW)
                    case pygame.K_UP:
                        self.player.handle_input_action(InputAction.ROTATE_180)
                        
                    case _:
                        self.player.handle_input_action(InputAction.NOP)
                self.player.check_gravity()
       
        return True