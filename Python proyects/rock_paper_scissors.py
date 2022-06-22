import tkinter as tk 
from tkinter import ttk
import random

#Atributos sobre ventana
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry('500x500+50+50')
root.resizable(False, False)

#Funciones
userSelection = -1
def logic():
#Seleccion de la ia
    iaList = [0, 1, 2]
    iaSelection = random.choice(iaList)
#Lógica del juego
    if iaSelection == userSelection:
        print("empate")
    elif (iaSelection == 0 and userSelection == 1) or (iaSelection == 1 and userSelection == 2) or (iaSelection == 2 and userSelection == 0):
        print("gana")
    else:
        print("pierde")

def Rock():
    userSelection = 0
    logic()
    userSelection = -1
    
def Paper():
    userSelection = 1
    logic()
    userSelection = -1
    
def Scissors():  
    userSelection = 2
    logic()
    userSelection = -1
    
    
#Objetos a mostrar en la ventana
rock = ttk.Button(root, text = "Rock", command = Rock).pack()
paper = ttk.Button(root, text = "Paper", command = Paper).pack()
scissors = ttk.Button(root, text = "Scissors", command = Scissors).pack()


#Arreglar blur de textos
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
finally:
    root.mainloop()