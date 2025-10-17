import chess
import random

class player:
    def __init__(self, color: bool, board: chess.Board):
     self.board = board
     self.color = color
    
    def make_move(self, board: chess.Board, move: chess.Move): 
        piece = board.piece_at(move.from_square)
        if piece.color == self.color:
           board.push(move)
           return move
        else:
            raise Exception("It's not your turn!")  

def old_pick_move(board: chess.Board):
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
        #add to pool or dont based on move's score
        if current_move_score > max_move_score: #if m is better than the current movepool
            max_move_score = current_move_score #update max move score
            moves = [] #empty the movepool
        if current_move_score == max_move_score:
            moves.append(m) #add m to movepool
    return moves[random.randrange(0,len(moves))]

def pick_move(board:chess.Board)->chess.Move:
    return minimax(0, board)[0]

def minimax(depth:int,board:chess.Board) -> tuple[chess.Move, int]:
    if board.is_game_over(): 
        if board.is_checkmate():
            if board.turn: #I THINK that if its checkmate on whites turn that means white lost correct my logic if im wrong
                return chess.Move.null(), -999999
            else:
                return chess.Move.null(), 999999
        return chess.Move.null(), 0 #if its not a checkmate its a stalemate or something similar which is not particularly good for either side but preferable to losing
    #maybe change max depth
    if depth >= 3 and board.turn: #if hit max depth and white to play
        moves = []
        max_move_score = -999
        for m in board.legal_moves: # for each legal move
        #calculate the resulting board's score
            board.push(move)
            current_move_score = boardScore(board)
            board.pop()
            if current_move_score > max_move_score: #if m is better than the current movepool
                max_move_score = current_move_score #update max move score
                moves = [] #empty the movepool
            if current_move_score == max_move_score:
                moves.append(m) #add m to movepool
        return moves[random.randrange(0,len(moves))], max_move_score
    elif depth >= 3: #if hit max depth and black to play
        moves = []
        min_move_score = 999
        for m in board.legal_moves: # for each legal move
        #calculate the resulting board's score
            board.push(move)
            current_move_score = boardScore(board)
            board.pop()
            if current_move_score < min_move_score: #if m is better than the current movepool
                min_move_score = current_move_score #update max move score
                moves = [] #empty the movepool
            if current_move_score == min_move_score:
                moves.append(m) #add m to movepool
        return moves[random.randrange(0,len(moves))], min_move_score
    if board.turn: #if white to play
        moves = []
        max_move_score = -999
        for m in board.legal_moves: # for each legal move
        #calculate the resulting board's score
            board.push(move)
            current_move_score = minimax(depth + 1,board)[1]
            board.pop()
            if current_move_score > max_move_score: #if m is better than the current movepool
                max_move_score = current_move_score #update max move score
                moves = [] #empty the movepool
            if current_move_score == max_move_score:
                moves.append(m) #add m to movepool
        return moves[random.randrange(0,len(moves))], max_move_score
    else: #if black to play 
        moves = []
        min_move_score = 999
        for m in board.legal_moves: # for each legal move
        #calculate the resulting board's score
            board.push(move)
            current_move_score = minimax(depth + 1,board)[1]
            board.pop()
            if current_move_score < min_move_score: #if m is better than the current movepool
                min_move_score = current_move_score #update max move score
                moves = [] #empty the movepool
            if current_move_score == min_move_score:
                moves.append(m) #add m to movepool
        return moves[random.randrange(0,len(moves))], min_move_score
    


def boardScore(board:chess.Board) -> int: #calculate the score of a board. positive ints mean board is favourable to white, negative mean board is favourable to black
    if board.is_game_over(): #check if the game is actually over
        if board.is_checkmate():
            if board.turn: #I THINK that if its checkmate on whites turn that means white lost correct my logic if im wrong
                return -999999
            else:
                return 999999
        return 0 #if its not a checkmate its a stalemate or something similar which is not particularly good for either side but preferable to losing
    if board.has_insufficient_material(chess.WHITE):
        return -9999
    elif board.has_insufficient_material(chess.BLACK):
        return 9999
    score = 0
    #things to check:
    #sum up total material on the board (pawn = 1, knight = bishop = 3, rook = 5, queen=9) (white positive black negative)
    for square in board.pieces():  #iterate through each piece and add/subtract. board.pieces returns a set of squares with pieces on them
        piece = board.piece_at(square)
        if piece.color == chess.WHITE:
            if piece.piece_type == chess.PAWN:
                score = score + 1
            elif piece.piece_type == chess.KNIGHT or piece.piece_type == chess.BISHOP:
                score = score + 3
            elif piece.piece_type == chess.ROOK:
                score = score + 5
            elif piece.piece_type == chess.QUEEN:
                score = score + 9
            #no points for king. both sides will always have one
        elif piece.color == chess.BLACK:
            if piece.piece_type == chess.PAWN:
                score = score - 1
            elif piece.piece_type == chess.KNIGHT or piece.piece_type == chess.BISHOP:
                score = score - 3
            elif piece.piece_type == chess.ROOK:
                score = score - 5
            elif piece.piece_type == chess.QUEEN:
                score = score - 9
    #uhhhhhhh. come up with other things to affect score. this is the meat of it idk    
    return score

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
