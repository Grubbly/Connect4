from tkinter import *
from tkinter import font

root = Tk()

class GameDetails(Frame):
    def __init__(self):
        Frame.__init__(self, master=root, Background="green")
        self.configure(width=400, height=100) 
        self.t = Label(self, text="Connect 4", font=font.Font(self, size=22, family='Arial'))
        self.t.grid(sticky=W, pady=30)

