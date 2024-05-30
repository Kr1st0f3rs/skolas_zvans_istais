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

# zvans bilde
image_zvans = Image.open("zvans.png")
tkimage = ImageTk.PhotoImage(image_zvans)
image_izvada = canva.create_image(280, 250, image=tkimage)

# zvana animacija
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

# izveido pūlksteni kas rāda laiku
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

# Track the last time the audio was played to prevent multiple plays within the same period
last_played = ""

def stundu_zvans():
    global last_played
    string = strftime('%H:%M:%S')
    play_times = {
        "08:10:00": "1",
        "09:10:00": "2",
        "10:00:00": "3",
        "10:50:00": "4",
        "11:40:00": "5",
        "12:30:00": "6",
        "13:20:00": "7",
        "14:10:00": "8",
        "15:00:00": "9",
        "15:50:00": "10"
    }

    if string in play_times and string != last_played:
        audio()
        print(play_times[string])
        last_played = string

i = 0
def check_time():
    global i
    stundu_zvans()
    i += 1
    logs.after(1000, check_time)

update_time()
logs.after(1000, check_time)
if i > 0 and i < 4:
    animacija()
logs.mainloop()
