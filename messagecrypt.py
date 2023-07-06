from tkinter import *
from tkinter import messagebox
import base64
import os

def decrypt():
    password=code.get()

    #this can be some password.
    if password == "132435":
        screen2 = Toplevel(screen)
        encryptIcon = PhotoImage(file="lock.png")
        screen2.iconphoto(False, encryptIcon)
        screen2.title("Decrypted Text")
        screen2.geometry("400x200")
        screen2.configure(bg = "#59c11f")

        message=text1.get(1.0, END)
        decoded = message.encode("ascii")
        base64_bytes = base64.b64decode(decoded)
        decrypted = base64_bytes.decode("ascii")

        Label(screen2, text="DECRYPTED", font="arial", fg="white", bg="#59c11f").place(x=10, y=0)
        text2 = Text(screen2, font="Robote 12", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)

        text2.insert(END, decrypted)
        text2.config(state=DISABLED)

    elif password == "":
        messagebox.showerror("Encryption", "Provide the secret key!")
    elif password != "":
        messagebox.showerror("Encryption", "The Secret Key is wrong!")
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

    def reset():
        code.set("")
        text1.delete(1.0, END)

    Label(text="Enter text to encrypt or decrypt", fg="black", font=("calibri", 13)).place(x=10, y=10)
    text1 = Text(font="Robote 15", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text1.place(x=10, y=50, width=355, height=120)

    Label(text="Enter Secret Key to do crypto operations", fg="black", font=("calibri", 13)).place(x=10, y=170)
    
    code=StringVar()
    Entry(textvariable=code, width=19, bd=0, font=("arial", 15), show="*").place(x=10, y=200)

    Button(text="ENCRYPT", height=2, width=23, bg="red", fg="white", bd=0, command=encrypt).place(x=10, y=250)
    Button(text="DECRYPT", height=2, width=23, bg="#59c11f", fg="white", bd=0, command=decrypt).place(x=200, y=250)
    Button(text="RESET", height=2, width=50, bg="blue", fg="white", bd=0, command=reset).place(x=10, y=300)

    screen.mainloop()

main_screen()