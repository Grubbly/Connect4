import random
import time
import copy

from time import sleep

from tkinter import *
from tkinter import font

windowWidth = 700
windowHeight = 600

blueWins = 0
redWins = 0
ties = 0
evaluatedMoves = 0
countColor = "blue"

blueWinsText = "Blue Wins: " 
redWinsText = "Red Wins: " 
tiesText = "Ties: "
evaluatedMovesText = "Evaluated Moves: "
timeText = "Total Time: "
movesOverTimeText = "Moves/Second: "

class GameDetails(Frame):
    def __init__(self, master):
        Frame.__init__(self, master=root)
        self.configure(width=500, height=100) 
        self.text = Label(self, text="Connect 4", font=font.Font(self, size=22, family='Arial'), background="green")
        self.author = Label(self, text="Tristan Van Cise", font=font.Font(self, size=12, family='Arial'))
        self.text.grid(sticky=W, pady=20)
        self.author.grid(sticky=N)


class Piece(object):
    def __init__(self, x, y, canvas, color="white", bg="red"):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.color = color
        
        self.piece = self.canvas.create_oval(x+10, y+10, x+61, y+61, fill=color, outline="yellow")
    
    def switchColor(self, color):
        self.canvas.itemconfigure(self.piece, fill=color)
        self.color = color

class Board(Canvas):
    def __init__(self, master):
        Canvas.__init__(self)
        self.configure(width=windowWidth+70, height=windowHeight+70, bg="green")
        
        self.player = 1
        self.color = "blue"
        self.positions = []
        self.turn = True

        for row in range(0, windowHeight, int(windowHeight/6)):
            row_positions = []
            for column in range(0, windowWidth, int(windowWidth/7)):
                row_positions.append(Piece(column, row, self))
            self.positions.append(row_positions)
        self.bind("<Button-1>", self.setPiece)

    def startAIGame(self):
        if gameMode.get() == options[0] or gameMode2.get() == options2[0]:
            print("Click the board to start playing!")
            return

        while self.turn:
            if gameMode.get() == options[1]: # Random AI
                self.setAIPiece()
            if gameMode.get() == options[2]: # Defense
                self.setDefenseAIPiece()
            if gameMode.get() == options[3]: # Defense Aggro
                self.setDefenseAgroAIPiece()
            if gameMode.get() == options[4]: # Mobile Defense Aggro
                self.setMobileDefenseAgroAIPiece()

            if not self.turn:
                break

            if gameMode2.get() == options2[1]: # Random AI
                self.setAIPiece()
            if gameMode2.get() == options2[2]: # Defense
                self.setDefenseAIPiece()
            if gameMode2.get() == options2[3]: # Defense Aggro
                self.setDefenseAgroAIPiece()  
            if gameMode2.get() == options2[4]: # Mobile Defense Aggro
                self.setMobileDefenseAgroAIPiece()
            if gameMode2.get() == options2[5]: # DFS
                self.testDFSDepth2()
            

    def setPiece(self, event):
        if self.turn:
            if gameMode.get() == options[0]: # Player
                column = int(event.x/100) # integer divide to get column
                self.placePiece(column, "player")
            if gameMode.get() == options[1]: # Random AI
                self.setAIPiece()
            if gameMode.get() == options[2]: # Defense
                self.setDefenseAIPiece()
            if gameMode.get() == options[3]: # Defense Aggro
                self.setDefenseAgroAIPiece()
            if gameMode.get() == options[4]: # Mobile Defense Aggro
                self.setMobileDefenseAgroAIPiece()

        if self.turn:
            if gameMode2.get() == options2[0]: # Player
                column = int(event.x/100) # integer divide to get column
                self.placePiece(column, "player")
            if gameMode2.get() == options2[1]: # Random AI
                self.setAIPiece()
            if gameMode2.get() == options2[2]: # Defense
                self.setDefenseAIPiece()
            if gameMode2.get() == options2[3]: # Defense Aggro
                self.setDefenseAgroAIPiece()    
            if gameMode2.get() == options2[4]: # Mobile Defense Aggro
                self.setMobileDefenseAgroAIPiece()
            if gameMode2.get() == options2[5]: # DFS
                self.testDFSDepth2()
    
    def setMobileDefenseAgroAIPiece(self):
        column = self.checkThreeInARow("blue" if self.color=="red" else "red")
        noThreeInARow = 9000
        global evaluatedMoves

        if(column == noThreeInARow):
            column = self.checkThreeInARow(self.color)
            print("AGGRO: " + str(column))
        else:
            print("CheckThreeInARow: " + str(column))

        if(column == noThreeInARow):
            column = self.mobileMoveDefault()
            print("MOBILE: " + str(column))

        if(column == noThreeInARow):
            if self.color == countColor:
                evaluatedMoves += 1
            column = random.randint(0,6)

        self.placePiece(column, "AI")

    def testDFSDepth2(self):
        column = self.mobileMoveHeuristic2(self.positions)
        print("DFS column: " + str(column))
        self.placePiece(column, "AI")

    # def BFS(self, s): 
    #     visited = [False] * (len(self.graph)) 
    #     queue = [] 
    #     queue.append(s) 
    #     visited[s] = True
  
    #     while queue: 
    #         s = queue.pop(0) 
    #         print (s, end = " ") 

    #         for i in self.graph[s]: 
    #             if visited[i] == False: 
    #                 queue.append(i) 
    #                 visited[i] = True

    def setDefenseAgroAIPiece(self):
        column = self.checkThreeInARow("blue" if self.color=="red" else "red")
        noThreeInARow = 9000
        global evaluatedMoves

        if(column == noThreeInARow):
            column = self.checkThreeInARow(self.color)
            print("AGGRO: " + str(column))
        else:
            print("CheckThreeInARow: " + str(column))

        if(column == noThreeInARow):
            if self.color == countColor:
                evaluatedMoves += 1
            column = random.randint(0,6)

        self.placePiece(column, "AI")


    def setDefenseAIPiece(self):
        column = self.checkThreeInARow("blue" if self.color=="red" else "red")
        noThreeInARow = 9000
        global evaluatedMoves

        if(column == noThreeInARow):
            if self.color == countColor:
                evaluatedMoves += 1
            column = random.randint(0,6)
        else:
            print("CheckThreeInARow: " + str(column))

        #print("AI placed piece in column: " + str(column+1))
        self.placePiece(column, "AI")

    def setAIPiece(self):
        column = random.randint(0,6)
        global evaluatedMoves
        if self.color == countColor:
                evaluatedMoves += 1
        print("AI placed piece in column: " + str(column+1))
        self.placePiece(column, "AI")

    def placePiece(self, column, type="player"):
            row = 0
            while row < len(self.positions):
                # Full column condition
                if self.positions[0][column].color == "red" or self.positions[0][column].color == "blue": 
                    if(type == "AI"):
                        print("Bad AI move generated, regenerating...")
                        self.setAIPiece()
                    else:
                        # TODO: Label this on GUI
                        print("Bad player move")
                    return
                
                # If there exits a piece in the column, place the next piece above it
                if self.positions[row][column].color == "red" or self.positions[row][column].color == "blue":
                    print("Piece Placed: (" + str(column) + ", " + str(row) + ")")
                    self.positions[row-1][column].switchColor(self.color)
                    break
                
                # If there is no piece in the column, place it in the first spot
                elif row == len(self.positions) - 1:
                    print("Piece Placed: (" + str(column) + ", " + str(row) + ")")
                    self.positions[row][column].switchColor(self.color)
                    break

                # No open spot? Increment to find it
                if self.positions[row][column].color != "red" and self.positions[row][column].color != "blue":
                    row += 1

            # Change turns:
            
            if self.player == 1:
                self.player = 2
                gameDetails.text.config(text="Player 2's Turn")
                self.color = "red"

            elif self.player == 2:
                self.player = 1
                gameDetails.text.config(text="Player 1's Turn")
                self.color = "blue"
            
            self.checkWin()
    
    def testPlacePiece(self, column, positions, type="player"):
            row = 0
            placedRow = 0
            while row < len(positions):
                # Full column condition
                if positions[0][column].color == "red" or positions[0][column].color == "blue": 
                    # print("COLUMN ", column, " FULL")
                    return positions, -1
                
                # If there exits a piece in the column, place the next piece above it
                if positions[row][column].color == "red" or positions[row][column].color == "blue":
                    # print("PREDICTION Piece Placed: (" + str(column) + ", " + str(row) + ")")
                    positions[row-1][column].switchColor(self.color)
                    placedRow = row-1
                    break
                
                # If there is no piece in the column, place it in the first spot
                elif row == len(positions) - 1:
                    # print("TEST Piece Placed: (" + str(column) + ", " + str(row) + ")")
                    positions[row][column].switchColor(self.color)
                    placedRow = row
                    break

                # No open spot? Increment to find it
                if positions[row][column].color != "red" and positions[row][column].color != "blue":
                    row += 1

            return positions, placedRow

    def tallyWin(self, color):
        if color == "red":
            global redWins
            redWins += 1
            redWinsLabel.config(text=redWinsText + str(redWins))
        elif color == "blue":
            global blueWins
            blueWins += 1
            blueWinsLabel.config(text=blueWinsText + str(int(blueWins/2)))

    def checkWin(self):
        # horizontal
        for row in range(len(self.positions)):
            for column in range(4):
                horizontalFourInARow = self.positions[row][column].color == self.positions[row][column+1].color == self.positions[row][column+2].color == self.positions[row][column+3].color
                horizontalWinCondition = horizontalFourInARow and self.positions[row][column].color != "white"
                if(horizontalWinCondition):
                    gameDetails.text.config(text=self.positions[row][column].color + " wins!")
                    self.tallyWin(self.positions[row][column].color)
                    self.turn = False
                    return
                    
        # vertical
        for row in range(3):
            for column in range(len(self.positions[0])):
                verticalFourInARow = self.positions[row][column].color == self.positions[row+1][column].color == self.positions[row+2][column].color == self.positions[row+3][column].color
                verticalWinCondition = verticalFourInARow and self.positions[row][column].color != "white"
                if(verticalWinCondition):
                    gameDetails.text.config(text=self.positions[row][column].color + " wins!")
                    self.tallyWin(self.positions[row][column].color)
                    self.turn = False
                    return

        # upDownDiagonal
        for row in range(3):
            for column in range(4):
                upDownDiagonalFourInARow = self.positions[row][column].color == self.positions[row+1][column+1].color == self.positions[row+2][column+2].color == self.positions[row+3][column+3].color
                upDownDiagonalWinCondition = upDownDiagonalFourInARow and self.positions[row][column].color != "white"
                if(upDownDiagonalWinCondition):
                    gameDetails.text.config(text=self.positions[row][column].color + " wins!")
                    self.tallyWin(self.positions[row][column].color)
                    self.turn = False
                    return

        # downupdiagonal
        for row in range(3):
            for column in range(6,2,-1):
                downupdiagonalFourInARow = self.positions[row][column].color == self.positions[row+1][column-1].color == self.positions[row+2][column-2].color == self.positions[row+3][column-3].color
                downupdiagonalWinCondition = downupdiagonalFourInARow and self.positions[row][column].color != "white"
                if(downupdiagonalWinCondition):
                    gameDetails.text.config(text=self.positions[row][column].color + " wins!")
                    self.tallyWin(self.positions[row][column].color)
                    self.turn = False
                    return

        # tie game
        for row in range(len(self.positions)):
            for column in range(len(self.positions[0])):
                if(self.positions[row][column].color == "white"):
                    return
        gameDetails.text.config(text="Tie Game!")
        global ties
        ties += 1
        tiesLabel.config(text=tiesText + str(ties))
        self.turn = False

    def checkThreeInARow(self, color):
        global evaluatedMoves
        # upDownDiagonal
        for row in range(3):
            for column in range(4):
                if self.color == countColor:
                    evaluatedMoves += 1
                upDownDiagonalFourInARow = self.positions[row+3][column+3].color == self.positions[row+1][column+1].color == self.positions[row+2][column+2].color
                upDownDiagonalWinCondition = upDownDiagonalFourInARow and self.positions[row+3][column+3].color == color
                if(upDownDiagonalWinCondition and self.positions[row][column].color == "white" and self.positions[row+1][column].color != "white"):
                    print("upDownDiagonal")
                    return column
        # downupdiagonal
        for row in range(3):
            for column in range(6,2,-1):
                if self.color == countColor:
                    evaluatedMoves += 1
                downupdiagonalFourInARow = self.positions[row+3][column-3].color == self.positions[row+1][column-1].color == self.positions[row+2][column-2].color
                downupdiagonalWinCondition = downupdiagonalFourInARow and self.positions[row+3][column-3].color == color
                if(downupdiagonalWinCondition and self.positions[row][column].color == "white" and self.positions[row+1][column].color != "white"):
                    print("downUpDiagonal")
                    return column
        
        # Vertical
        for row in range(3):
            for column in range(len(self.positions[0])):
                if self.color == countColor:
                    evaluatedMoves += 1
                verticalFourInARow = self.positions[row+1][column].color == self.positions[row+2][column].color == self.positions[row+3][column].color
                verticalWinCondition = verticalFourInARow and self.positions[row+3][column].color == color
                if(verticalWinCondition and self.positions[row][column].color == "white"):
                    print("vertical")
                    return column

        # Horizontal
        for row in range(len(self.positions)):
            for column in range(5):
                if self.color == countColor:
                    evaluatedMoves += 1
                horizontalFourInARow = self.positions[row][column].color == self.positions[row][column+1].color 
                horizontalWinCondition = horizontalFourInARow and self.positions[row][column].color == color
                if horizontalWinCondition and self.positions[row][column+2].color == "white":
                    if row == 5:
                        return column+2
                    elif self.positions[row+1][column+2].color != "white":
                        return column+2
                elif horizontalWinCondition and column >= 1 and self.positions[row][column-1].color == "white":
                    if row == 5:
                        return column-1
                    elif self.positions[row+1][column-1].color != "white":
                        return column-1

        return 9000

    def getRowNumberForColumn(self, column, positions):
        row = 0
        global evaluatedMoves
        while row < len(positions):
            if self.color == countColor:
                evaluatedMoves += 1
            # Full column condition
            if positions[0][column].color == "red" or positions[0][column].color == "blue": 
                return -1
            
            # If there exits a piece in the column, place the next piece above it
            if positions[row][column].color == "red" or positions[row][column].color == "blue":
                return row-1
            
            # If there is no piece in the column, place it in the first spot
            elif row == len(positions) - 1:
                return row

            # No open spot? Increment to find it
            if positions[row][column].color != "red" and positions[row][column].color != "blue":
                row += 1

    def mobileMoveDefault(self):
        global evaluatedMoves
        validMoves = []
        moveScores = [0,0,0,0,0,0,0]
        for column in range(len(self.positions[0])):
            validMoves.append(self.getRowNumberForColumn(column, self.positions))

        # Score the immediate next move
        # Add these values to the move score 
        # because we want to maximize the value
        # of the AI's next move.
        for column in range(len(validMoves)):
            if self.color == countColor:
                evaluatedMoves += 1
            if validMoves[column] > 0:
                leftMoveIndex = column-1
                rightMoveIndex = column+1
                verticalMoveIndex = validMoves[column]-1
                
                if leftMoveIndex >= 0:
                    moveScores[column] += 1
                if rightMoveIndex <= 6:
                    moveScores[column] += 1
                if verticalMoveIndex >= 0:
                    moveScores[column] += 1

        return max(moveScores)

    # Get this to work with a depth of 1 per column, then expand
    def recurse(self, rootPositions, rootCol, score, depth):
        global evaluatedMoves
        
        if depth == 0:
            return score

        moveScores = [0,0,0,0,0,0,0]
        validMoves = []
        # REMOVE THIS LOOPING and pass column additionally
        rootRow = self.getRowNumberForColumn(rootCol, rootPositions)
        
        ## validMoves[column] = rootRow
        ## column = rootColumn

        if self.color == countColor:
            evaluatedMoves += 1
        if rootRow > 0:
            leftMoveIndex = rootCol-1
            rightMoveIndex = rootCol+1 # this is rootCol + 1
            verticalMoveIndex = rootRow-1 # This is rootRow-1
            
            if leftMoveIndex >= 0:
                score += 1
            if rightMoveIndex <= 6:
                score += 1
            if verticalMoveIndex >= 0:
                score += 1

            # Can an enemy three in a row be block? If so, weight this heavily
            if self.checkThreeInARow("blue" if self.color=="red" else "red") == rootCol:
                score += 5

            # Can we win this turn?
            if self.checkThreeInARow(self.color) == rootCol:
                score += 10

        ## Start edits here!
        
            positions = rootPositions
            positions, placedRow = self.testPlacePiece(rootCol, positions, "null")

            if placedRow < 0:
                score = -9000

            playerValidMoves = []
            for playerColumn in range(len(positions[0])):
                if self.color == countColor:
                    evaluatedMoves += 1
                playerValidMoves.append(self.getRowNumberForColumn(playerColumn, positions))

            for playerColumn in range(len(playerValidMoves)):
                if self.color == countColor:
                    evaluatedMoves += 1
                if score > 0:
                    leftMoveIndex = playerColumn-1
                    rightMoveIndex = playerColumn+1
                    verticalMoveIndex = playerValidMoves[playerColumn]-1
                    
                    if leftMoveIndex >= 0:
                        score -= 1./21
                    if rightMoveIndex <= 6:
                        score -= 1./21
                    if verticalMoveIndex >= 0:
                        score -= 1./21

            # Subtract the best move the player could make from the
            # score of the AI's best move. The net value will represent
            # the best move (in terms of the heuristic) that the AI can
            # make with a depth of 2.
            score += min(playerValidMoves)
            # score += self.recurse(positions, column, score, depth-1)
            positions[placedRow][rootCol].switchColor("white")
            # print("Switched: (", column ,  ", ", placedRow, ")")
        return score

    def mobileMoveHeuristic2(self, rootPositions, depth=1):
        global evaluatedMoves
        validMoves = []
        moveScores = [0,0,0,0,0,0,0]
        for column in range(len(rootPositions[0])):
            moveScores[column] = self.recurse(rootPositions, column, moveScores[column], depth)

        print("Column score evaluations: ", moveScores)
        return moveScores.index(max(moveScores))

    def mobileMoveHeuristic(self, rootPositions, depth=1):
        global evaluatedMoves
        validMoves = []
        moveScores = [0,0,0,0,0,0,0]
        for column in range(len(rootPositions[0])):
            validMoves.append(self.getRowNumberForColumn(column, rootPositions))

        # Score the immediate next move
        # Add these values to the move score 
        # because we want to maximize the value
        # of the AI's next move.
        for column in range(len(validMoves)):
            if self.color == countColor:
                evaluatedMoves += 1
            if validMoves[column] > 0:
                leftMoveIndex = column-1
                rightMoveIndex = column+1
                verticalMoveIndex = validMoves[column]-1
                
                if leftMoveIndex >= 0:
                    moveScores[column] += 1
                if rightMoveIndex <= 6:
                    moveScores[column] += 1
                if verticalMoveIndex >= 0:
                    moveScores[column] += 1

                # Can an enemy three in a row be block? If so, weight this heavily
                if self.checkThreeInARow("blue" if self.color=="red" else "red") == column:
                    moveScores[column] += 5

                # Can we win this turn?
                if self.checkThreeInARow(self.color) == column:
                    moveScores[column] += 10
        
        # Generate the move set for the enemy for each
        # valid move. Subtract these from the move score
        # to minimize the value of the player's next move.
        for column in range(len(validMoves)):
            positions = rootPositions
            positions, placedRow = self.testPlacePiece(column, positions, "null")

            if placedRow < 0:
                moveScores[column] = -9000
                continue

            playerValidMoves = []
            for playerColumn in range(len(positions[0])):
                if self.color == countColor:
                    evaluatedMoves += 1
                playerValidMoves.append(self.getRowNumberForColumn(playerColumn, positions))

            for playerColumn in range(len(playerValidMoves)):
                if self.color == countColor:
                    evaluatedMoves += 1
                if validMoves[column] > 0:
                    leftMoveIndex = column-1
                    rightMoveIndex = column+1
                    verticalMoveIndex = validMoves[column]-1
                    
                    if leftMoveIndex >= 0:
                        moveScores[column] -= 1./21
                    if rightMoveIndex <= 6:
                        moveScores[column] -= 1./21
                    if verticalMoveIndex >= 0:
                        moveScores[column] -= 1./21

            # Subtract the best move the player could make from the
            # score of the AI's best move. The net value will represent
            # the best move (in terms of the heuristic) that the AI can
            # make with a depth of 2.
            positions[placedRow][column].switchColor("white")
            # print("Switched: (", column ,  ", ", placedRow, ")")
            moveScores[column] += max(playerValidMoves)

        print("Column score evaluations: ", moveScores)
        return moveScores.index(max(moveScores))

def menuChange(*args):
    print("menu change")
    resetGlobals()
    restart()
    # restart()

def restart():
    global gameDetails
    gameDetails.text.config(text="")
    gameDetails = GameDetails(root)
    gameDetails.grid(row=0, column=0)

    global board
    board = Board(boardFrame)
    board.grid(row=90, column=0)

def resetGlobals():
    global redWins, blueWins, ties, evaluatedMoves
    redWins = 0
    blueWins = 0
    ties = 0
    evaluatedMoves = 0

def startAIGame(*args):
    if gameMode.get() == options[0] or gameMode2.get() == options2[0]:
        print("Click the board to start playing!")
        return
    
    if type(int(numGames.get())) is not int or int(numGames.get()) <= 0:
        return

    resetGlobals()
    t0 = time.time()
    for game in range(int(numGames.get())):
        board.startAIGame()
        restart()
    t1 = time.time()
    totalTime = t1 - t0
    print(str(int(numGames.get())) + " Games Finished")
    evaluatedMovesLabel.config(text=evaluatedMovesText + str(evaluatedMoves))
    timeLabel.config(text=timeText+str(totalTime)+" seconds")
    movesOverTimeLabel.config(text=movesOverTimeText+str(evaluatedMoves/totalTime)+" moves/sec")


root = Tk()
root.geometry("675x950")
root.title("Connect 4")

gameDetails = GameDetails(root)
gameDetails.grid(row=0, column=0)

boardFrame = Frame(root)
board = Board(boardFrame)
board.grid(row=90, column=0)

gameMode = StringVar(root)
options = ["Player", "Random AI", "Defense", "Defense Agro", "Mobile Defense Agro"]
gameMode.set(options[0])
gameMode.trace("w", menuChange)
selectionMenu = OptionMenu(root, gameMode, *options)
selectionMenu.grid(row=1, column=0)
selectionMenu.config(bg="BLUE")

gameMode2 = StringVar(root)
options2 = ["", "Random AI", "Defense", "Defence Agro", "Mobile Defense Agro", "DFS"]
gameMode2.set(options2[2])
gameMode2.trace("w", menuChange)
selectionMenu2 = OptionMenu(root, gameMode2, *options2)
selectionMenu2.grid(row=2, column=0)
selectionMenu2.config(bg="RED")

blueWinsLabel = Label(root, text=blueWinsText + str(blueWins))
redWinsLabel = Label(root, text=redWinsText + str(redWins))
tiesLabel = Label(root, text=tiesText + str(ties))

blueWinsLabel.grid(row=5, column=0)
redWinsLabel.grid(row=6, column=0)
tiesLabel.grid(row=7, column=0)

numGames = Entry(root)
numGames.insert(0,0)
numGames.grid(row=8, column=0)

startButton = Button(root, text="Start AI Battle!")
startButton.bind("<Button-1>", startAIGame)
startButton.grid(row=9, column=0)

evaluatedMovesLabel = Label(root, text=evaluatedMovesText + str(evaluatedMoves))
evaluatedMovesLabel.grid(row=10, column=0)

timeLabel = Label(root, text=timeText + str(0) + " seconds")
timeLabel.grid(row=11, column=0)

movesOverTimeLabel = Label(root, text=movesOverTimeText + str(0))
movesOverTimeLabel.grid(row=12, column=0)

resetButton = Button(root, text="RESET")
resetButton.bind("<Button-1>", menuChange)
resetButton.grid(row=13, column=0)

root.mainloop()