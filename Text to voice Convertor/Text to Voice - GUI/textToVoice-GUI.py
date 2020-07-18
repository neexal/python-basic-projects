import pyttsx3
from tkinter import *

window = Tk()
window.title("Text-to-Voice Convertor")
window.geometry("400x200")

tfText = Entry(window, text="Enter text here :")
tfText.grid(row=0, column = 0, columnspan=2, ipady=15, padx=10, ipadx=350)

def readText():
    textInput = tfText.get()
    engine = pyttsx3.init()
    engine.say(textInput)
    engine.runAndWait()


btnRead = Button(window, text="Read", bg="grey", fg="white", font="16", command=readText)
btnRead.grid(row=1, column=0, padx=50, pady=20, ipady=10, ipadx=10)


window.mainloop()