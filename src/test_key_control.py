from tkinter import *

tk = Tk()

canvas = Canvas(tk, width=400, height=400)
canvas.pack()
canvas.create_polygon(10, 10, 10, 60, 50, 35)


def movefigure(event):
    if event.keysym == 'Up':
        canvas.move(1, 0, -3)
    elif event.keysym == 'Down':
        canvas.move(1, 0, 3)
    elif event.keysym == 'Left':
        canvas.move(1, -3, 0)
    else:
        canvas.move(1, 3, 0)


canvas.bind_all('<KeyPress-Up>', movefigure)
canvas.bind_all('<KeyPress-Down>', movefigure)
canvas.bind_all('<KeyPress-Left>', movefigure)
canvas.bind_all('<KeyPress-Right>', movefigure)

tk.mainloop()