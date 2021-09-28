from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)

### hardware
yellow = LED(4)
green = LED(17)
red = LED(22)

### GUI definitions ###
win = Tk()
win.title("LED Toggler")
myFont = tkinter.font.Font(family = 'Helvetica',size=12,weight = "bold")

### Event Function ###
def green_toggle():
    if green.is_lit:
        green.off()
        green_btn["text"] = "Green >> off"
    else:
        green.on()
        green_btn["text"] = "Green >> on"

def red_toggle():
    if red.is_lit:
        red.off()
        red_btn["text"] = "Green >> off"
    else:
        red.on()
        green_btn["text"] = "Green >> on"
        
def yellow_toggle():
    if yellow.is_lit:
        yellow.off()
        yellow_btn["text"] = "Green >> off"
    else:
        yellow.on()
        yellow_btn["text"] = "Green >> on"

### Widgets ###
green_btn = Button(win,text = "Green >> off",font = myFont, command = green_toggle,bg = 'bisque2',height = 1,width =24)
red_btn = Button(win,text = "red >> off",font = myFont, command = red_toggle,bg = 'bisque2',height = 1,width =24)
yellow_btn = Button(win,text = "yellow >> off",font = myFont, command = yellow_toggle,bg = 'bisque2',height = 1,width =24)

green_btn.grid(row=0,column=1)
red_btn.grid(row=1,column=1)
yellow_btn.grid(row=2,column=1)

