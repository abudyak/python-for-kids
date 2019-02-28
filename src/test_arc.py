from tkinter import *

tk = Tk()

canvas = Canvas(tk, width=400, height=400)
canvas.pack()
canvas.create_arc(10, 10, 200, 80, exten=45, style=ARC)
canvas.create_arc(10, 80, 200, 160, exten=90, style=ARC)
canvas.create_arc(10, 160, 200, 240, exten=135, style=ARC)
canvas.create_arc(10, 240, 200, 320, exten=180, style=ARC)
canvas.create_arc(10, 320, 200, 400, exten=359, style=ARC)

tk.mainloop()
