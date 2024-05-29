import tkinter as Tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter.ttk import *



Garums = 700
Platums = 800
logs = Tk()
logs.title("Skolas zvans")
canva = Canvas(logs, width=Platums, height=Garums, bg="white")
canva.pack()

#zvans bilde
image_zvans = Image.open("zvans.png")
tkimage = ImageTk.PhotoImage(image_zvans)
image_izvada = canva.create_image(280, 250, image=tkimage)

canva.mainloop()