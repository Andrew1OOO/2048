import random, pygame
class Board:

    def __init__(self, board):
        self.board = list(board)

    def new_turn(self, block):
        for i in range(16):
            x,y = random.randint(0,3)
            if(self.board[x][y] == 0):
                self.board[x][y] = block
                break
    def check_end(self):
        pass
    
    def add_block(self, block):
        for i in range(16):
            rand_pos = (random.randint(0,3), random.randint(0,3))
            if(self.board[rand_pos[0]][rand_pos[1]] == 0):
                self.board[rand_pos[0]][rand_pos[1]] = block 
                return True

    def paint(self, surface):
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if(self.board[i][j] != 0):
                    self.board[i][j].draw(surface,self.board)

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
    def move(self, from_, pos):
        move = self.encrypt(pos)
        temp = self.board[move[0]][move[1]] 
        self.board[move[0]][move[1]] = self.board[from_[0]][from_[1]]
        self.board[from_[0]][from_[1]] = temp
        return True

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
                

    def decrypt(self, i,j):

        if(i == 0 and j == 0):
            return 8,8
        if(i == 1 and j == 0):
            return 84,8
        if(i == 2 and j == 0):
            return 160,8
        if(i == 3 and j == 0):
            return 236,8
        if(i == 0 and j == 1):
            return 8,84
        if(i == 0 and j == 2):
            return 8,160
        if(i == 0 and j == 3):
            return 8,236
        if(i == 1 and j == 1):
            return 84,84
        if(i == 2 and j == 1):
            return 160,84
        if(i == 1 and j == 2):
            return 84,160
        if(i == 1 and j == 3):
            return 84,236
        if(i == 3 and j == 1):
            return 236,84
        if(i == 2 and j == 2):
            return 160,160
        if(i == 2 and j == 3):
            return 160,236
        if(i == 3 and j == 2):
            return 236,160
        if(i == 3 and j == 3):
            return 236,236

    def center(i):
        return i[0]+4, i[1]+5