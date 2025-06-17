from board import *
from piece import *

class CommandLineGame:
    def __init__(self):
        self.player = Board()
        self.player.current_piece = Piece(self.player.queue.get_next_piece(), (4, 21), PieceRotation.UP)
        self.player.print_matrix(self.player.current_piece)

    def loop(self):
        cmd = input("command:")
        match cmd:
            case "quit":
                return False
            case "a":
                self.player.handle_input_action(InputAction.MOVE_LEFT)
            case "d":
                self.player.handle_input_action(InputAction.MOVE_RIGHT)
            case "s":
                self.player.handle_input_action(InputAction.TAP_DOWN)
            
            case "q":
                self.player.handle_input_action(InputAction.ROTATE_CCW)
            case "e":
                self.player.handle_input_action(InputAction.ROTATE_CW)
            case "w":
                self.player.handle_input_action(InputAction.ROTATE_180)
            
            case "aa":
                self.player.handle_input_action(InputAction.DAS_LEFT)
            case "dd":
                self.player.handle_input_action(InputAction.DAS_RIGHT)
                
            case "ss":
                self.player.handle_input_action(InputAction.SOFT_DROP)
            case "f":
                self.player.handle_input_action(InputAction.HARD_DROP)
                
            case "r":
                self.player.handle_input_action(InputAction.HOLD)
            
            case _:
                self.player.handle_input_action(InputAction.NOP)
            
        self.player.check_gravity()
        self.player.print_matrix(self.player.current_piece)
        return True

game = CommandLineGame()
while game.loop():
    pass