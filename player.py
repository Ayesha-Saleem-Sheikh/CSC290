import chess
class player:
    def __init__(self, color: bool, board: chess.Board):
     self.board = board
     self.color = color
    
    def make_move(self,board: chess.Board,move):
        piece =board.piece_at(move.from_square)
        if piece.color == self.color:
           board.push(move)
           return move
        else:
            raise Exception("It's not your turn!")  
            

# game = chess.Board()
# print(game)
# x = input ("Enter your color (w=white/b=black): ")
# if x == 'w':
#     player_color = chess.WHITE
# else:
#     player_color = chess.BLACK



# p1 = player(player_color, game)
# p2 = player(not player_color,game)
# print ("Player 1 is playing as :" , p1.color)
# print("player 2 is playing as :", p2.color)
# while not game.is_game_over():
#     if game.turn == chess.WHITE:
#         p1.make_move(game)
#     else:
#         p2.make_move(game)
#     print(game)

    




    











