# Button test.
import tkinter as tk
main = tk.Tk()
main.title('Button Example')
main.geometry('500x250')
frame_1 = tk.Frame(main)
frame_2 = tk.Frame(main)
frame_1.pack(side='top')
frame_2.pack(side='bottom')

# Button functions must be specified before buttons.
def button_1_click():
    print('Button 1 was pressed.')
def button_2_click():
    print('Button 2 was pressed.')

# Create buttons on both frames with functions.
button_1 = tk.Button(frame_1, text='Button 1', command=button_1_click)
button_2 = tk.Button(frame_2, text='Button 2', command=button_2_click)

# Pack both buttons on both frames.
button_1.pack(side='left')
button_2.pack(side='right')

main.mainloop()