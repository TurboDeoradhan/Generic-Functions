# Combobox test.
import tkinter as tk
from tkinter import ttk
main = tk.Tk()
main.title('Combobox')
main.geometry('500x250')

# Combobox variable and creation.
combo_var = tk.StringVar()
combo_box = ttk.Combobox(main, width = 27, textvariable = combo_var)

# Adding combobox values and setting default.
combo_box['values'] = ('Option 1', 'Option 2')
combo_var.set('Select:')

combo_box.pack(side='left')
combo_box.current()
main.mainloop()