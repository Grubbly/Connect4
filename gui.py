from tkinter import *
from tkinter import font

windowWidth = 400
windowHeight = 600

class GameDetails(Frame):
    def __init__(self, master):
        Frame.__init__(self, master=root, bg="green")
        self.configure(width=windowWidth, height=100) 
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
        
        self.radius = 30
        self.piece = self.canvas.create_oval(x+10, y+10, x+61, y+61, fill=color, outline="yellow")
    
    def switchColor(self, color):
        self.canvas.itemconfigure(self.piece, fill=color)
        self.color = color

class Board(Canvas):
    def __init__(self, master):
        Canvas.__init__(self)
        self.configure(width=windowWidth, height=windowHeight, bg="green")
        
        self.player = 1
        self.color = "blue"
        self.positions = []
        self.turn = True


        for row in range(0, windowHeight-60, int(windowHeight/6)):
            row_positions = []
            for column in range(0, windowWidth-60, int(windowWidth/7)):
                row_positions.append(Piece(column, row, self))
            self.positions.append(row_positions)
        self.bind("<Button-1>", self.setPiece)
    
    def setPiece(self, event):
        # if self.turn:
            print(str(event.x))



root = Tk()
root.geometry("400x600")
root.title("Connect 4")

gameDetails = GameDetails(root)
gameDetails.grid(row=0, column=0)

board = Board(root)
board.grid(row=1, column=0)

root.mainloop()