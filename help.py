from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os


class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1250x650+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="HELP DESK", font=("times new roman", 30, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1300, height=45)

        img_top = Image.open(r"C:\Users\HP\Desktop\face recognition system\images\37.jpg")
        img_top = img_top.resize((1250, 610), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lb = Label(self.root, image=self.photoimg_top)
        f_lb.place(x=0, y=45, width=1250, height=610)

        dev_lbl = Label(f_lb, text="Email : tejsand4@gmail.com", font=("times new roman", 20, "bold"), bg="black",fg="white")
        dev_lbl.place(x=500, y=200, width=350, height=40)




if __name__ == "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()