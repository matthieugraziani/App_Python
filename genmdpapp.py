from tkinter import Label, Button, Checkbutton, Tk, IntVar, Entry, StringVar
from random import choice, randint

alphabet_min = [ chr(i) for i in range(97,123) ]
alphabet_maj = [ chr(i) for i in range(65,91) ]
chiffres = [ chr(i) for i in range(48,58) ]
caracteres_speciaux = [ '%' , '_' , '-' , '!' , '$' , '^' , '&' , '#' , '(' , ')' , '[' , ']' , '=' , '@']

class Generateur:
    def __init__(self, window):
        self.window = window
        window.geometry('450x300')
        window.title('Générateur de mot de passe')
        window.resizable(1,0)
        Label(window, text = "Nombre de caractères :").place(x = 5 , y = 5)
        self.nombre_caracteres = IntVar(window,value=20)
        self.n = Entry(window, width=3, textvariable=self.nombre_caracteres)
        self.n.place(x = 140, y=6)
        Label(window, text = "Alphabets à prendre en compte :").place(x = 5 , y = 40)
        self.checkMin = IntVar(value=1)
        t = 'Lettres minuscules : '
        for i in range(len(alphabet_min)-1):
            t += alphabet_min[i] + ','
        t += alphabet_min[-1]
        self.min = Checkbutton(window, text = t, variable = self.checkMin, \
                onvalue = 1, offvalue = 0, height=1, width = 50)
        self.min.place(x=0,y=60)
        self.checkMaj = IntVar(value=1)
        t = 'Lettres majuscules : '
        for i in range(len(alphabet_maj)-1):
            t += alphabet_maj[i] + ','
        t += alphabet_maj[-1]
        self.maj = Checkbutton(window, text = t, variable = self.checkMaj, \
                onvalue = 1, offvalue = 0, height=1, width = 55)
        self.maj.place(x=0,y=80)
        self.checkChiffres = IntVar(value=1)
        t = 'Chiffres : '
        for i in range(len(chiffres)-1):
            t += chiffres[i] + ','
        t += chiffres[-1]
        self.chif = Checkbutton(window, text = t, variable = self.checkChiffres, \
                onvalue = 1, offvalue = 0, height=1, width = 21)
        self.chif.place(x=0,y=100)
        self.checkCS = IntVar(value=1)
        t = 'Caractères spéciaux : '
        for i in range(len(caracteres_speciaux)-1):
            t += caracteres_speciaux[i] + ' , '
        t += caracteres_speciaux[-1]
        self.cs = Checkbutton(window, text = t, variable = self.checkCS, \
                onvalue = 1, offvalue = 0, height=1, width = 44)
        self.cs.place(x=0,y=120)
        self.checkPerso = IntVar(value=0)
        t = 'Caractères personnels :'
        self.liste_perso = StringVar()
        self.listePerso = Checkbutton(window, text = t, variable = self.checkPerso, \
                onvalue = 1, offvalue = 0, height=1, width = 18)
        self.listePerso.place(x=0,y=140)
        self.perso = Entry(window, width=30, textvariable=self.liste_perso)
        self.perso.place(x = 160, y=145)
        Label(window,text='(à la suite,sans virgule)').place(x=25,y=160)
        gener = Button(window, text = 'Générer',  width = 15, font = ('Tahoma', 10), command = self.generate)
        gener.place(x = 170 , y = 170)
        
    def generate(self):
        t = 'Mot de passe généré : ' + ' '*100
        Label(self.window, text = t).place(x = 5 , y = 220)
        n = int(self.n.get())
        min = int(self.checkMin.get())
        maj = int(self.checkMaj.get())
        chif = int(self.checkChiffres.get())
        cs = int(self.checkCS.get())
        perso = int(self.checkPerso.get())
        self.style = dict()
        i = 0      
        if min == 1:
            self.style[i] = alphabet_min
            i += 1
        if maj == 1:
            self.style[i] = alphabet_maj
            i += 1
        if chif == 1:
            self.style[i] = chiffres
            i += 1
        if cs == 1:
            self.style[i] = caracteres_speciaux
            i += 1
        if perso == 1:
            liste_personnelle = list(self.liste_perso.get().strip())
            self.style[i] = liste_personnelle
            i += 1           
        self.pwd = ''
        for j in range(n):
            s = randint(0,i-1)
            self.pwd += choice( self.style[s] )        
        t = 'Mot de passe généré : ' + self.pwd
        Label(self.window, text = t).place(x = 5 , y = 220)
        copie_presse_papier = Button(self.window, text = 'Copier en mémoire',  width = 20, font = ('Tahoma', 10), command = self.memory)
        copie_presse_papier.place(x = 150 , y = 260)
        
    def memory(self):
        self.window.clipboard_clear()
        self.window.clipboard_append(self.pwd)
        self.window.update()

root = Tk()
app = Generateur(root)
root.mainloop()