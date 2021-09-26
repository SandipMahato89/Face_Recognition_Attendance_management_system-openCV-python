from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os


class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1250x650+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="DEVELOPER", font=("times new roman", 30, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1300, height=45)

        img_top = Image.open(r"C:\Users\HP\Desktop\face recognition system\images\35.png")
        img_top = img_top.resize((1250, 610), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lb = Label(self.root, image=self.photoimg_top)
        f_lb.place(x=0, y=45, width=1250, height=610)

        # MAIN frame
        main_frame = Frame(f_lb, bd=2, bg="yellow")
        main_frame.place(x=940, y=0, width=300, height=300)

        img_top1 = Image.open(r"C:\Users\HP\Desktop\face recognition system\images\own.jpeg")
        img_top1 = img_top1.resize((250, 350), Image.ANTIALIAS)
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)

        f_lb = Label(main_frame, image=self.photoimg_top1)
        f_lb.place(x=50, y=0, width=200, height=200)

        #Developer information

        dev_lbl = Label(main_frame, text="Hi my name, Sandip Mahato", font=("times new roman", 18, "bold"), bg="red", fg="white")
        dev_lbl.place(x=0, y=220, width=295, height=20)

        dev_lbl = Label(main_frame, text="I am a full stack developer", font=("times new roman", 18, "bold"), bg="red",fg="white")
        dev_lbl.place(x=0, y=255, width=290, height=20)



if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()