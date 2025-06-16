from board import *
from piece import *

player = Board()
player.current_piece = Piece(player.queue.get_next_piece(), (4, 21), PieceRotation.UP)
player.print_matrix(player.current_piece)

while True:
    cmd = input("command:")
    match cmd:
        case "quit":
            break
        case "a":
            player.handle_input_action(InputAction.MOVE_LEFT)
        case "d":
            player.handle_input_action(InputAction.MOVE_RIGHT)
        case "s":
            player.handle_input_action(InputAction.TAP_DOWN)
        
        case "q":
            player.handle_input_action(InputAction.ROTATE_CCW)
        case "e":
            player.handle_input_action(InputAction.ROTATE_CW)
        case "w":
            player.handle_input_action(InputAction.ROTATE_180)
        
        case "aa":
            player.handle_input_action(InputAction.DAS_LEFT)
        case "dd":
            player.handle_input_action(InputAction.DAS_RIGHT)
            
        case "ss":
            player.handle_input_action(InputAction.SOFT_DROP)
        case "f":
            player.handle_input_action(InputAction.HARD_DROP)
            
        case "r":
            player.handle_input_action(InputAction.HOLD)
        
        case _:
            player.handle_input_action(InputAction.NOP)
        
    player.print_matrix(player.current_piece)
    if player.current_piece:
        pass
        #print(, " ", player.current_piece.pos)
    else:
        player.spawn_next_piece()