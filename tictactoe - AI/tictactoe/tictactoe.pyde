import pdb
import board
import Player
global X
global O
global f;
global obj


#-----------------------------------------------------------------------------------------------------#
#player class
class Player:
    name = None
    mark = None
    position = [0]*10
    
    def __init__(self, sign):
        self.mark = sign
    
    def posAppend(self, index):
        self.position[index] = 1
    
    def checkWin(self):

        if ((self.position[1] and self.position[2] and self.position[3]) or
        (self.position[4] and self.position[5] and self.position[6]) or 
        (self.position[1] and self.position[2] and self.position[3]) or
        (self.position[1] and self.position[4] and self.position[7]) or
        (self.position[2] and self.position[5] and self.position[8]) or
        (self.position[3] and self.position[6] and self.position[9]) or
        (self.position[1] and self.position[5] and self.position[9]) or
        (self.position[3] and self.position[5] and self.position    [7])):
            return True
        return False




#-----------------------------------------------------------------------------------------------------#
#Background for Game
class Board:
    position  = [[0]*10, [0]*10]
    
    players = []
    boardpos = []
    pos = [0]*10
    availpos = 9;
    check = 1
    game  = True

    
    def __init__(self):
        global X
        global O
        global board 
        X = loadImage("Player_X.png")
        O = loadImage("Player_O.png")
        board = loadImage("tic-tac-toe.png")
        self.players = []
        self.boardpos = []
        self.pos = [0]*10
        self.availpos = 9;
        self.check = 0 
        self.game  = True
        self.position  = [[0]*10, [0]*10]
        
        
    
    
    def checkWin(self,index):

        if ((self.position[index][1] and self.position[index][2] and self.position[index][3]) or
        (self.position[index][4] and self.position[index][5] and self.position[index][6]) or 
        (self.position[index][7] and self.position[index][8] and self.position[index][9]) or
        (self.position[index][1] and self.position[index][4] and self.position[index][7]) or
        (self.position[index][2] and self.position[index][5] and self.position[index][8]) or
        (self.position[index][3] and self.position[index][6] and self.position[index][9]) or
        (self.position[index][1] and self.position[index][5] and self.position[index][9]) or
        (self.position[index][3] and self.position[index][5] and self.position[index][7])):
            return True
        return False
    
    def move(self,index, ai = 0):  
            if (30<mouseX<130 and 30<mouseY<130 and not self.pos[1] and mousePressed) or ai == 1:
                self.boardpos.append((self.players[index].mark, 80, 80, width/4, height/4))
                self.position[index][1] = 1
                self.pos[1] = 1
                self.availpos-=1
                self.check ^= 1;
                return False
                                                
            elif (150<mouseX<250 and 30<mouseY<130 and not self.pos[2] and mousePressed) or ai == 2:
                self.boardpos.append((self.players[index].mark, 200, 80, width/4, height/4)) 
                self.position[index][2] = 1
                self.pos[2] = 1
                self.availpos-=1
                self.check ^= 1;
                return False
                
            elif (270<mouseX<360 and 30<mouseY<130 and not self.pos[3] and mousePressed) or ai == 3:
                self.boardpos.append((self.players[index].mark, 320, 80, width/4, height/4)) 
                self.position[index][3] = 1
                self.pos[3] = 1
                self.availpos-=1
                self.check ^= 1;
                return False
                
            elif (30<mouseX<130 and 150<mouseY<250 and not self.pos[4] and mousePressed) or ai == 4:
                self.boardpos.append((self.players[index].mark, 80, 200, width/4, height/4))
                self.position[index][4] = 1
                self.pos[4] = 1
                self.availpos-=1
                self.check ^= 1;
                return False
                
            elif (150<mouseX<250 and 150<mouseY<250 and not self.pos[5] and mousePressed) or ai == 5:
                self.boardpos.append((self.players[index].mark, 200, 200, width/4, height/4))
                self.position[index][5] = 1
                self.pos[5] = 1
                self.availpos-=1
                self.check ^= 1;
                return False
                
            elif (270<mouseX<370 and 150<mouseY<250 and not self.pos[6] and mousePressed) or ai == 6:
                self.boardpos.append((self.players[index].mark, 320, 200, width/4, height/4))
                self.position[index][6] = 1
                self.pos[6] = 1
                self.availpos-=1
                self.check ^= 1;
                return False
                
            elif (30<mouseX<130 and 275<mouseY<375 and not self.pos[7] and mousePressed) or ai == 7:
                self.boardpos.append((self.players[index].mark, 80, 320, width/4, height/4))
                self.position[index][7] = 1
                self.pos[7] = 1
                self.availpos-=1
                self.check ^= 1;
                return False
                
            elif (150<mouseX<250 and 275<mouseY<375 and not self.pos[8] and mousePressed) or ai == 8:
                self.boardpos.append((self.players[index].mark, 200, 320, width/4, height/4))
                self.position[index][8] = 1
                self.pos[8] = 1
                self.availpos-=1
                self.check ^= 1;
                return False
                
            elif (270<mouseX<370 and 275<mouseY<375 and not self.pos[9] and mousePressed) or ai == 9:
                self.boardpos.append((self.players[index].mark, 320, 320, width/4, height/4))
                self.position[index][9] = 1
                self.pos[9] = 1
                self.availpos-=1
                self.check ^= 1;
                return False
    
    def drawImage(self, arg):
        image(arg[0], arg[1], arg[2], arg[3], arg[4])
    
    def drawBoard(self):
        global X
        global O
        global board
        background(255)
        imageMode(CENTER)
        #image(X, 200, 320,  width/4, height/4)
        #image(O, 320, 320, width/4, height/4)    
        image(board, width/2, height/2, width, height)
        for img in self.boardpos:
            self.drawImage(img)
        if keyPressed:
            exit()
    

    
    def displayWinner(self,winner):
        self.drawBoard()

        background(255)
        fill(0)
        textSize(30)
        text("{} wins!".format(winner), width/2-100, height/2)

    
    def main(self):
        game = True
        global X
        global O
        self.players.append(Player(X))
        self.players.append(Player(O))

    
    def drawed(self):
        

        background(255)
        fill(0)
        textSize(30)
        text("Game Drawed!", width/2-100, height/2)

            
    def updateBoard(self):
        if self.check == 0:
            self.move(0)
            
            
                
        if self.check == 1:
            self.move(1,self.bestPlay())
            
        
        if self.checkWin(0):
                self.game = False
                winner = 1
                if not self.game:
                    self.displayWinner("You")
        
        elif self.checkWin(1):
                self.game = False
                winner = 2
                if not self.game:
                    self.displayWinner("Computer")
                    
        elif self.availpos<1:
            self.game = False
            self.drawed()
            
    
    #------------------------------------------Brain of AI-------------------------------------------#
    def bestPlay(self):
        bestScore = -1000
        bestPosition = -1
        for i in range(1,10):
            if self.pos[i] == 0:
                self.position[1][i] = 1
                self.pos[i] = 1
                self.availpos -= 1
                currentScore = self.miniMax(0, False)
                if currentScore > bestScore:
                    bestScore = currentScore
                    bestPosition = i
                self.resetStatus(i, 1)
        
        return bestPosition
    
    
    def miniMax(self, depth, isMaxmus):
        bestPosition = -1
        bestScore = 0
        if self.checkWin(0):
            return -10 + depth
        if self.checkWin(1):
            return  10 - depth
        
        if self.availpos == 0:
            return 0
        
        
        
        else:
            
            if isMaxmus:
                bestScore = -1000
                for i in range(1,10):
                    if self.pos[i] == 0:
                        self.position[1][i] = 1
                        self.pos[i] = 1
                        self.availpos -= 1
                        currentScore = self.miniMax(depth+1, False)
                        if currentScore > bestScore:
                            bestScore = currentScore
                            bestPosition = i
                        self.resetStatus(i, 1)
                        
            else:
                bestScore = 1000
                for i in range(1,10):
                    if self.pos[i] == 0:
                        self.position[0][i] = 1
                        self.pos[i] = 1
                        self.availpos -= 1
                        currentScore = self.miniMax(depth+1, True)
                        if currentScore < bestScore:
                            bestScore = currentScore
                            bestPosition = i
                        self.resetStatus(i, 0)
             
             
            return bestScore
             
 
    def resetStatus(self, i, player):
        self.pos[i] = 0
        self.position[player][i] = 0
        self.availpos += 1

#-----------------------------------------------------------------------------------------------------#
#main 


def setup():
    size(400,400)
    reset()


#-----------------------------------------------------------------------------------------------------#
# reset the game to initial state
def reset():
    background(255)
    global X
    global f
    global O
    global obj
    
    f = createFont("Arial",16,True);
    obj = Board()
    obj.drawBoard()
    obj.main()
     



def getInfo():
    background(51)
    global f
    textFont(f, 20)
    fill(255)
    text("Enter your choice :", 10, 100)
    if(frameCount% 60 == 0):
        fill(0)
    else:
        fill(255)
    text("__", 200,100)
    delay(1/2)
    


#-----------------------------------------------------------------------------------------------------#
#drawing item each frame
def draw():
    global obj
    if obj.game:
        obj.drawBoard()
        obj.updateBoard()
    else:
        delay(2000)
        reset()
