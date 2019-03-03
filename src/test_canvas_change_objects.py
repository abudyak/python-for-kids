from tkinter import *

tk = Tk()

canvas = Canvas(tk, width=400, height=400)
canvas.pack()
mytriangle = canvas.create_polygon(10, 10, 10, 60, 50, 35, fill='red')


def movefigure(event):
    if event.keysym == 'Down':
        canvas.move(mytriangle, 0, 50)
        canvas.itemconfig(mytriangle, fill='blue')
    elif event.keysym == 'Up':
        canvas.move(mytriangle, 0, -50)
        canvas.itemconfig(mytriangle, fill='red')


canvas.bind_all('<KeyPress-Down>', movefigure)
canvas.bind_all('<KeyPress-Up>', movefigure)

tk.mainloop()
