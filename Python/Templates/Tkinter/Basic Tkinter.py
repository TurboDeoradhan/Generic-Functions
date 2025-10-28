# Tkinter test.
import tkinter as tk
from tkinter import ttk
from tkinter import font as tkfont

# Create the main window.
main = tk.Tk()
main.title('Tkinter Example')

# Window size.
main.geometry('500x250')

# Establish a font.
main_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

# Create two frames on main.
frame_1 = tk.Frame(main)
frame_2 = tk.Frame(main)

# Pack frames on main.
frame_1.pack(side='top')
frame_2.pack(side='bottom')

# Labels.
ttk.Label(frame_1, text = 'Label 1', background = 'white', foreground ='black', font = ('Times New Roman', 10)).pack(side='left', pady=10)
ttk.Label(frame_2, text = 'Label 2', background = 'black', foreground ='white', font = ('Ariel', 20)).pack(side='right', padx=10)

# Start the Tkinter main loop
main.mainloop()