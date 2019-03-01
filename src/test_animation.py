import time
from tkinter import *

tk = Tk()

canvas = Canvas(tk, width=400, height=300)
canvas.pack()
canvas.create_polygon(10, 10, 10, 60, 50, 35)

for x in range(0, 360):
    canvas.move(1, 1, 1)
    tk.update()
    time.sleep(0.01)

tk.mainloop()
