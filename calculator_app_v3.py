import tkinter as tk



LIGHT_GRAY = "#F5F5F5"
LABEL_COLOR = "25265E"

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry('375x667')
        self.window.resizable(0,0)
        self.window.title("Calculator")

        self.total_expression = "0"
        self.current_expression = "0"

        self.display_Frame = self.create_display_frame()
        self.buttons_Frame = self.create_buttons_frame()

    def create_display_label(self):
        total_label = tk.Label(self.display_frame, text = self.total_expression, anchor = tk.E, bg = LIGHT_GRAY, fg = LABEL_COLOR, PADX = 24, )


    def create_display_frame(self):
        frame = tk.Frame(self.window, height = 221, bg = LIGHT_GRAY)
        frame.pack(expand = True, fill = 'both')
        return frame
    
    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand = True, fill = 'both')
        return frame
    


    def run(self):
        self.window.mainloop()



if __name__ == "__main__":
    calc = Calculator()
    Calculator.run()