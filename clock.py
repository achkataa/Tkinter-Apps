from tkinter import *
from tkinter.ttk import *
from time import strftime


#create tkinter  window
root = Tk()
root.title("Clock by Achkata")

#this function is used to display time on the label.
def time():
    current_time = strftime('%H:%M:%S %p')
    lbl.config(text = current_time)
    lbl.after(1000, time)

#Styling the label widget
lbl = Label(font = ("Helvetica", 40, "bold italic"),
            background = "#294C60",
            foreground = "white")

#placing clock in the center of window
lbl.pack(anchor = "center")

time()
mainloop()