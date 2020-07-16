import string as s
import random
from tkinter import *

window = Tk()
window.title("Random Password Generator")
window.geometry("500x200")


label1 = Label(window, text = "Random Password Generator", font =("Times New Roman", 20)).pack()

label2 = Label(window, text="Enter the password length : ", font =("Times New Roman", 16)). pack()

txtField = Entry(window, width=25, bg ="gray", fg="black")
txtField.pack()



def passGen():
    s1 = s.ascii_uppercase
    s2 = s.ascii_lowercase
    s3 = s.punctuation 
    s4 = s.digits

    st = []
    st.extend(list(s1))
    st.extend(list(s2))
    st.extend(list(s3))
    st.extend(list(s4))

    random.shuffle(st)

    leng = int(txtField.get())

    passwrd = ("".join(st[0:leng]))
    lblpswd = Label(window, text = passwrd).pack()
    

btnGen = Button(window, text="Generate", bg ="blue", fg ="white", command=passGen).pack()


window.mainloop()