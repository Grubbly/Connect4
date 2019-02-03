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

root = Tk()
root.geometry("400x600")
root.title("Connect 4")

gameDetails = GameDetails(root)
gameDetails.pack()

# STUFF here

root.mainloop()