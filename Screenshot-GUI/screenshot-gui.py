import pyautogui as pg
import time
from tkinter import *

def screenshot():
    name = int(round(time.time() * 1000))
    name = '{}.png'.format(name)
    Count()
    print('Capturing now!!!')
    image = pg.screenshot(name)
    image.show()

def Count():
    for i in range(5,0,-1):
        print('Capturing screenshot in ' + str(i))
        time.sleep(1)
    

window = Tk()
window.title('Screenshot-GUI')
window.configure(background = "gray")
window.geometry("500x200")

frame = Frame(window)
frame.pack()

label1 = Label(frame, text="Click to capture Screenshot.", height=2, background="brown")
label1.pack(side = LEFT)

btnCapture = Button(frame, 
                text="Capture",
                background="black",
                fg="white",
                command=screenshot)
btnCapture.pack(side = RIGHT)

frameMid = Frame(window)
frameMid.pack()

label2 = Label(frameMid, text="Click to quit.")
label2.pack(side = LEFT)

btnQuit = Button(frameMid, 
                text="Quit",
                background="red",
                fg="white",
                command=quit)
btnQuit.pack(side = RIGHT)


frameBtm = Frame(window)
frameBtm.pack()

lblCount = Label(frameBtm, text="Please wait for 5 sec to take Screenshot")
lblCount.pack()

window.mainloop()