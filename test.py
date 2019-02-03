import tkinter as tk

counter = 0
def updateLabelCount(label):
    def count():
        global counter
        counter += 1
        label.config(text=str(counter))
        label.after(1000, count)
    count()

root = tk.Tk()
root.title("Connect 4")



# Widget that surrounds other widgets
frame = tk.Frame(root) 
labelText = tk.StringVar()
label = tk.Label(frame, textvariable=labelText)
button = tk.Button(root, text="Click Me!")

labelText.set("I am label")

label.pack()
button.pack()
frame.pack()


frame2 = tk.Frame(root)
tk.Label(frame, text="A bunch of buttons").pack()

tk.Button(frame2, text="B1").pack(side=tk.LEFT, fill=tk.X)
tk.Button(frame2, text="B2").pack(side=tk.TOP, fill=tk.X)
tk.Button(frame2, text="B3").pack(side=tk.RIGHT, fill=tk.X)
tk.Button(frame2, text="B4").pack(side=tk.LEFT, fill=tk.X)

frame2.pack()


frame3 = tk.Frame(root)

# Sticky is the direction the widget expands N NE, W, SE
tk.Label(frame3, text="First Name").grid(row=0, sticky=tk.W, padx=4)
tk.Entry(frame3).grid(row=0, column=1, sticky=tk.E, pady=4)

tk.Label(frame3, text="Last Name").grid(row=1, sticky=tk.E, padx=4)
tk.Entry(frame3).grid(row=1, column=1, sticky=tk.W, pady=4)

tk.Button(frame3, text="Submit").grid(row=3)

frame3.pack()


frame4 = tk.Frame(root)

tk.Label(frame4, text="Description").grid(row=0, column=0, sticky=tk.W)
tk.Entry(frame4, width=50).grid(row=0, column=1)
tk.Button(frame4, text="Submit").grid(row=0, column=3)

tk.Label(frame4, text="Quality").grid(row=1, column=0, sticky=tk.W)
tk.Radiobutton(frame4, text="New", value=1).grid(row=2, column=0, sticky=tk.W)
tk.Radiobutton(frame4, text="Good", value=2).grid(row=3, column=0, sticky=tk.W)
tk.Radiobutton(frame4, text="Poor", value=3).grid(row=4, column=0, sticky=tk.W)
tk.Radiobutton(frame4, text="Damaged", value=4).grid(row=5, column=0, sticky=tk.W)

tk.Label(frame4, text="Benefits").grid(row=1, column=1, sticky=tk.W)
tk.Checkbutton(frame4, text="Free Shipping").grid(row=2, column=1, sticky=tk.W)
tk.Checkbutton(frame4, text="Shtuff").grid(row=3, column=1, sticky=tk.W)

frame4.pack()


frame5 = tk.Frame(root)

def get_sum(event):
    num1 = int(num1Entry.get())
    num2 = int(num2Entry.get())

    sum = num1 + num2

    # Delete all characters from [0, str.length)
    sumEntry.delete(0, tk.END)
    sumEntry.insert(0, sum)
# Positioning elements like .grid and .pack cannot be suffixed onto
# GUI elements if they are being used for data retrieval. It must
# be done later. Example:
num1Entry = tk.Entry(frame5)
num1Entry.pack(side=tk.LEFT)

tk.Label(frame5, text="+").pack(side=tk.LEFT)

num2Entry = tk.Entry(frame5)
num2Entry.pack(side=tk.LEFT)

equalButton = tk.Button(frame5, text="=")
equalButton.bind("<Button-1>", get_sum)
equalButton.pack(side=tk.LEFT)

sumEntry = tk.Entry(frame5)
sumEntry.pack(side=tk.LEFT)

frame5.pack()

root.mainloop()
