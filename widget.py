# programe to demonstrate widgets
from tkinter import Button, Entry, Label, Tk, Checkbutton, Frame

root = Tk()
# fram widget

frame = Frame(root)
frame.pack()

# button widget
btn = Button(root, text="click", command=root.destroy)
btn.pack()

# checkbutton widgets
chk_btn_1 = Checkbutton(root, text="java")
chk_btn_1.pack()
chk_btn_2 = Checkbutton(root, text="python")
chk_btn_2.pack()
chk_btn_3 = Checkbutton(root, text="c")
chk_btn_3.pack()

# entry widgets
Label_1 = Label(root, text="entry box")
Label_1.pack()
entry_1 = Entry(root)
entry_1.pack()
root.mainloop()
