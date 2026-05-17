from tkinter import *
class Calculator():
    def __init__(self):
        self.phase1 = 0 
        self.phase2 = 0 
        self.final = 0 
        self.entry = StringVar()
        self.text = ""
        self.signe = ""
        self.entry.set("Créer par Matt")
        
    def init(self):
        self.phase1 = 0 
        self.phase2 = 0 
        self.final = 0 
        self.text = "" 
        self.signe = "" 
        
    def afficher_Nb(self):
        self.entry.set(self.text)

    def operation(self):
        try : 
            if "+" in self.text:
                self.Plus()
            elif "-" in self.text:
                self.Sous()
            elif "/" in self.text:
                self.Div()
            elif "X" in self.text:
                self.Mult()
        except:
            self.entry.set("ERROR")
            self.init()

    def Plus(self):
        nb = self.text.split("+")
        self.phase1 = float(nb[0])
        self.phase2 = float(nb[1])
        self.final = self.phase1 + self.phase2
        self.entry.set(str(self.final))
        self.init()

    def Sous(self):
        nb = self.text.split("-")
        self.phase1 = float(nb[0])
        self.phase2 = float(nb[1])
        self.final = self.phase1 - self.phase2
        self.entry.set(str(self.final))
        self.init()

    def Div(self):
        nb = self.text.split("/")
        self.phase1 = float(nb[0])
        self.phase2 = float(nb[1])
        self.final = self.phase1 / self.phase2
        self.entry.set(str(self.final))
        self.init()

    def Mult(self):
        nb = self.text.split("X")
        self.phase1 = float(nb[0])
        self.phase2 = float(nb[1])
        self.final = self.phase1 * self.phase2
        self.entry.set(str(self.final))
        self.init()
    
def Button1 (): 
    calculatrice.text += "1"
    calculatrice.entry.set(calculatrice.text)

def Button2 (): 
    calculatrice.text += "2"
    calculatrice.entry.set(calculatrice.text)

def Button3 (): 
    calculatrice.text += "3"
    calculatrice.entry.set(calculatrice.text)

def Button4 ():
    calculatrice.text += "4"
    calculatrice.entry.set(calculatrice.text)
    
def Button5 (): 
    calculatrice.text += "5"
    calculatrice.entry.set(calculatrice.text)

def Button6 (): 
    calculatrice.text += "6"
    calculatrice.entry.set(calculatrice.text)

def Button7 (): 
    calculatrice.text += "7"
    calculatrice.entry.set(calculatrice.text)

def Button8 (): 
    calculatrice.text += "8"
    calculatrice.entry.set(calculatrice.text)
    
def Button9 (): 
    calculatrice.text += "9"
    calculatrice.entry.set(calculatrice.text)

def Button0 (): 
    calculatrice.text += "0"
    calculatrice.entry.set(calculatrice.text)

def ButtonF():
    calculatrice.text += "."
    calculatrice.entry.set(calculatrice.text)
    
def ButtonP (): 
    calculatrice.text += "+"
    calculatrice.entry.set(calculatrice.text)

def ButtonS (): 
    calculatrice.text += "-"
    calculatrice.entry.set(calculatrice.text)

def ButtonD ():
    calculatrice.text += "/"
    calculatrice.entry.set(calculatrice.text)

def ButtonM ():
    calculatrice.text += "X"
    calculatrice.entry.set(calculatrice.text)

def ButtonE (): 
    calculatrice.operation()

def ButtonC (): 
    calculatrice.entry.set("")
    calculatrice.init()

fen = Tk() 
fen.geometry("200x240") 
fen.title("Calculatrice v1.0")
fen["bg"]= "SkyBlue2"
fen["relief"] = "raised"
calculatrice = Calculator()
ECRAN = Entry(fen, width=28, textvariable=calculatrice.entry, bg ="black", fg="white", relief=SUNKEN, bd=5).place(x=9, y=8)
B1 = Button(fen, text="1", command=Button1, width=3, height=2, bg="grey", fg="white").place(x=10, y=40)
B2 = Button(fen, text="2", command=Button2, width=3, height=2, bg="grey", fg="white").place(x=50, y=40)
B3 = Button(fen, text="3", command=Button3, width=3, height=2, bg="grey", fg="white").place(x=90, y=40)
B4 = Button(fen, text="4", command=Button4, width=3, height=2, bg="grey", fg="white").place(x=10, y=90)
B5 = Button(fen, text="5", command=Button5, width=3, height=2, bg="grey", fg="white").place(x=50, y=90)
B6 = Button(fen, text="6", command=Button6, width=3, height=2, bg="grey", fg="white").place(x=90, y=90)
B7 = Button(fen, text="7", command=Button7, width=3, height=2, bg="grey", fg="white").place(x=10, y=140)
B8 = Button(fen, text="8", command=Button8, width=3, height=2, bg="grey", fg="white").place(x=50, y=140)
B9 = Button(fen, text="9", command=Button9, width=3, height=2, bg="grey", fg="white").place(x=90, y=140)
BC = Button(fen, text="C", command=ButtonC, width=3, height=2, bg="gold", fg="red", relief=RIDGE).place(x=10, y=190)
B0 = Button(fen, text="0", command=Button0, width=3, height=2, bg="grey", fg="white").place(x=50, y=190)
BF = Button(fen, text=".", command=ButtonF, width=3, height=2, bg="grey", fg="white").place(x=90, y=190)

BP = Button(fen, text="+", command=ButtonP, width=4, height=2, bg="gold", fg="black", relief=GROOVE).place(x=150, y=40)
BS = Button(fen, text="-", command=ButtonS, width=4, height=2, bg="gold", fg="black", relief=GROOVE).place(x=150, y=80)
BD = Button(fen, text="/", command=ButtonD, width=4, height=2, bg="gold", fg="black", relief=GROOVE).place(x=150, y=120)
BM = Button(fen, text="X", command=ButtonM, width=4, height=2, bg="gold", fg="black", relief=GROOVE).place(x=150, y=160)
BE = Button(fen, text="=", command=ButtonE, width=4, height=1, bg="blue", fg="white", relief=RIDGE).place(x=150, y=205)

fen.mainloop()