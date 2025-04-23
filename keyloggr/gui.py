#gui file
import tkinter as tk
import logger
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import Canvas
import sys
import os


def resource_path(relative_path):
    if hasattr(sys,'_MEIPASS'):
        return os.path.join(sys._MEIPASS,relative_path)
    return os.path.abspath(relative_path)

#called to start the gui
def startgui():
    root.mainloop()


#creating root and title
root=tk.Tk()
root.title("Sunset")

#bringing in background image
origsun=resource_path("sunset.png")
origsunset=PhotoImage(file=origsun)
sunset=origsunset.subsample(4,4)

widths=sunset.width()
heights=sunset.height()
root.geometry(f"{widths}x{heights}")
root.resizable(False,False)

bg_image=tk.Label(root,image=sunset)

bg_image.place(x=0,y=0,height=heights,width=widths)


