#gui file
import tkinter as tk
import logger
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import Canvas


#called to start the gui
def startgui():
    root.mainloop()


#creating root and title
root=tk.Tk()
root.title("Sunset")

#bringing in background image
origsunset=PhotoImage(file="sunset.png")
sunset=origsunset.subsample(4,4)
widths=sunset.width()
heights=sunset.height()
root.geometry(f"{widths}x{heights}")
root.resizable(False,False)

bg_image=tk.Label(root,image=sunset)

bg_image.place(x=0,y=0,height=heights,width=widths)


