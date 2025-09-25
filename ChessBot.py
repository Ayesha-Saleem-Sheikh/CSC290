import chess


board = chess.Board()
print(board)
# player = input("Computer Player? (w=white/b=black):") #get player and store as variable
# print("Starting FEN position? (hit ENTER for standard starting position):")

# if (position.equals("")):
#if user enters something, set the board state
#gameplay loop:
#while not in checkmate:
#
while (True):
    position = input("White:")
    move = chess.Move.from_uci(position)
    board.push(move)
    print(board)
    print(board.fen())
    position = input("Black:")
    move = chess.Move.from_uci(position)
    board.push(move)
    print(board)
    print(board.fen())
# while (True):
    
    


    


