from tkinter import *
root = Tk()
myCanvas = Canvas(root)
myCanvas.pack()

def create_circle(x, y, r, canvasName): #center coordinates, radius
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvasName.create_oval(x0, y0, x1, y1)

create_circle(100, 100, 20, myCanvas)
create_circle(50, 25, 10, myCanvas)
root.mainloop()