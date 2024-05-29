import tkinter as Tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter.ttk import *
from time import strftime
import playsound

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

#izveido pūlksteni kas rāda laiku
def update_time():
    global string
    string = strftime('%H:%M:%S')
    lbl.config(text=string)
    lbl.after(1000, update_time)
    
lbl = Label(canva, font=('calibri', 40, 'bold'),
            background='white',
            foreground='black')

lbl.place(x=220, y=580)

def audio():
    playsound.playsound("zvans.mp3")
    


def stundu_zvans():
    string = strftime('%H:%M:%S')
    if string <= "08:00" or string >="16:31":
        pass
    elif string <= "08:10" or string >= "08:50":
        audio()
    elif string <="9:10" or string >="9:50":
        audio()
    elif string <="10:00" or string >="10:40":
        audio()
    elif string <="10:50" or string >="11:30":
        audio()
    elif string <="11:40" or string >="12:20":
        audio()
    elif string <="12:30" or string >="13:10":
        audio()
    elif string <="13:20" or string >="14:00":
        audio()
    elif string <="14:10" or string >="14:50":
        audio()
    elif string <="15:00" or string >="15:40":
        audio()
    elif string <="15:50" or string >="16:30":
        audio()
    

i=0
def check_time():
    global i, stundu_zvans
    if i < 3:
        stundu_zvans()
        i+=1
        logs.after(1000, check_time)
    else:
        pass

update_time()
logs.after(1000, check_time)
if i > 0 and i<4:
    animacija()
logs.mainloop()