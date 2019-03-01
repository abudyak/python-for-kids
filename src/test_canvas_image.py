from tkinter import *

tk = Tk()

canvas = Canvas(tk, width=600, height=800)
canvas.pack()
my_image = PhotoImage(file='C:\\Users\\abudyak\\Downloads\\USB20.gif')
canvas.create_image(0, 0, anchor=NW, image=my_image)

tk.mainloop()
