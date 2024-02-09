from tkinter import *
root = Tk()
root.title("This is my first window!")
root.geometry('500x200')

menu = Menu(root)
item = Menu(menu)
item.add_command(label='New')
menu.add_cascade(label='File', menu=item)
root.config(menu=menu)

lbl = Label (root, text="u love me? ")
lbl.grid()

txt = Entry(root, width=10)
txt.grid(column=1, row=0)

def clicked():
    
    res = "You wrote: " + txt.get()
    lbl.configure(text = res)
    
btn = Button(root, text = "Click here!", fg="red", command=clicked)

btn.grid(column=2, row=0)

rdbtn = Radiobutton(text="radio" + "not radio" )
rdbtn.grid(column=2, row=3)

root.mainloop()