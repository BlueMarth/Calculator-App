### main code for the calculator app
import tkinter as tk
from tkinter import ttk

## button functions


## arithmetic functions


## 


## app setup
root = tk.Tk()
root.title('Calculator')
root.iconbitmap('python_icon.ico') ### change icon!

app_width = 400
app_height = 600
screen_centerX = int(root.winfo_screenwidth()/2 - app_width/2)
screen_centerY = int(root.winfo_screenheight()/2 - app_height/2)
app_geometry = str(app_width) + 'x' + str(app_height) + '+' + str(screen_centerX) + '+' + str(screen_centerY)
print(app_geometry)
root.geometry(app_geometry)


## dynamic display


## buttons


## layout & packing


## security event
root.bind('<Escape>', lambda event: root.quit())

## run app
root.mainloop()