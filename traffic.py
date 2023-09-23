
from tkinter import *
import time

win=Tk()
win.title('Traffic Signal')

canvas1=Canvas(win,height=200,width=500,bg='White')
canvas1.pack()

canvas1.create_rectangle(50,50,300,125,fill='Grey',width=5)
canvas1.create_rectangle(155,125,195,190,fill='Grey',width=5)
red=canvas1.create_oval(60,60,100,100,fill='Black',width=2)
orange=canvas1.create_oval(150,60,190,100,fill='Black',width=2)
green=canvas1.create_oval(250,60,290,100,fill='Black',width=2)


a=5

while True:
    def red_on():
        for i in range(a):
            red=canvas1.create_oval(60,60,100,100,fill='Red',width=2)
            win.update()
            time.sleep(0.60)
            
    def red_off():
        for i in range(a):
            red=canvas1.create_oval(60,60,100,100,fill='Black',width=2)
            win.update()
            time.sleep(.00001)
            
    def orange_on():
        for i in range(a):
            orange=canvas1.create_oval(150,60,190,100,fill='Orange',width=2)
            win.update()
            time.sleep(0.60)
            
    def orange_off():
        for i in range(a):
            orange=canvas1.create_oval(150,60,190,100,fill='Black',width=2)
            win.update()
            time.sleep(0.00001)
            
    def green_on():
        for i in range(a):
            green=canvas1.create_oval(250,60,290,100,fill='Green',width=2)
            win.update()
            time.sleep(0.60)
            
    def green_off():
        for i in range(a):
            green=canvas1.create_oval(250,60,290,100,fill='Black',width=2)
            win.update()
            time.sleep(0.00001)

    red_on()
    red_off()
    orange_on()
    orange_off()
    green_on()
    green_off()

win.mainloop()
