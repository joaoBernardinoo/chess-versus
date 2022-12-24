class Piece:
    
    def __init__(self, x, y, sprite, color):
        self.color = color
        self.i = y
        self.j = x
        self.sprite = sprite
        self.moves = []
        self.valid_moves()
    
    def update_pos(self,i,j):
        self.i = i
        self.j = j
        self.valid_moves()
        
        
class Rook(Piece):
    def valid_moves(self):
        self.moves.clear()
        i = self.i 
        j = self.j
        while i < 7:
            self.moves.append((i+1,j))
            i +=1
            
        i = self.i
         
        while i > 0:
            self.moves.append((i-1,j))
            i -=1
            
        i = self.i
        while j < 7:
            j +=1
            self.moves.append((i,j))
            
        j = self.j
        while j > 0:
            self.moves.append((i,j-1))
            j -=1
            
    
class Knight(Piece):
    def valid_moves(self):
        self.moves.clear()
        i = self.i 
        j = self.j
        
        if i > 1:
            if j < 7:
                self.moves.append((i-2,j+1))
            if j > 0:
                self.moves.append((i-2,j-1))
                
        i = self.i 
        j = self.j
                
        if i < 6:
            if j < 7:
                self.moves.append((i+2,j+1))
            if j > 0:
                self.moves.append((i+2,j-1))
        
        i = self.i 
        j = self.j
        
        if j > 1:
            if i < 7:
                self.moves.append((i+1,j-2))
            if i > 0:
                self.moves.append((i-1,j-2))
                
        i = self.i 
        j = self.j
                
        if j < 6:
            if i < 7:
                self.moves.append((i+1,j+2))
            if i > 0:
                self.moves.append((i-1,j+2))
        
class Bishop(Piece):
    def valid_moves(self):
        self.moves.clear()
        
        i = self.i 
        j = self.j
        while i < 7 and j < 7:
            self.moves.append((i+1,j+1))
            i += 1
            j += 1
            
        i = self.i
        j = self.j
        while i > 0 and j < 7:
            self.moves.append((i-1,j+1))
            i -= 1
            j += 1
                        
        i = self.i 
        j = self.j
        while i < 7 and j > 0:
            i += 1
            j -= 1
            self.moves.append((i,j))
            
        j = self.j
        i = self.i 
        while j > 0 and i > 0:
            self.moves.append((i-1,j-1))
            i -= 1
            j -= 1
            
class Queen(Piece):
    def valid_moves(self):
        self.moves.clear()
        i = self.i 
        j = self.j
        while i < 7 and j < 7:
            
            self.moves.append((i+1,j+1))
            i += 1
            j += 1
            
        i = self.i
        j = self.j
        while i > 0 and j < 7:
            self.moves.append((i-1,j+1))
            i -= 1
            j += 1
                        
        i = self.i 
        j = self.j
        while i < 7 and j > 0:
            i += 1
            j -= 1
            self.moves.append((i,j))
            
        j = self.j
        i = self.i 
        while j > 0 and i > 0:
            self.moves.append((i-1,j-1))
            i -= 1
            j -= 1
        i = self.i 
        j = self.j
        while i < 7:
            self.moves.append((i+1,j))
            i +=1
            
        i = self.i
         
        while i > 0:
            self.moves.append((i-1,j))
            i -=1
            
        i = self.i
        while j < 7:
            j +=1
            self.moves.append((i,j))
            
        j = self.j
        while j > 0:
            self.moves.append((i,j-1))
            j -=1
            
class King(Piece):
    def valid_moves(self):
        self.moves.clear()
        i = self.i
        j = self.j
        if i < 7:
            i += 1
            if j < 7:
                self.moves.append((i,j+1))
            if j > 0:
                self.moves.append((i,j-1))
            self.moves.append((i,j))
                              
        i = self.i
        j = self.j                      
        if i > 0:
            i -= 1
            if j < 7:
                self.moves.append((i,j+1))
            if j > 0:
                self.moves.append((i,j-1))
            self.moves.append((i,j))
        
        i = self.i
        j = self.j
        if j < 7:
            self.moves.append((i,j+1))
                
        j = self.j                      
        if j > 0:
            self.moves.append((i,j-1))
            
class Pawn(Piece):
    def valid_moves(self):
        self.moves.clear()
        i = self.i
        j = self.j
#####################################################################
        if self.color == 'white':
            self.moves.append((i,j-1))
            self.moves.append((i+1,j-1))
            self.moves.append((i-1,j-1))
        elif self.color == 'black':
            self.moves.append((i,j+1))
            self.moves.append((i+1,j+1))
            self.moves.append((i-1,j+1))
            
        if self.j == 6: 
            self.moves.append((i,j-2))
        elif self.j == 1:
            self.moves.append((i,j+2))    
            
            
        
    