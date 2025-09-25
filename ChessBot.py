import chess
import random

class player:
    def __init__(self, color: bool, board: chess.Board):
     self.board = board
     self.color = color
    
    def make_move(self, board: chess.Board, move: chess.Move):
        piece =board.piece_at(move.from_square)
        if piece.color == self.color:
           board.push(move)
           return move
        else:
            raise Exception("It's not your turn!")  


def pick_move(board: chess.Board):
    moves = []
    max_move_score = -99
    for m in board.legal_moves: # for each legal move
        #calculate the move's score
        current_move_score = 0 #reset the score
        if board.is_capture(m): #if the move captures a piece
            current_move_score += 1 #increase its score by one
            #add variable increases based on captured piece?
        if board.is_en_passant(m): #if the move is en passant
            current_move_score += 1 #increase its score by one (will total two bc en passant is necesarily a capture)
            #because funny. everybody loves en passant :3
        if board.gives_check(m): #if the move puts the other side in check
            current_move_score += 3 #increase its score by three
        #add or dont based on move's score
        if current_move_score > max_move_score: #if m is better than the current movepool
            max_move_score = current_move_score #update max move score
            moves = [] #empty the movepool
        if current_move_score == max_move_score:
            moves.append(m) #add m to movepool
    return moves[random.randrange(0,len(moves))]




#main action starts here
board = chess.Board()
x = input("Computer Player? (w=white/b=black):") #get player and store as variable
if x == 'w':#choose a side
    player_color = chess.WHITE
else:
    player_color = chess.BLACK
computer_player = player(player_color, board)
human_player = player(not player_color, board)
print("Starting FEN position? (hit ENTER for standard starting position):")
pos = input()
try: #try to set the board state from the input
    board.set_fen(pos)
except ValueError: #if the 
    if (not pos == ""): #(dont show error if they hit enter like the instructions said)
        print("Invalid FEN! Starting from default board.") #show error and continue
print(board)
if computer_player.color: #if computer is playing as white, make the first move
    move = pick_move(board)
    board.push(move)
    print(move)
    print(board)
    print(board.fen())
#gameplay loop:
while (not board.is_game_over()): #while not in checkmate/stalemate/etc
    if human_player.color:
        move = input("White:")
    else:
        move = input("Black:")
    move = chess.Move.from_uci(move)
    human_player.make_move(board, move)
    print(board)
    print(board.fen())
    move = pick_move(board)
    board.push(move)
    print(move)
    print(board)
    print(board.fen())

    
    



        

    




