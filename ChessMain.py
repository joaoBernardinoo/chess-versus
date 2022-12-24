import pyglet
import ChessBoard

window = pyglet.window.Window(width= 800, height= 720, caption= 'Chess Versus')
window.set_location(350,30)
white_moves = pyglet.media.StaticSource(pyglet.media.load('assets/white_moves.mp3'))
black_moves = pyglet.media.StaticSource(pyglet.media.load('assets/black_moves.mp3'))
player = pyglet.media.Player()
player.play()


class Game:
    
    def __init__(self):
        self.table =  ChessBoard.GameState()
        self.holding = [None,0,0]
    
    def dragNdrop(self,sprite,x,y):
            sprite.sprite.x = x - 40
            sprite.sprite.y = y - 35
            
    def place_piece(self,x,y):
        valid,i,j = self.board_pos(x,y)
        if self.table.valid_pos(i,j,self.holding) and valid:
            self.holding[0].sprite.x = 44 + 90 * j
            self.holding[0].sprite.y = 635 - 90 * i
            
            self.table.board[i][j] = self.holding[0]
            self.table.board[self.holding[1]][self.holding[2]] = '-'
            self.table.board[i][j].update_pos(j,i)
            
            player.next_source()
            if self.table.board[i][j].color == 'white':
                player.queue(white_moves)
            else:
                player.queue(black_moves)
            player.play()
            
        else:
            self.holding[0].sprite.x = 44 + 90 * self.holding[2]
            self.holding[0].sprite.y = 635 - 90 * self.holding[1]
        self.holding[0] = None
    
    def board_pos(self,x,y):
        valid = True
        if 720> y >= 630:
            i = 0
        elif 630> y >= 540:
            i = 1
        elif 540> y >= 450:
            i = 2
        elif 450> y >= 360:
            i = 3
        elif 360> y >= 270:
            i = 4
        elif 270> y >= 180:
            i = 5
        elif 180> y >= 90:
            i = 6
        elif 90> y >= 0:
            i = 7
        else:
            i = -1
            valid = False
        if 44 <= x < 134:
            j = 0
        elif 134 <= x < 224:
            j = 1
        elif 224 <= x < 314:
            j = 2
        elif 314 <= x < 404:
            j = 3
        elif 404 <= x < 494:
            j = 4
        elif 494 <= x < 584:
            j = 5
        elif 584 <= x < 674:
            j = 6
        elif 674 <= x < 764:
            j = 7
        else:
            j = -1
            valid = False
            
        
        return valid,i,j
            
##########################################################################################################################
##########################################################################################################################
        
chess = Game()
def text_board():
    print('----------------')
    for i in range(8):
        for x in chess.table.board[i]:
            if x == '-':
                print(x,end=' ')
            else:
                print(x.name,end= ' ')
        print()

@window.event
def on_draw():  
    chess.table.draw_board()

@window.event
def on_key_press(symbol,modifiers):
    text_board()

@window.event
def on_mouse_release(x, y, button, modifiers):
    if chess.holding[0] is None:
        return
    chess.place_piece(x,y)
    text_board()
    
    
@window.event
def on_mouse_press(x, y, button, modifiers):
    valid,i,j = chess.board_pos(x,y)
    if chess.table.board[i][j] == '-' or not valid:
        return
    chess.holding[0] = chess.table.board[i][j]
    chess.holding[1] = i
    chess.holding[2] = j
    chess.dragNdrop(chess.holding[0],x,y)
    
    
@window.event
def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
    if chess.holding[0] is None or chess.holding[1] == -1 or chess.holding[2] == -1 :
        return
    chess.dragNdrop(chess.holding[0],x,y)


if __name__ == '__main__':
    pyglet.app.run()