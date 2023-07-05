from tkinter import *
from tkinter import messagebox
import base64
import os


def encrypt():
    password=code.get()

    #this can be some password.
    if password == "132435":
        screen1 = Toplevel(screen)
        encryptIcon = PhotoImage(file="lock.png")
        screen1.iconphoto(False, encryptIcon)
        screen1.title("Encrypted Text")
        screen1.geometry("400x200")
        screen1.configure(bg = "red")

        message=text1.get(1.0, END)
        encoded = message.encode("ascii")
        base64_bytes = base64.b64encode(encoded)
        encrypted = base64_bytes.decode("ascii")

        Label(screen1, text="ENCRYPTED", font="arial", fg="white", bg="red").place(x=10, y=0)
        text2 = Text(screen1, font="Robote 12", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)

        text2.insert(END, encrypted)
        text2.config(state=DISABLED)

    elif password == "":
        messagebox.showerror("Encryption", "Provide the secret key!")
    elif password != "":
        messagebox.showerror("Encryption", "The Secret Key is wrong!")

def main_screen():
    global screen
    global code
    global text1

    screen = Tk()
    screen.geometry("400x430")
    icon_img = PhotoImage(file="lockandkey.png")
    screen.iconphoto(False, icon_img)
    screen.title("MessageCryptor")
    Label(text="Enter text to encrypt or decrypt", fg="black", font=("calibri", 13)).place(x=10, y=10)
    text1 = Text(font="Robote 15", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text1.place(x=10, y=50, width=355, height=120)

    Label(text="Enter Secret Key to do crypto operations", fg="black", font=("calibri", 13)).place(x=10, y=170)
    
    code=StringVar()
    Entry(textvariable=code, width=19, bd=0, font=("arial", 15), show="*").place(x=10, y=200)

    Button(text="ENCRYPT", height=2, width=23, bg="red", fg="white", bd=0, command=encrypt).place(x=10, y=250)
    

    screen.mainloop()

main_screen()
