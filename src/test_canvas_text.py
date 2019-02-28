from tkinter import *

tk = Tk()

canvas = Canvas(tk, width=400, height=400)
canvas.pack()
canvas.create_text(150, 100, text='Text test')
canvas.create_text(150, 300, text='Text test', fill='blue', font=('Times', 15))

tk.mainloop()
