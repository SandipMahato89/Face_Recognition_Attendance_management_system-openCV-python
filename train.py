from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1250x650+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="TRAIN DATA SET", font=("times new roman", 30, "bold"), bg="white",fg="red")
        title_lbl.place(x=0, y=0, width=1300, height=45)

        img_top = Image.open(r"C:\Users\HP\Desktop\face recognition system\images\16.jpg")
        img_top = img_top.resize((1250,220), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_lb = Label(self.root, image=self.photoimg_top)
        f_lb.place(x=0, y=45, width=1250, height=180)

        #button
        b1_1 = Button(self.root, text="TRAIN DATA",command=self.train_classifier, cursor="hand2", font=("time new roman", 30, "bold"), bg="yellow",fg="blue")
        b1_1.place(x=0, y=225, width=1250, height=60)

        img_bottom = Image.open(r"C:\Users\HP\Desktop\face recognition system\images\30.jpg")
        img_bottom = img_bottom.resize((1250, 375), Image.ANTIALIAS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        f_lb = Label(self.root, image=self.photoimg_bottom)
        f_lb.place(x=0, y=285, width=1250, height=375)

    def train_classifier(self):
        data_dir=(r"C:\Users\HP\Desktop\face recognition system\data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')  #gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])


            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)


        #............train classifier and save..............
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!!")








if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()

