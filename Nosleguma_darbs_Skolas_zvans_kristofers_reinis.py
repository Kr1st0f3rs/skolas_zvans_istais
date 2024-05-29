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

#zvana animacija
def animacija(angle=0, direction=1):
    global tkimage
    
    rotated_image = image_zvans.rotate(angle)
    tkimage = ImageTk.PhotoImage(rotated_image)
    
    canva.itemconfig(image_izvada, image=tkimage)
    
    if direction == 1:
        new_angle = angle + 5
        if new_angle >= 45:
            direction = -1
    else:
        new_angle = angle - 5
        if new_angle <= -45:
            direction = 1
    
    logs.after(50, animacija, new_angle, direction)

canva.mainloop()