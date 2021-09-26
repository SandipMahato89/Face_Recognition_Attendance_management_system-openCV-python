from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os

class Register:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1250x650+0+0")
        self.root.title("Register")

        #...............variables...............
        self.var_fname=StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()


        #background image
        self.bg = ImageTk.PhotoImage(file=r"C:\Users\HP\Desktop\face recognition system\images\49.jpg")
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        # left image
        self.bg1 = ImageTk.PhotoImage(file=r"C:\Users\HP\Desktop\face recognition system\images\50.png")
        lbl_bg1 = Label(self.root, image=self.bg1)
        lbl_bg1.place(x=50, y=100, width=370, height=500)

        #main frame
        frame=Frame(self.root,bg="white")
        frame.place(x=420,y=100,width=800,height=500)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="dark green",bg="white")
        register_lbl.place(x=10,y=10)

        #Labels and entries...............
        #row1.........
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=80)

        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        fname_entry.place(x=50,y=110,width=250)

        lname = Label(frame, text="Last Name", font=("times new roman", 15, "bold"), bg="white")
        lname.place(x=370, y=80)

        lname_entry = ttk.Entry(frame,textvariable=self.var_lname ,font=("times new roman", 15, "bold"))
        lname_entry.place(x=370, y=110, width=250)

        # row2.................
        contact = Label(frame, text="Contact", font=("times new roman", 15, "bold"), bg="white")
        contact.place(x=50, y=150)

        contact_entry = ttk.Entry(frame,textvariable=self.var_contact, font=("times new roman", 15, "bold"))
        contact_entry.place(x=50, y=180, width=250)

        email = Label(frame, text="Email", font=("times new roman", 15, "bold"), bg="white")
        email.place(x=370, y=150)

        email_entry = ttk.Entry(frame, textvariable=self.var_email,font=("times new roman", 15, "bold"))
        email_entry.place(x=370, y=180, width=250)

        #row3...........................
        security_q = Label(frame, text="Security Question", font=("times new roman", 15, "bold"), bg="white")
        security_q.place(x=50, y=220)

        self.combo_security_q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman", 15, "bold"),state="readonly")
        self.combo_security_q["values"]=("Select","Your Birth Place","Your Favourite Cricketer","Your Pet name")
        self.combo_security_q.place(x=50, y=250, width=250)
        self.combo_security_q.current(0)

        security_a = Label(frame, text="Security Answer", font=("times new roman", 15, "bold"), bg="white")
        security_a.place(x=370, y=220)

        security_a_entry = ttk.Entry(frame, textvariable=self.var_securityA,font=("times new roman", 15, "bold"))
        security_a_entry.place(x=370, y=250, width=250)

        #row4.................
        password = Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white")
        password.place(x=50, y=290)

        password_entry = ttk.Entry(frame,textvariable=self.var_pass, font=("times new roman", 15, "bold"))
        password_entry.place(x=50, y=320, width=250)

        confirm_pass = Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white")
        confirm_pass.place(x=370, y=290)

        confirm_pass_entry = ttk.Entry(frame, textvariable=self.var_confpass,font=("times new roman", 15, "bold"))
        confirm_pass_entry.place(x=370, y=320, width=250)

        #check button
        self.var_check=IntVar()
        self.checkbtn=Checkbutton(frame,variable=self.var_check,text="I agree the terms and conditions",font=("times new roman", 12, "bold"),bg="white",onvalue=1,offvalue=0)
        self.checkbtn.place(x=50,y=360)

        #buttons........
        img=Image.open(r"C:\Users\HP\Desktop\face recognition system\images\54.png")
        img=img.resize((250,50),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2")
        b1.place(x=50,y=400,width=250)

        img1 = Image.open(r"C:\Users\HP\Desktop\face recognition system\images\53.jpg")
        img1 = img1.resize((250, 50), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        b1 = Button(frame, image=self.photoimage1, borderwidth=0, cursor="hand2")
        b1.place(x=350, y=400, width=250)


    #..............function Declaration.................
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","password & confirm password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms and conditions")
        else:
            #messagebox.showinfo("Success","Welcome......")

            conn = mysql.connector.connect(host="localhost", username="root", password="1234",database="login")
            my_cursor = conn.cursor()

            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist please try with another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_securityQ.get(),
                                                                                        self.var_securityA.get(),
                                                                                        self.var_pass.get()

                                                                                        ))

            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Registered Successfully.........")












if __name__ == "__main__":
    root=Tk()
    obj=Register(root)
    root.mainloop()
