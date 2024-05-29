import tkinter as Tk
from tkinter import *

Garums = 700
Platums = 800
logs = Tk()
logs.title("Skolas zvans")
canva = Canvas(logs, width=Platums, height=Garums, bg="white")
canva.pack()

canva.mainloop()