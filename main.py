from board import *
from piece import *

player = Board()
player.current_piece = Piece('z', (4, 22), 0)
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
            
        case "aa":
            player.handle_input_action(InputAction.DAS_LEFT)
        case "dd":
            player.handle_input_action(InputAction.DAS_RIGHT)
        case "ss":
            player.handle_input_action(InputAction.SOFT_DROP)
        
        case "f":
            player.handle_input_action(InputAction.HARD_DROP)
        
        case _:
            player.handle_input_action(InputAction.NOP)
        
    player.print_matrix(player.current_piece)
    if player.current_piece:
        pass
        #print(, " ", player.current_piece.pos)
    else:
        player.current_piece = Piece('z', (4, 22), 0)
        print(player.queue.get_next_piece())