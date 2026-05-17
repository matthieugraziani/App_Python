from langdetect import detect
from translate import Translator
import tkinter as tk
from tkinter import filedialog, messagebox
import pyttsx3

engine = pyttsx3.init()

def detecter_langue(texte):
    try:
        langue_detectee = detect(texte)
        return langue_detectee
    except Exception as e:
        print(f"Erreur lors de la détection de la langue : {e}")
        return None

def traduire_texte():
    texte = zone_texte.get("1.0", "end-1c")  # Obtenir le texte de la zone de texte

    # Détecter automatiquement la langue source
    langue_source_auto = detecter_langue(texte)
    if langue_source_auto:
        langue_source_var.set(langue_source_auto)
    else:
        messagebox.showwarning("Erreur", "Impossible de détecter automatiquement la langue source.")
        return

    langue_destination = langue_destination_var.get()

    try:
        # Créer un objet Translator
        traducteur = Translator(to_lang=langue_destination, from_lang=langue_source_auto)

        # Traduire le texte
        texte_traduit = traducteur.translate(texte)

        # Afficher le texte traduit dans une nouvelle fenêtre
        engine.say(texte_traduit)
        engine.runAndWait()
        messagebox.showinfo("Texte Traduit" , texte_traduit)

    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

# ... (le reste du code reste inchangé)


# Configuration de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Traducteur")

# Création de la zone de texte
zone_texte = tk.Text(fenetre)
zone_texte.pack()

# Options de langue
langues = ["fr", "en", "es", "de", "nl", "cr", "ru", "ja", "ar"]  # Vous pouvez ajouter d'autres langues au besoin

langue_source_var = tk.StringVar(fenetre)
langue_source_var.set(langues[0])  # Sélectionnez la première langue par défaut

# Langue destination
label_langue_destination = tk.Label(fenetre, text="Langue destination:")
label_langue_destination.pack()

langue_destination_var = tk.StringVar(fenetre)
langue_destination_var.set(langues[1])  # Sélectionnez la deuxième langue par défaut

menu_langue_destination = tk.OptionMenu(fenetre, langue_destination_var, *langues)
menu_langue_destination.pack()

# Bouton de traduction
bouton_traduire = tk.Button(fenetre, text="Traduire", command=traduire_texte)
bouton_traduire.pack()

fenetre.mainloop()