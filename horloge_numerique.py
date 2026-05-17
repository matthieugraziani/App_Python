from tkinter import *			
from time import gmtime, strftime, sleep
root = Tk()
root.resizable(width=False, height=False)
root.geometry("130x40+0+0")
root.overrideredirect(1)
root.config(bg="red")
Label_Heure = Label(root, font=('', 20, 'bold'), bg='green')
Label_Heure.pack()
def Heure():
	Label_Heure.config(text=strftime('%H:%M:%S'))
	Label_Heure.after(200, Heure)
Heure()
root.mainloop()