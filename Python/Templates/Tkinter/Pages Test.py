# Pages test.
import tkinter as tk
from tkinter import font as tkfont

class PageTest(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.main_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        # Stack frames for pages, raise the default page to front.
        main_frame = tk.Frame(self)
        main_frame.pack(side="top", fill="both", expand=True)
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (PageMain, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=main_frame, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("PageMain")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

class PageMain(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Main Menu", font=controller.main_font)
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="Page One",
            command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="Page Two",
            command=lambda: controller.show_frame("PageTwo"))
        button1.pack()
        button2.pack()

class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Page One", font=controller.main_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Return",
            command=lambda: controller.show_frame("PageMain"))
        button.pack()

class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Page Two", font=controller.main_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Return",
            command=lambda: controller.show_frame("PageMain"))
        button.pack()

if __name__ == "__main__":
    app = PageTest()
    app.mainloop()