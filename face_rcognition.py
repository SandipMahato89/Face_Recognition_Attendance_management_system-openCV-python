from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
from time import strftime
from datetime import datetime
import os
import numpy as np



class Face_recognizer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1250x650+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 30, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1300, height=45)


        #1st image
        img_left = Image.open(r"C:\Users\HP\Desktop\face recognition system\images\29.png")
        img_left = img_left.resize((600, 610), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        f_lb = Label(self.root, image=self.photoimg_left)
        f_lb.place(x=0, y=45, width=600, height=610)


        #2nd image
        img_right = Image.open(r"C:\Users\HP\Desktop\face recognition system\images\33.jpg")
        img_right = img_right.resize((650, 610), Image.ANTIALIAS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        f_lb = Label(self.root, image=self.photoimg_right)
        f_lb.place(x=600, y=45, width=650, height=610)

        #......button.............
        b1_1 = Button(f_lb, text="Face Detector",command=self.face_recog,  cursor="hand2",font=("times new roman", 15, "bold"), bg="dark green", fg="white")
        b1_1.place(x=220, y=535, width=200, height=40)

    #===================attendence==================
    def mark_attendence(self, i,n,r,sec,dep):
        with open("attendence.csv","r+",newline="\n") as f:
            myDetaList=f.readlines()
            name_list=[]
            for line in myDetaList:
                entry=line.split((","))
                name_list.append(entry[0])
            if ((i not in name_list) and (n not in name_list) and (r not in name_list) and (sec not in name_list) and (dep not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{n},{r},{sec},{dep},{dtString},{d1},Present")




    # .................face recognition...............
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict = clf.predict(gray_image[y:y+h,x:x+w])
                confidence = int((100*(1-predict/300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="1234",database="face_recognizer")
                my_cursor = conn.cursor()

                my_cursor.execute("select StudentId from student1 where StudentId=" + str(id))
                i= my_cursor.fetchone()
                i="+".join(i)

                my_cursor.execute("select Name from student1 where StudentId=" + str(id))
                n = my_cursor.fetchone()
                n = "+".join(n)

                my_cursor.execute("select Roll from student1 where StudentId=" + str(id))
                r = my_cursor.fetchone()
                r = "+".join(r)

                my_cursor.execute("select Section from student1 where StudentId=" + str(id))
                sec = my_cursor.fetchone()
                sec = "+".join(sec)

                my_cursor.execute("select Dep from student1 where StudentId=" + str(id))
                dep = my_cursor.fetchone()
                dep = "+".join(dep)





                if confidence>77:

                    cv2.putText(img, f"ID:{i}", (x, y - 105), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 2)
                    cv2.putText(img, f"Name:{n}", (x, y - 80), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 2)
                    cv2.putText(img, f"Roll:{r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 2)
                    cv2.putText(img, f"Section:{sec}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 2)
                    cv2.putText(img, f"Department:{dep}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 2)
                    self.mark_attendence(i,n,r,sec,dep)
                else:
                    cv2.rectangle(img,(x, y), (x + w, y + h),(0, 0, 255), 3)
                    cv2.putText(img,"Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord = [x,y,w,h]

            return coord

        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to face recognition",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()




if __name__ == "__main__":
    root=Tk()
    obj=Face_recognizer(root)
    root.mainloop()