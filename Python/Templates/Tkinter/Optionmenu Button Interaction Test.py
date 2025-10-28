# Optionmenu button interaction test.
from tkinter import *
main = Tk()
main.geometry('200x200')

menu_var = StringVar(main)
menu_var.set('Select:')
choices = ['Option 1', 'Option 2', 'Option 3']

option_menu = OptionMenu(main, menu_var, *choices)
option_menu.pack()

def submit():
    selection = menu_var.get()
    print(selection)

button = Button(main, text='Submit', command=submit)
button.pack()
main.mainloop()