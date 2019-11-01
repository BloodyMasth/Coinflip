# coding=utf-8
from tkinter import *
import random
# Auteur: Bloodyfire
# Dernière modification le 15/07/2019
# Pile ou face avec interface
# https://pastebin.com/nJn0vUj7

# Fenètre 1
# Créer la fenètre
window = Tk()

# Paramètre de la fenètre
window.title("Pile ou Face")  # Titre
window.geometry("720x480")  # Taille de la fenètre
window.minsize(705, 485)
window.iconbitmap("coin.ico")  # Icone
window.config(background='#cdc217')

# Numero de la fenètre
global window_num
window_num = 1

# Créer la frame
original_frame = Frame(window, bg="#cdc217")
original_frame.grid(padx=120, pady=100)

# Texte de la fenètre
label_title = Label(original_frame, text="Jeu du Pile ou Face", font=("Arial", 40), bg="#cdc217", fg="#000000")
label_title.grid()
label_subtitle = Label(original_frame, text="Voulez-vous jouer ?", font=("Arial", 20), bg="#cdc217", fg="#000000")
label_subtitle.grid()

def lets_go():
    original_frame.destroy()
    coinflip()

# Bouton dans la fenètre
start_button = Button(original_frame, text="C'est Parti !", font=("Arial", 20), bg="black", fg="#cdc217", command=lets_go)
start_button.grid(pady=20)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Fenètre 2
# Initialisation/Déclaration des variables
score_win = 0
score_loose = 0
parties = 0

# Fonction du jeu
def game():
    # Nettoyage des entrées
    message_exit.delete(0, END)
    winrate_exit.delete(0, END)
    score_win_exit.delete(0, END)
    score_loose_exit.delete(0, END)

    # Tirage de la piece
    global score_win, score_loose, parties
    choix_user = int(entree.get())
    piece = random.randint(1, 2)
    parties = parties + 1

    # Choix + Affichage de l'image tail/head
    if piece == 1:
        tails_frame = Frame(piece_frame, bg='#cdc217', bd=1, relief=SUNKEN)
        tails_frame.grid(row=0, column=1, pady=20)
        # Image tails
        width3 = 100
        height3 = 100
        canvas_tails = Canvas(tails_frame, width=100, height=100, bg='#cdc217', bd=2, highlightthickness=0)
        canvas_tails.create_image(width3 / 2, height3 / 2, image=image_tails)
        canvas_tails.grid()
    if piece == 2:
        head_frame = Frame(piece_frame, bg='#cdc217', bd=1, relief=SUNKEN)
        head_frame.grid(row=0, column=1, pady=20)
        # Image heads
        width2 = 100
        height2 = 100
        canvas_heads = Canvas(head_frame, width=100, height=100, bg='#cdc217', bd=2, highlightthickness=0)
        canvas_heads.create_image(width2 / 2, height2 / 2, image=image_heads)
        canvas_heads.grid()

    # Les différentes issues possible
    # Victoire du joueur
    if piece == 1 and choix_user == 1:
        message = "C'est pile, vous avez gagné(e) !"
        score_win = score_win + 1
        message_exit.insert(0, message)
        score_win_exit.insert(0, "W: ")
        score_win_exit.insert(3, score_win)
        score_loose_exit.insert(0, "L: ")
        score_loose_exit.insert(3, score_loose)
        winrate = (score_win / parties) * 100
        winrate = int(winrate * 100)
        winrate = winrate / 100
        winrate_exit.insert(0, "Winrate: ")
        winrate_exit.insert(9, winrate)
        winrate_exit.insert(14, "%")
    if piece == 2 and choix_user == 2:
        message = "C'est face, vous avez gagné(e) !"
        score_win = score_win + 1
        message_exit.insert(0, message)
        score_win_exit.insert(0, "W: ")
        score_win_exit.insert(3, score_win)
        score_loose_exit.insert(0, "L: ")
        score_loose_exit.insert(3, score_loose)
        winrate = (score_win / parties) * 100
        winrate = int(winrate*100)
        winrate = winrate/100
        winrate_exit.insert(0, "Winrate: ")
        winrate_exit.insert(9, winrate)
        winrate_exit.insert(14, "%")

    # Défaite du joueur
    if piece == 1 and choix_user == 2:
        message = "C'est pile, vous avez perdu(e) !"
        score_loose = score_loose + 1
        message_exit.insert(0, message)
        score_win_exit.insert(0, "W: ")
        score_loose_exit.insert(3, score_loose)
        score_loose_exit.insert(0, "L: ")
        score_win_exit.insert(3, score_win)
        winrate = (score_win / parties) * 100
        winrate = int(winrate * 100)
        winrate = winrate / 100
        winrate_exit.insert(0, "Winrate: ")
        winrate_exit.insert(9, winrate)
        winrate_exit.insert(14, "%")
    if piece == 2 and choix_user == 1:
        message = "C'est face, vous avez perdu(e) !"
        score_loose = score_loose + 1
        message_exit.insert(0, message)
        score_win_exit.insert(0, "W: ")
        score_loose_exit.insert(3, score_loose)
        score_loose_exit.insert(0, "L: ")
        score_win_exit.insert(3, score_win)
        winrate = (score_win / parties) * 100
        winrate = int(winrate * 100)
        winrate = winrate / 100
        winrate_exit.insert(0, "Winrate: ")
        winrate_exit.insert(9, winrate)
        winrate_exit.insert(14, "%")

# Fonction de la fenètre
def coinflip():
    global window_num
    if window_num == 3:
        frame_info.destroy()

    # Numero de la fenètre
    window_num = 2

    # Créer les frames
    global frame2
    frame2 = Frame(window, bg="#cdc217")
    frame2.grid(row=1, column=1, padx=100)
    loose_frame = Frame(frame2, bg='#cdc217')
    loose_frame.grid(row=7, column=0, sticky=E, padx=10, pady=10)
    win_frame = Frame(frame2, bg='#cdc217')
    win_frame.grid(row=7, column=0, sticky=W, padx=10, pady=10)
    global piece_frame
    piece_frame = Frame(window, bg='#cdc217')
    piece_frame.grid(row=0, column=1)
    global white_frame
    white_frame = Frame(piece_frame, bg='#cdc217')
    white_frame.grid(row=0, column=1,pady=20)

    # Texte de la fenètre
    label_title2 = Label(frame2, text="Choisisser le coté sur lequel vous misez \n 1- Pile \n 2- Face", font=("Arial", 20), bg='#cdc217', fg='Black')
    label_title2.grid(row=0, column=0)

    # Choix de l'utilisateur
    global entree
    entree = Entry(frame2, width=3)
    entree.grid()

    # Bouton jouer
    play_button = Button(frame2, text="Jouer", font=("Arial", 20), bg='#cdc217', fg='Black', command=game)
    play_button.grid(pady=10)

    # Sortie message
    global message_exit
    message_exit = Entry(frame2, font=("Arial", 15), bg='#cdc217', fg='Black', width=26)
    message_exit.grid(pady=10)

    # Sortie Winrate
    global winrate_exit
    winrate_text = StringVar()
    winrate_text.set('Winrate (en %): ')
    winrate_exit = Entry(frame2, textvariable=winrate_text,font=("Arial", 15), bg='#cdc217', fg='Black', width=15)
    winrate_exit.grid()

    # Sortie des points
    global score_win_exit
    win_text = StringVar()
    win_text.set('W:')
    score_win_exit = Entry(win_frame, textvariable=win_text ,font=("Arial", 15), bg='#cdc217', fg='Black', width=5)
    score_win_exit.grid()
    global score_loose_exit
    loose_text = StringVar()
    loose_text.set('L:')
    score_loose_exit = Entry(loose_frame, textvariable=loose_text, font=("Arial", 15), bg='#cdc217', fg='Black', width=5)
    score_loose_exit.grid()

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Image heads
image_heads = PhotoImage(file="heads.png").zoom(6).subsample(32)

# Image tails
image_tails = PhotoImage(file="tails.png").zoom(11).subsample(32)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def a_propos():
    global window_num
    if window_num == 1:
        original_frame.destroy()
    if window_num == 2:
        frame2.destroy()
        piece_frame.destroy()

    # Numero de la fenetre
    window_num = 3

    # Créer les frames
    global frame_info
    frame_info = Frame(window, bg='#4065A4')
    frame_info.grid(padx=150, pady=150)

    # Texte de la fenètre
    label_title_info = Label(frame_info, text="Pile ou Face réalisé par \n BloodyFire", font=("Arial", 30), bg='#cdc217', fg='Black')
    label_title_info.grid()

# Barre de menu
menu_bar = Menu(window)
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Fichier", menu=file_menu)
file_menu.add_command(label="Quitter", command=window.quit)
menu_bar.add_cascade(label="Jouer", command=coinflip)
file_menu.add_command(label="A propos", command=a_propos)


window.config(menu=menu_bar)

window.mainloop()