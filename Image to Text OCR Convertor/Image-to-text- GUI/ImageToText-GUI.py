import os
import pytesseract
from PIL import Image
from tkinter import Label, Button, filedialog, Tk
from tkinter import filedialog

window = Tk()
window.title("Image to Text OCR Convertor")
window.geometry("500x200")

label1 = Label(window, text = "Upload a image to read text from :", font =("Times New Roman", 20))
label1.grid(row=0, column=0)

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

def fileSelect():
    filename = filedialog.askopenfilename(initialdir="/", title="Select an Image to convert to text", filetype=(("jpeg","*.jpg"),("png","*.png"),("All files","*.*")))
    img = Image.open(filename)
    textCon = pytesseract.image_to_string(img)

    textImg = Label(window, text="", font=16)
    textImg.grid(row=1,column=0,pady=20)
    textImg.configure(text=textCon)


btnUpload = Button(window, text="Upload Image", bg="blue",fg="white", command=fileSelect)
btnUpload.grid(row=0, column=1)


window.mainloop()