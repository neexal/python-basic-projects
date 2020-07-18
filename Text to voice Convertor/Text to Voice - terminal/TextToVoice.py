import pyttsx3

textInput = input("Enter the text you want to read:\n> ")

engine = pyttsx3.init()
engine.say(textInput)
engine.runAndWait()
