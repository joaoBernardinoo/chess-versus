import game_core
import ChessPieces
import pyglet

class GameState():

    def __init__(self):

        self.imgs = dict(
            r = game_core.image("assets/bR.png"),
            n = game_core.image("assets/bN.png"),
            b = game_core.image("assets/bB.png"),
            k = game_core.image("assets/bK.png"),
            q = game_core.image("assets/bQ.png"),
            p = game_core.image("assets/bP.png"),
            P = game_core.image("assets/wP.png"),
            R = game_core.image("assets/wR.png"),
            N = game_core.image("assets/wN.png"),
            B = game_core.image("assets/wB.png"),
            K = game_core.image("assets/wK.png"),
            Q = game_core.image("assets/wQ.png")
            
        )
        
        self.Board = pyglet.sprite.Sprite(pyglet.image.load("assets/board.png"))
        self.board = [
            ['r','n','b','k','q','b','n','r'],
            ['p','p','p','p','p','p','p','p'],
            ['-','-','-','-','-','-','-','-'],
            ['-','-','-','-','-','-','-','-'],
            ['-','-','-','-','-','-','-','-'],
            ['-','-','-','-','-','-','-','-'],
            ['P','P','P','P','P','P','P','P'],
            ['R','N','B','K','Q','B','N','R'],
        ]
        
        self.pieces = pyglet.graphics.Batch()
        
        self.load_game("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR")
        
    def valid_pos(self,i,j,holding):
        if holding[1] == i and holding[2] == j:
            return False
        try:
            index = holding[0].moves.index((j,i))
            piece = holding[0]
            if piece.name.upper() == 'P':
                way = -1 if piece.color == 'white' else 1
                if self.board[i][j] == '-':
                    if index == 0:
                        return True
                    if index == 3 and self.board[i - way][j] == '-':
                        return True
                else:
                    if self.board[i][j].color != piece.color and 3 > index > 0:
                        return True
                return False
            
            if self.board[i][j] == '-':
                return True
            
            if self.board[i][j].color != piece.color:
                return True
            
        except ValueError:
            return False

    def load_game(self,FEN):
        y = 635
        pieces = FEN.split('/')
        for i in range(8):
            j = 0
            x = 44
            for piece in pieces[i]:
                if '0' < piece < '9':
                    count = int(piece)
                    while count != 0:
                        self.board[i][j] = '-'
                        count -= 1
                        
                else:
                    if piece == 'r':
                        self.board[i][j] = ChessPieces.Rook(i,j,game_core.sprite(self.imgs[piece], x, y, self.pieces),'black')
                    elif piece == 'R':
                        self.board[i][j] = ChessPieces.Rook(i,j,game_core.sprite(self.imgs[piece], x, y, self.pieces),'white')
                    elif piece == 'n':
                        self.board[i][j] = ChessPieces.Knight(i,j,game_core.sprite(self.imgs[piece], x, y, self.pieces),'black')
                    elif piece == 'N':
                        self.board[i][j] = ChessPieces.Knight(i,j,game_core.sprite(self.imgs[piece], x, y, self.pieces),'white') 
                    elif piece == 'b':
                        self.board[i][j] = ChessPieces.Bishop(i,j,game_core.sprite(self.imgs[piece], x, y, self.pieces),'black')
                    elif piece == 'B':
                        self.board[i][j] = ChessPieces.Bishop(i,j,game_core.sprite(self.imgs[piece], x, y, self.pieces),'white') 
                    elif piece == 'k':
                        self.board[i][j] = ChessPieces.King(i,j,game_core.sprite(self.imgs[piece], x, y, self.pieces),'black')
                    elif piece == 'K':
                        self.board[i][j] = ChessPieces.King(i,j,game_core.sprite(self.imgs[piece], x, y, self.pieces),'white') 
                    elif piece == 'q':
                        self.board[i][j] = ChessPieces.Queen(i,j,game_core.sprite(self.imgs[piece], x, y, self.pieces),'black')
                    elif piece == 'Q':
                        self.board[i][j] = ChessPieces.Queen(i,j,game_core.sprite(self.imgs[piece], x, y, self.pieces),'white')
                    elif piece == 'p':
                        self.board[i][j] = ChessPieces.Pawn(i,j,game_core.sprite(self.imgs[piece], x, y, self.pieces),'black')
                    elif piece == 'P':
                        self.board[i][j] = ChessPieces.Pawn(i,j,game_core.sprite(self.imgs[piece], x, y, self.pieces),'white')    
                    self.board[i][j].sprite.scale = 1.94
                    self.board[i][j].name = piece
                j += 1
                x += 90
            y -= 90
                
    def draw_board(self):
        self.Board.draw()
        self.pieces.draw()
                
                
                    



