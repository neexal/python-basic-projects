import os
import pytesseract
from PIL import Image
import pyttsx3

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

def Convertor():
    engine = pyttsx3.init()
    img = Image.open(r'C:\Users\neexal\Desktop\Python-Projects\Image to Text OCR Convertor\Image-to-Text- terminal\img.jpg')
    text = pytesseract.image_to_string(img)
    print("> " + text)
    print("\nReading the text :")
    engine.say(text)
    engine.runAndWait()


Convertor()