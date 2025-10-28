from tkinter import *
main = Tk()
main.title('Input Button Test')
main.geometry('400x300')

def get_input():
    name = user_input.get()
    Label(main, text=f'Recieved input: {name}').pack()
    return name

user_input = Entry(main)
user_input.pack()
Button(main, text='User Input:', command=get_input).pack()
name = user_input.get()

main.mainloop()