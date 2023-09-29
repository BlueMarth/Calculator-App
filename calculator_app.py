### main code for the calculator app
import tkinter as tk
from tkinter import ttk

## user input functions


## arithmetic functions


## display output functions


## app setup
root = tk.Tk()
root.title('Calculator')
root.iconbitmap('python_icon.ico') ### change icon!

# app_width = 260
# app_height = 420
# screen_centerX = int(root.winfo_screenwidth()/2 - app_width/2)
# screen_centerY = int(root.winfo_screenheight()/2 - app_height/2)
# app_geometry = str(app_width) + 'x' + str(app_height) + '+' + str(screen_centerX) + '+' + str(screen_centerY)
# root.geometry(app_geometry)

app_width = 280
app_height = 400
display_width = root.winfo_screenwidth()
display_height = root.winfo_screenheight()

left = int(display_width / 2 - app_width / 2)
top = int(display_height / 2 - app_height / 2)
root.geometry(f'{app_width}x{app_height}+{left}+{top}')
resize_x = False
resize_y = False
root.resizable(resize_x, resize_y)

## widgets definition
# main display
main_disp_var = tk.StringVar()
main_display = ttk.Label(root, textvariable = main_disp_var)


# buttons
btn_0 = ttk.Button(root, text = '0')
btn_1 = ttk.Button(root, text = '1')
btn_2 = ttk.Button(root, text = '2')
btn_3 = ttk.Button(root, text = '3')
btn_4 = ttk.Button(root, text = '4')
btn_5 = ttk.Button(root, text = '5')
btn_6 = ttk.Button(root, text = '6')
btn_7 = ttk.Button(root, text = '7')
btn_8 = ttk.Button(root, text = '8')
btn_9 = ttk.Button(root, text = '9')

btn_negate = ttk.Button(root, text = '+/-')
btn_dot = ttk.Button(root, text = '.')
btn_exe = ttk.Button(root, text = '=')
btn_plus = ttk.Button(root, text = '+')
btn_minus = ttk.Button(root, text = '-')
btn_times = ttk.Button(root, text = 'x')
btn_divide = ttk.Button(root, text = '/')
btn_percent = ttk.Button(root, text = '%')
btn_parentheses = ttk.Button(root, text = '( )')
btn_clear = ttk.Button(root, text = 'C')



## grid

root.rowconfigure(0, weight = 2)
root.rowconfigure(1, weight = 2)
root.rowconfigure(2, weight = 2)
root.rowconfigure(3, weight = 3)
root.rowconfigure(4, weight = 3)
root.rowconfigure(5, weight = 3)
root.rowconfigure(6, weight = 3)
root.rowconfigure(7, weight = 3)

root.columnconfigure(0, weight = 3)
root.columnconfigure(1, weight = 3)
root.columnconfigure(2, weight = 3)
root.columnconfigure(3, weight = 3)

# place widgets in grid
btn_0.grid(row = 7, column = 1, sticky = 'nesw', ipadx=3, ipady=3)
btn_1.grid(row = 6, column = 0, sticky = 'nesw', ipadx=3, ipady=3)
btn_2.grid(row = 6, column = 1, sticky = 'nesw', ipadx=3, ipady=3)
btn_3.grid(row = 6, column = 2, sticky = 'nesw', ipadx=3, ipady=3)
btn_4.grid(row = 5, column = 0, sticky = 'nesw', ipadx=3, ipady=3)
btn_5.grid(row = 5, column = 1, sticky = 'nesw', ipadx=3, ipady=3)
btn_6.grid(row = 5, column = 2, sticky = 'nesw', ipadx=3, ipady=3)
btn_7.grid(row = 4, column = 0, sticky = 'nesw', ipadx=3, ipady=3)
btn_8.grid(row = 4, column = 1, sticky = 'nesw', ipadx=3, ipady=3)
btn_9.grid(row = 4, column = 2, sticky = 'nesw', ipadx=3, ipady=3)

btn_negate.grid(row = 7, column = 0, sticky = 'nesw', ipadx=3, ipady=3)
btn_dot.grid(row = 7, column = 2, sticky = 'nesw', ipadx=3, ipady=3)
btn_exe.grid(row = 7, column = 3, sticky = 'nesw', ipadx=3, ipady=3)
btn_plus.grid(row = 6, column = 3, sticky = 'nesw', ipadx=3, ipady=3)
btn_minus.grid(row = 5, column = 3, sticky = 'nesw', ipadx=3, ipady=3)
btn_times.grid(row = 4, column = 3, sticky = 'nesw', ipadx=3, ipady=3)
btn_divide.grid(row = 3, column = 3, sticky = 'nesw', ipadx=3, ipady=3)
btn_percent.grid(row = 3, column = 2, sticky = 'nesw', ipadx=3, ipady=3)
btn_parentheses.grid(row = 3, column = 1, sticky = 'nesw', ipadx=3, ipady=3)
btn_clear.grid(row = 3, column = 0, sticky = 'nesw', ipadx=3, ipady=3)

## security event
root.bind('<Escape>', lambda event: root.quit())

## run app
root.mainloop()