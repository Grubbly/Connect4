import random

from time import sleep

from tkinter import *
from tkinter import font

windowWidth = 700
windowHeight = 600

blueWins = 0
redWins = 0
ties = 0

blueWinsText = "Blue Wins: " 
redWinsText = "Red Wins: " 
tiesText = "Ties: "

class GameDetails(Frame):
    def __init__(self, master):
        Frame.__init__(self, master=root, bg="green")
        self.configure(width=500, height=100) 
        self.text = Label(self, text="Connect 4", font=font.Font(self, size=22, family='Arial'), background="green")
        self.author = Label(self, text="Tristan Van Cise", font=font.Font(self, size=12, family='Arial'), background="green")
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

    def startAIGame(self, event):
        for games in range(int(numGames.get())):
            while self.turn:
                if gameMode.get() == options[1]: # Random AI
                    self.setAIPiece()
                if gameMode.get() == options[2]: # Defense
                    self.setDefenseAIPiece()

                if gameMode2.get() == options2[1]: # Random AI
                    self.setAIPiece()
                if gameMode2.get() == options2[2]: # Defense
                    self.setDefenseAIPiece()

    def setPiece(self, event):
        if self.turn:
            if gameMode.get() == options[0]: # Player
                column = int(event.x/100) # integer divide to get column
                self.placePiece(column, "player")
            if gameMode.get() == options[1]: # Random AI
                self.setAIPiece()
            if gameMode.get() == options[2]: # Defense
                self.setDefenseAIPiece()

            if gameMode2.get() == options2[0]: # Player
                column = int(event.x/100) # integer divide to get column
                self.placePiece(column, "player")
            if gameMode2.get() == options2[1]: # Random AI
                self.setAIPiece()
            if gameMode2.get() == options2[2]: # Defense
                self.setDefenseAIPiece()
    
    def setDefenseAIPiece(self):
        column = self.checkThreeInARow("blue" if self.color=="red" else "red")
        noThreeInARow = 9000

        if(column == noThreeInARow):
            column = random.randint(0,6)
        else:
            print("CheckThreeInARow: " + str(column))

        #print("AI placed piece in column: " + str(column+1))
        self.placePiece(column, "AI")

    def setAIPiece(self):
        column = random.randint(0,6)
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
    
    def tallyWin(self, color):
        if color == "red":
            global redWins
            redWins += 1
            redWinsLabel.config(text=redWinsText + str(redWins))
        if color == "blue":
            global blueWins
            blueWins += 1
            blueWinsLabel.config(text=blueWinsText + str(blueWins))

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
        # upDownDiagonal
        for row in range(3):
            for column in range(4):
                upDownDiagonalFourInARow = self.positions[row+3][column+3].color == self.positions[row+1][column+1].color == self.positions[row+2][column+2].color
                upDownDiagonalWinCondition = upDownDiagonalFourInARow and self.positions[row+3][column+3].color == color
                if(upDownDiagonalWinCondition and self.positions[row][column].color == "white" and self.positions[row+1][column].color != "white"):
                    print("upDownDiagonal")
                    return column
        # downupdiagonal
        for row in range(3):
            for column in range(6,2,-1):
                downupdiagonalFourInARow = self.positions[row+3][column-3].color == self.positions[row+1][column-1].color == self.positions[row+2][column-2].color
                downupdiagonalWinCondition = downupdiagonalFourInARow and self.positions[row+3][column-3].color == color
                if(downupdiagonalWinCondition and self.positions[row][column].color == "white" and self.positions[row+1][column].color != "white"):
                    print("downUpDiagonal")
                    return column
        
        # Vertical
        for row in range(3):
            for column in range(len(self.positions[0])):
                verticalFourInARow = self.positions[row+1][column].color == self.positions[row+2][column].color == self.positions[row+3][column].color
                verticalWinCondition = verticalFourInARow and self.positions[row+3][column].color == color
                if(verticalWinCondition and self.positions[row][column].color == "white"):
                    print("vertical")
                    return column

        # Horizontal
        for row in range(len(self.positions)):
            for column in range(5):
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


def menuChange(*args):
    restart()

def restart():
    global gameDetails
    gameDetails.text.config(text="")
    gameDetails = GameDetails(root)
    gameDetails.grid(row=0, column=0)

    board = Board(boardFrame)
    board.grid(row=90, column=0)

    startButton = Button(root, text="Start AI Battle!")
    startButton.bind("<Button-1>", board.startAIGame)
    startButton.grid(row=8, column=0)
    


root = Tk()
root.geometry("675x800")
root.title("Connect 4")

gameDetails = GameDetails(root)
gameDetails.grid(row=0, column=0)

boardFrame = Frame(root)
board = Board(boardFrame)
board.grid(row=90, column=0)

gameMode = StringVar(root)
options = ["Player", "Random AI", "Defense"]
gameMode.set(options[0])
gameMode.trace("w", menuChange)
selectionMenu = OptionMenu(root, gameMode, *options)
selectionMenu.grid(row=1, column=0)
selectionMenu.config(bg="BLUE")

gameMode2 = StringVar(root)
options2 = ["Player", "Random AI", "Defense"]
gameMode2.set(options2[0])
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
numGames.grid(row=8, column=0)

startButton = Button(root, text="Start AI Battle!")
startButton.bind("<Button-1>", board.startAIGame)
startButton.grid(row=9, column=0)



root.mainloop()