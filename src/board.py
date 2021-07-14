import random, pygame
from block import Block
class Board():

    def __init__(self, mode):
        self.board = self.create_board(mode)
        self.score = 0
    def printb(self):
        for i in range(4):
            print(str(i+1) + "| ", *self.board[i], sep=' ')
    def create_board(self, mode):
        board1 =[[0,0,0,0],
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0]]
        board1[random.randint(0,3)][random.randint(0,3)] = Block(4,pygame.Rect(0,0, 60, 60), mode)
        board1[random.randint(0,3)][random.randint(0,3)] = Block(2,pygame.Rect(0,0, 60, 60), mode)
        board1[random.randint(0,3)][random.randint(0,3)] = Block(2,pygame.Rect(0,0, 60, 60), mode)
        return board1
    def clear(self):
        self.board =[[0,0,0,0],
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0]]
        self.board[random.randint(0,3)][random.randint(0,3)] = Block(4,pygame.Rect(0,0, 60, 60))
        self.board[random.randint(0,3)][random.randint(0,3)] = Block(2,pygame.Rect(0,0, 60, 60))
        self.board[random.randint(0,3)][random.randint(0,3)] = Block(2,pygame.Rect(0,0, 60, 60))
    def add_block(self, block):
        for i in range(16):
            rand_pos = (random.randint(0,3), random.randint(0,3))
            if(self.board[rand_pos[0]][rand_pos[1]] == 0):
                self.board[rand_pos[0]][rand_pos[1]] = block 
                return True

    def paint(self, surface, scoreSurface):
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if(self.board[i][j] != 0):
                    self.board[i][j].draw(surface,self.board, scoreSurface, self.score)
                    break

    def shift_left(self):
        
        for i in range(len(self.board)):
            v=[]
            w=[]
            for j in range(len(self.board[0])):
                if(self.board[i][j] != 0):
                    v.append(self.board[i][j])

            j=0
            while(j < len(v)):
                if(j < len(v) - 1 and v[j].size == v[j+1].size):
                    v[j].set_size(v[j].size*2)
                    w.append(v[j])
                    self.score += v[j].size
                    j+=1
                else:
                    w.append(v[j])
                j += 1
            
            for j in range(len(self.board)):
                self.board[i][j] = 0
            j=0
            for it in w:
                self.board[i][j] = it

                j+=1
        
    def shift_right(self):
        for i in range(len(self.board)):
            v = []
            w = []

            for j in range(len(self.board) - 1, -1, -1):
                    
                    # if not 0
                if (self.board[i][j]):
                    v.append(self.board[i][j])
    
                # For each temporary array
            j = 0
            while (j < len(v)): 
                if (j < len(v) - 1 and v[j].size == v[j + 1].size):
                    v[j].set_size(v[j].size*2)
                    w.append(v[j])
                    self.score += v[j].size
                    j += 1
                    
                else:
                    w.append(v[j])
                        
                j += 1
    
                # Filling the each row element to 0.
            for j in range(len(self.board)):
                self.board[i][j] = 0
    
            j = len(self.board) - 1
    
            for it in w:
                self.board[i][j] = it
                j -= 1
        
    def shift_vertical(self, up):
        if(up):
            for i in range(len(self.board)):
                v = []
                w = []
    

                for j in range(len(self.board)):
                    
                    # If not 0
                    if (self.board[j][i]):
                        v.append(self.board[j][i])

                j = 0
                while(j < len(v)):
                    

                    if (j < len(v) - 1 and v[j].size == v[j + 1].size):
                        v[j].set_size(v[j].size*2)
                        w.append(v[j])
                        self.score += v[j].size
                        j += 1
                    
                    else:
                        w.append(v[j])
                    j += 1
    
                for j in range(len(self.board)):
                    self.board[j][i] = 0
    
                j = 0

                for it in w:
                    self.board[j][i] = it
                    j += 1
        else:
            for i in range(len(self.board)):
                v = []
                w = []

                for j in range(len(self.board) - 1, -1, -1):
                    
                    # If not 0
                    if (self.board[j][i]):
                        v.append(self.board[j][i])
                j = 0
                while(j < len(v)):
    
                    
                    if (j <len( v) - 1 and v[j].size == v[j+1].size):
                        v[j].set_size(v[j].size*2)

                        w.append(v[j])
                        self.score += v[j].size
                        j += 1
                    
                    else:
                        w.append(v[j])
                        
                    j += 1
                        
                for j in range(len(self.board)):
                    self.board[j][i] = 0
    
                j = len(self.board) - 1
    
                for it in w:
                    self.board[j][i] = it
                    j -= 1

    def move(self, move):
        if move == "L":
            self.shift_left()
            #self.add_block(Block(2 * random.randint(1,2), pygame.Rect(0,0, 60, 60)))
        if move == "R":
            self.shift_right()
            #self.add_block(Block(2 * random.randint(1,2), pg.Rect(0,0, 60, 60)))
        if move == "U":
            self.shift_vertical(True)
            #self.add_block(Block(2 * random.randint(1,2), pg.Rect(0,0, 60, 60)))
        if move == "D":
            self.shift_vertical(False)
            #self.add_block(Block(2 * random.randint(1,2), pg.Rect(0,0, 60, 60)))

    def encrypt(self, pos):
        origin = (75,75)
        start = (75,75)
        size = 60
        in_between = 8
        for j in range(4):
            for i in range(4):
                start = (in_between*i*2+origin[0]+size*i, in_between*j*2+origin[1]+size*j)
                if pos[0] <= start[0]+size+8 and pos[1] <= start[1]+size+8 and pos[0] >= start[0]+8 and pos[1] >= start[1]+8:
                    return i,j
                
    
    def game_over(self):
        for i in range(4):
            for j in range(4):
                if(self.board[i][j]!= 0):

                    if(self.board[i][j].size == 2048):
                        return True

        for i in range(4):
            for j in range(4):
                if(self.board[i][j]== 0):
                    return False
            
        for i in range(3):
            for j in range(3):
                if(self.board[i][j].size== self.board[i + 1][j].size or self.board[i][j].size== self.board[i][j + 1].size):
                    return False
    
        for j in range(3):
            if(self.board[3][j].size== self.board[3][j + 1].size):
                return False
    
        for i in range(3):
            if(self.board[i][3].size== self.board[i + 1][3].size):
                return False
    
        return True
    
