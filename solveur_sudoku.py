from tkinter import Tk, Canvas
import copy

# Initialisation de la fenêtre
fenetre = Tk()
fenetre.title("Résolveur de Sudoku by Matt")
fenetre.resizable(False, False)

interface = Canvas(fenetre, width=400, height=500, bg="white")
interface.pack()

# Instructions
interface.create_text(5, 400, anchor="nw", tags="i",
                    text="Pour ajouter un chiffre, survolez la case et appuyez sur le pavé numérique.")
interface.create_text(5, 435, anchor="nw", tags="i",
                    text="Pour supprimer un chiffre, survolez la case et appuyez sur 'Retour'.")
interface.create_text(5, 455, anchor="nw", tags="i",
                    text="Pour résoudre la grille, appuyez sur 'Entrer'.")
interface.create_text(5, 480, anchor="nw", tags="i",
                    text="Pour tout effacer, appuyez sur 'Suppr'.")

# Dessin de la grille
interface.create_rectangle(12, 7, 15, 379, fill="black")
interface.create_rectangle(381, 7, 384, 379, fill="black")
interface.create_rectangle(12, 7, 384, 10, fill="black")
interface.create_rectangle(12, 376, 384, 379, fill="black")

cases = [[0] * 9 for _ in range(9)]
text_case = [[False] * 9 for _ in range(9)]
grille = [[0] * 9 for _ in range(9)]
grille_finie = [[False] * 9 for _ in range(9)]

ic = 0
ie = 0
for i in range(15, 369, 40):
    jc = 0
    je = 0
    for j in range(10, 364, 40):
        cases[jc][ic] = interface.create_rectangle(i + ie, j + je, i + ie + 40, j + je + 40,
                                                    fill="white", activefill="#e0e0e0")
        jc += 1
        if jc in [3, 6]:
            interface.create_rectangle(12, j + 43 + je, 384, j + 40 + je, fill="black")
            je += 3
    ic += 1
    if ic in [3, 6]:
        interface.create_rectangle(i + 43 + ie, 7, i + ie + 40, 379, fill="black")
        ie += 3


def event(touche):
    global grille
    touche_k = touche.keysym
    closest = interface.find_closest(touche.x, touche.y)[0]

    if touche_k in "123456789":
        for i in range(9):
            for j in range(9):
                if closest == cases[i][j]:
                    interface.delete(f"txt_{i}_{j}")
                    grille[i][j] = int(touche_k)
                    aff_g(i, j, touche_k)
                    return

    elif touche_k == "Return":
        chercher()

    elif touche_k == "Delete":
        nouv()

    elif touche_k == "BackSpace":
        for i in range(9):
            for j in range(9):
                if closest == cases[i][j]:
                    interface.delete(f"txt_{i}_{j}")
                    grille[i][j] = 0
                    return


def aff_g(x=-1, y=-1, nb=-1):
    if x == -1:
        interface.delete("case")
        for i in range(9):
            for j in range(9):
                if grille[i][j] != 0:
                    coords = interface.coords(cases[i][j])
                    cx, cy = (coords[0] + coords[2]) / 2, (coords[1] + coords[3]) / 2
                    interface.create_text(cx, cy, text=str(grille[i][j]),
                                        font=("Helvetica", 16, "bold"), fill="#0f0fa0", tags="case")
    else:
        coords = interface.coords(cases[x][y])
        cx, cy = (coords[0] + coords[2]) / 2, (coords[1] + coords[3]) / 2
        interface.create_text(cx, cy, text=str(nb), font=("Helvetica", 16, "bold"),
                            tags=("case", f"txt_{x}_{y}"))


def nouv():
    global grille, grille_finie
    grille = [[0] * 9 for _ in range(9)]
    grille_finie = [[False] * 9 for _ in range(9)]
    interface.delete("case")


def est_valide(l, c, nb):
    for i in range(9):
        if grille[l][i] == nb or grille[i][c] == nb:
            return False
    bl_l, bl_c = (l // 3) * 3, (c // 3) * 3
    for i in range(bl_l, bl_l + 3):
        for j in range(bl_c, bl_c + 3):
            if grille[i][j] == nb:
                return False
    return True


def resoudre():
    for l in range(9):
        for c in range(9):
            if grille[l][c] == 0:
                for nb in range(1, 10):
                    if est_valide(l, c, nb):
                        grille[l][c] = nb
                        if resoudre():
                            return True
                        grille[l][c] = 0
                return False
    return True


def chercher():
    if resoudre():
        aff_g()
    else:
        print("Aucune solution possible")


fenetre.bind("<Key>", event)
fenetre.mainloop()