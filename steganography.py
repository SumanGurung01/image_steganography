"""
    Date : Thu Jan 12 2023 16:52:14 GMT+0530 (India Standard Time)
    Author : Suman Gurung
    Description : Image Steganography using LSB method in python and tkinter  
"""

import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image , ImageTk
import os
from stegano import lsb

# constants
DIMENSION = "720x520"
BG_COLOR="#565656"

# root window configutation
root = Tk()
root.title("Steganography using Python")
root.geometry(DIMENSION)
root.resizable(False,False)
root.configure(bg=BG_COLOR)

# options
def open_image():
    global file
    file = filedialog.askopenfilename(initialdir=os.getcwd() , title="Select Image" , filetype=(("PNG file","*.png"), ("JPG file","*.jpg") , ("All file","*.txt")))
    img = Image.open(file)
    img = ImageTk.PhotoImage(img)
    frame_1_label.configure(image=img , width=330 , height=330)
    frame_1_label.image = img

def hide_message():
    try:
        file
    except NameError:
        messagebox.showerror("Error", "Please Select an Image")

    global secret_message
    message = text.get(1.0,END)

    secret_message = lsb.hide(str(file) , message)
    text.delete(1.0,END)
    messagebox.showinfo("Message", "Message Hidden")

def show_message():
    try:
        file
    except NameError:
        messagebox.showerror("Error", "Please Select an Image")
    
    try:
        file
    except IndexError:
        messagebox.showerror("Error", "No hidden message")

    else:
        clear_message = lsb.reveal(file)
        text.delete(1.0,END)
        text.insert(END,clear_message) 
       
def save_image():
    try:
        secret_message
    except NameError:
        messagebox.showerror("Error", "please open an image and hide a message")
    secret_message.save("hidden.png")
    messagebox.showinfo("Message", "Image Saved as 'hidden.png'")


def main():
    Label(root,text="Hide Message in Images",bg="#565656" , fg="white", font="arial 20").place(x=200,y=10)

    frame_1 = Frame(root , bg="black" , width="350" , height="350").place(x=10 , y=70)   # image
    frame_2 = Frame(root , bg="white" , width="350" , height="350").place(x=360 , y=70)  # text
    frame_3 = Frame(root , bg="#565656" , width="700" , height="100").place(x=10 , y=500)  # option

    global frame_1_label
    frame_1_label = Label(frame_1 , bg="black")
    frame_1_label.place(x=20,y=80)
    
    global text
    text = Text(frame_2 , font="Robote 20" , bg="white" , fg="black" , wrap=WORD)
    text.place(x=360,y=70 , width=350 , height=350)

    Button(frame_3 , text="Open Image" , width=15 ,height=2 , command=open_image).place(x=60 , y=450)
    Button(frame_3 , text="Save Image" , width=15 ,height=2 , command=save_image).place(x=180 , y=450)
    Button(frame_3 , text="Hide Message" , width=15 ,height=2 , command=hide_message).place(x=420 , y=450)
    Button(frame_3 , text="Show Message" , width=15 ,height=2 , command=show_message).place(x=540 , y=450)

    root.mainloop()

if __name__ == "__main__":
    main()




