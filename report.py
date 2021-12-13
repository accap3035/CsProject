from tkinter import *
import tkinter as tk
import tkinter.font as tkFont
import hashlib
import os
def focus1(event):
    key.focus_set()
def focus2(event):
    checksum.focus_set()
def encryption(path, key):
    try:
        # take path of image as a input
        # taking encryption key as input
        # print path of image file and encryption key that
        # we are using
        print('The path of file : ', path)
        print('Key for encryption : ', key)

        # open file for reading purpose
        fin = open(path, 'rb')

        # storing image data in variable "image"
        image = fin.read()
        sha256_first = hashlib.sha256(image).hexdigest()
        print(f'{sha256_first} is your hash code save this to check later integrity of your data\n')
        fin.close()
        # converting image into byte array to
        # perform encryption easily on numeric data
        image = bytearray(image)
        # performing XOR operation on each value of bytearray
        for index, values in enumerate(image):
            image[index] = values ^ key
        # opening file for writing purpose
        fin = open(path, 'wb')
        # writing encrypted data in image
        fin.write(image)
        fin.close()
        print('Encryption Done...')

    except Exception:
        print('Error caught : ', Exception.__name__)
def decryption(path, key, hashcheck):
    # try block to handle the exception
    try:
        # take path of image as a input
        # taking decryption key as input
        # print path of image file and decryption key that we are using
        print('The path of file : ', path)
        print('Note : Encryption key and Decryption key must be same.')
        print('Key for Decryption : ', key)
        # open file for reading
        fin = open(path, 'rb')
        # storing image data in variable "image"
        image = fin.read()
        fin.close()
        # converting image into byte array to perform decryption easily on numeric data
        image = bytearray(image)
        # performing XOR operation on each value of bytearray
        for index, values in enumerate(image):
            image[index] = values ^ key
        # opening file for writing purpose
        fin = open(path, 'wb')

        # writing decryption data in image
        fin.write(image)
        fin.close()
        print('Decryption Done...')
        data = open(path, 'rb')
        image = data.read()
        sha256_later = hashlib.sha256(image).hexdigest()
        data.close()
        print(sha256_later)
        if (sha256_later == hashcheck):
            print(f'Your data was not changed during storage!')
        else:
            print(f'Get rid of this data, malicious data can be installed into it!!!')
            os.remove(path)
    except Exception:
        print('Error caught : ', Exception.__name__)

class App:
    def __init__(self, root):
        global path, key, checksum
        root.configure(background='light green')
        #setting title
        root.title("ProjcetApp")
        width = 550
        height = 400
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        #setting window size
        heading = Label(root, text="Future's app", bg="light green")
        path = Label(root, text="Path", bg="light green")
        key = Label(root, text="Key", bg="light green")
        checksum = Label(root, text="Hash(for decryption)", bg="light green")
        heading.grid(row=0, column=1)
        path.grid(row=1, column=0)
        key.grid(row=2, column=0)
        checksum.grid(row=3, column=0)
        path = Entry(root)
        key = Entry(root)
        checksum = Entry(root)
        path.grid(row=1, column=1, ipadx="100")
        key.grid(row=2, column=1, ipadx="100")
        checksum.grid(row=3, column=1, ipadx="100")
        path.bind("<Return>", focus1)
        key.bind("<Return>", focus2)
        GButton_97=tk.Button(root)
        GButton_97["bg"] = "Red"
        ft = tkFont.Font(family='Times',size=10)
        GButton_97["font"] = ft
        GButton_97["fg"] = "Black"
        GButton_97.grid(row=9, column=1)
        GButton_97["justify"] = "center"
        GButton_97["text"] = "Encrypt"
        GButton_97.place(x=280, y=100, width=70, height=40)
        GButton_97["command"] = self.GButton_97_command

        GButton_895= Button(root, )
        GButton_895["bg"] = "Red"
        ft = tkFont.Font(family='Times',size=10)
        GButton_895["font"] = ft
        GButton_895["fg"] = "Black"
        GButton_895.grid(row=10, column=2)
        GButton_895["justify"] = "center"
        GButton_895["text"] = "Decrypt"
        GButton_895.place(x=200, y=100, width=70,height=40)
        GButton_895["command"] = self.GButton_895_command

    def GButton_97_command(self):
        file = path.get()
        secret_key = key.get()
        encryption(file, int(secret_key))

    def GButton_895_command(self):
        file = path.get()
        secret_key = key.get()
        hashcheck = checksum.get()
        decryption(file, int(secret_key), hashcheck)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()