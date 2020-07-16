import string as s
import random

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

    leng = int(input('Enter the password length\n > '))
    random.shuffle(st)

    passwrd = ("".join(st[0:leng]))
    print(passwrd)

passGen()
