# progrmae to demonstrate canvs
from tkinter import Canvas, Tk

root = Tk()

canvas_w = 500
canvas_h = 500

canvas_obj = Canvas(root, width=canvas_w, height=canvas_h)
canvas_obj.pack()

y = int(canvas_h / 2)
canvas_obj.create_line(10, y, canvas_w, y, fill="green")

coords = 10, 50, 240, 10
canvas_obj.create_arc(coords, start=90, extent=190, fill="red")

canvas_obj.create_oval(50, 50, 100, 100)
root.mainloop()
