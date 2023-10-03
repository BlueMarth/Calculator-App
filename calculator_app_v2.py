import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Calculator')
        self.geometry('350x500')
        self.minsize(150,250)
        
        Display(self)
        Keypad(self)

        self.mainloop()


class Display(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(x = 0, y = 0, relwidth = 1, relheight = 0.25)
        label = ttk.Label(self, text = 'label', justify = 'center', background = 'red')
        label.place(relx = 1, rely = 1, anchor = 'se')
        

class Keypad(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(x = 0, rely = 0.25, relwidth = 1, relheight = 0.75)
        self.columnconfigure((0,1,2,3), weight = 1, uniform = 'a')
        self.rowconfigure((0,1,2,3,4,5), weight = 1, uniform = 'a')
        
        self.add_button('btn_0', '0', 5, 1)
        self.add_button('btn_1', '1', 4, 0)
        self.add_button('btn_2', '2', 4, 1)
        self.add_button('btn_3', '3', 4, 2)
        self.add_button('btn_4', '4', 3, 0)
        self.add_button('btn_5', '5', 3, 1)
        self.add_button('btn_6', '6', 3, 2)
        self.add_button('btn_7', '7', 2, 0)
        self.add_button('btn_8', '8', 2, 1)
        self.add_button('btn_9', '9', 2, 2)
        self.add_button('btn_dot', '.', 5, 2)
        self.add_button('btn_exe', '=', 5, 3)
        self.add_button('btn_plus', '+', 4, 3)
        self.add_button('btn_minus', '-', 3, 3)
        self.add_button('btn_times', 'x', 2, 3)
        self.add_button('btn_over', '/', 1, 3)
        self.add_button('btn_back', '<', 0, 3)
        self.add_button('btn_clear', 'C', 0, 2)
        self.add_button('btn_recip', '1/x', 1, 0)
        self.add_button('btn_sqrt', '1/^2', 1, 2)
        self.add_button('btn_sq', '^2', 1, 1)
        self.add_button('btn_fact', '!', 0, 1)
        self.add_button('btn_perc', '%', 0, 0)
        
    def add_button(self, buttonID, buttonText, buttonRow, buttonColumn, buttonCommand):
        buttonID = ttk.Button(self, text = buttonText, command = buttonCommand)
        buttonID.grid(row = buttonRow, column = buttonColumn, sticky = 'nsew')

    def



App()