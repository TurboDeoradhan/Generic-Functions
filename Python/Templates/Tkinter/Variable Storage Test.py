# Variable storage test.
from tkinter import *
main = Tk()
main.title('Variable Storage')
main_frame = Frame(main)                                 
main_frame.grid(column=0,row=0, sticky=(N,W,E,S) )
main_frame.columnconfigure(0, weight = 1)
main_frame.rowconfigure(0, weight = 1)
main_frame.pack(pady = 10, padx = 10)

menu_var = StringVar(main)
choices = {
    'Option 1': '1',
    'Option 2': '2',
}
option = OptionMenu(main_frame, menu_var, *choices)
menu_var.set('-')
option.grid(row = 1, column =1)

Label(main_frame, text='Value:').grid(row = 2, column = 1)
choice = StringVar()
value_ent = Entry(main_frame, text=choice, width = 15).grid(column = 2, row = 2)

def change_value(*args):
    value = choices[menu_var.get()]
    choice.set(value)

menu_var.trace('w', change_value)
main.mainloop()