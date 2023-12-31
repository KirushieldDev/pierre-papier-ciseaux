from tkinter import *
import random

list = ["pierre", "feuille", "ciseau"]
computerPoint = 0
userPoint = 0

window = Tk()
window.geometry("450x480")
window.title("Pierre - Feuille - Ciseau")
window.config(background="#148F77")
window.resizable(False, False) 

def playRock():
    global stateVar, computerChoiceTxtVar, list, computerPointVar, userPointTxtVar,computerPoint, userPoint
    computerChoice = random.choice(list)

    if computerChoice == "pierre":
        stateVar.set("Egalité, recommencez")
        computerChoiceTxtVar.set(f"Choix de l'ordinateur : {computerChoice}")
        userChoiceTxtVar.set("Votre choix : pierre")

        if computerPoint <1:
            computerPoint = 0
        computerPointVar.set(f"Ordinateur : {computerPoint}")

        if userPoint < 1:
            userPoint = 0
        userPointTxtVar.set(f"Vous : {userPoint}")


    elif computerChoice == "feuille":
        stateVar.set("Vous avez perdu !")
        computerChoiceTxtVar.set(f"Choix de l'ordinateur : {computerChoice}")
        userChoiceTxtVar.set(f"Votre choix : pierre")

        computerPoint += 1
        if computerPoint <1:
            computerPoint = 0
        computerPointVar.set(f"Ordinateur : {computerPoint}")

        if userPoint < 1:
            userPoint = 0
        userPointTxtVar.set(f"Vous : {userPoint}")


    elif computerChoice == "ciseau":
        stateVar.set("Vous avez gagné !")
        computerChoiceTxtVar.set(f"Choix de l'ordinateur : {computerChoice}")
        userChoiceTxtVar.set(f"Votre choix : pierre")

        if computerPoint < 1:
            computerPoint = 0
        computerPointVar.set(f"Ordinateur : {computerPoint}")

        userPoint += 1
        if userPoint < 1:
            userPoint = 0
        userPointTxtVar.set(f"Vous : {userPoint}")


def playPaper():
    global stateVar, computerChoiceTxtVar, list, computerPointVar, userPointTxtVar, computerPoint, userPoint
    computerChoice = random.choice(list)

    if computerChoice == "pierre":
        stateVar.set("Vous avez gagné !")
        computerChoiceTxtVar.set(f"Choix de l'ordinateur : {computerChoice}")
        userChoiceTxtVar.set("Votre choix : feuille")
        userPoint += 1
        if userPoint < 1:
            userPoint = 0
        userPointTxtVar.set(f"Vous : {userPoint}")

        
    elif computerChoice == "feuille":
        stateVar.set("Egalité, recommencez")
        computerChoiceTxtVar.set(f"Choix de l'ordinateur : {computerChoice}")
        userChoiceTxtVar.set(f"Votre choix : feuille")


    elif computerChoice == "ciseau":
        stateVar.set("Vous avez perdu !")
        computerChoiceTxtVar.set(f"Choix de l'ordinateur : {computerChoice}")
        userChoiceTxtVar.set(f"Votre choix : feuille")
        
        computerPoint += 1
        if computerPoint < 1:
            computerPoint = 0
        computerPointVar.set(f"Ordinateur : {computerPoint}")

        if userPoint < 1:
            userPoint = 0
        userPointTxtVar.set(f"Vous : {userPoint}")

def playScissor():
    global stateVar, computerChoiceTxtVar, list, computerPointVar, userPointTxtVar, computerPoint, userPoint
    computerChoice = random.choice(list)

    if computerChoice == "pierre":
        stateVar.set("Vous avez perdu !")
        computerChoiceTxtVar.set(f"Choix de l'ordinateur : {computerChoice}")
        userChoiceTxtVar.set(f"Votre choix : ciseau")

        computerPoint += 1
        if computerPoint < 1:
            computerPoint = 0
        computerPointVar.set(f"Ordinateur : {computerPoint}")


    elif computerChoice == "feuille":    
        stateVar.set("Vous avez gagné !")
        computerChoiceTxtVar.set(f"Choix de l'ordinateur : {computerChoice}")
        userChoiceTxtVar.set(f"Votre choix : ciseau")
        userPoint += 1
        if userPoint < 1:
            userPoint = 0
        userPointTxtVar.set(f"Vous : {userPoint}")

    elif computerChoice == "ciseau":
        stateVar.set("Egalité, recommencez")
        computerChoiceTxtVar.set(f"Choix de l'ordinateur : {computerChoice}")
        userChoiceTxtVar.set(f"Votre choix : ciseau")

        if userPoint < 1:
            userPoint = 0

        userPointTxtVar.set(f"Vous : {userPoint}")

frame_pricipale = Frame(window, bg="#148F77")
frame_pricipale.pack(expand=1, pady=15)

computerPointVar = StringVar()
computerPointVar.set("Ordinateur : 0")
computerPointTxt = Label(window, textvariable=computerPointVar, bg="#148F77", fg="#FDFEFE", font=("Courrier", 14))
computerPointTxt.place(x=10, y=10)

userPointTxtVar = StringVar()
userPointTxtVar.set("Vous : 0")
userPointTxt = Label(window, textvariable=userPointTxtVar, bg="#148F77", fg="#FDFEFE", font=("Courrier", 14))
userPointTxt.place(x=355, y=10)

title = Label(frame_pricipale, text="Choisir :", bg="#148F77", fg="#FDFEFE", font=("Courrier", 18))
title.pack(pady=15)

frame_button = Frame(frame_pricipale, bg="#148F77")
frame_button.pack(pady=15)

rock_button = Button(frame_button, text="Pierre", bg="#2E86C1", fg="#FDFEFE", font=("Courrier", 15), width=13, height= 2, command=playRock)
rock_button.pack()  

paper_button = Button(frame_button, text="Feuille", bg="#2E86C1", fg="#FDFEFE", font=("Courrier", 15), width=13, height= 2, command=playPaper)
paper_button.pack(pady=15) 

scissor_button = Button(frame_button, text="Ciseau", bg="#2E86C1", fg="#FDFEFE", font=("Courrier", 15), width=13, height= 2, command=playScissor)
scissor_button.pack()

userChoiceTxtVar = StringVar()
userChoiceTxtVar.set("Votre choix : ")
userChoiceTxt = Label(frame_pricipale, textvariable=userChoiceTxtVar, bg="#148F77", fg="#FDFEFE", font=("Courrier", 15))
userChoiceTxt.pack()

computerChoiceTxtVar = StringVar()
computerChoiceTxtVar.set("Choix de l'ordinateur : ")
computerChoiceTxt = Label(frame_pricipale, textvariable=computerChoiceTxtVar, bg="#148F77", fg="#FDFEFE", font=("Courrier", 15))
computerChoiceTxt.pack(pady=5)

stateVar = StringVar()
stateVar.set("Bonne chance !")
state = Label(frame_pricipale, textvariable=stateVar, bg="#148F77", fg="#FDFEFE", font=("Courrier", 15))
state.pack()

window.mainloop()

