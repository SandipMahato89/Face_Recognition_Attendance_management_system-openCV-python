from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from main import Face_Recognition
import getpass


def main():
    win=Tk()
    app=Login_window(win)
    win.mainloop()



class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1250x650+0+0")
        self.root.title("Login")

        self.var_email = StringVar()
        self.var_pass = StringVar()

        #background image
        self.bg = ImageTk.PhotoImage(file=r"C:\Users\HP\Desktop\face recognition system\images\39.jpg")
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        #frame
        frame=Frame(self.root,bg="black")
        frame.place(x=450,y=100,width=340,height=450)

        img_top = Image.open(r"C:\Users\HP\Desktop\face recognition system\images\42.png")
        img_top = img_top.resize((100, 100), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_lb = Label(image=self.photoimg_top,bg="black",borderwidth=0)
        f_lb.place(x=565, y=110, width=100, height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman","20","bold"),fg="white",bg="black")
        get_str.place(x=95,y=105)

        #labels
        username=Label(frame,text="Username",font=("times new roman","15","bold"),fg="white",bg="black")
        username.place(x=70,y=155)

        self.textuser=ttk.Entry(frame,font=("times new roman","15","bold"))
        self.textuser.place(x=40,y=180,width=270)

        password = Label(frame, text="Password", font=("times new roman", "15", "bold"), fg="white", bg="black")
        password.place(x=70, y=225)

        self.textpass = ttk.Entry(frame, font=("times new roman", "15", "bold"))
        self.textpass.place(x=40, y=250, width=270)

        #===========Icon Images========
        img1 = Image.open(r"C:\Users\HP\Desktop\face recognition system\images\45.png")
        img1 = img1.resize((25, 25), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lb = Label(image=self.photoimg1, bg="black", borderwidth=0)
        f_lb.place(x=490, y=253, width=25, height=25)

        img2 = Image.open(r"C:\Users\HP\Desktop\face recognition system\images\46.png")
        img2 = img2.resize((25, 25), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lb = Label(image=self.photoimg2, bg="black", borderwidth=0)
        f_lb.place(x=490, y=323, width=25, height=25)

        #login Button
        loginbtn=Button(frame,text="Login",command=self.login,font=("times new roman", "15", "bold"),borderwidth=0,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)

        #register Button
        registerbtn = Button(frame, text="New User Register", command=self.register_window,font=("times new roman", "10", "bold"),borderwidth=0, fg="white",bg="black", activeforeground="white", activebackground="black")
        registerbtn.place(x=20, y=350, width=120)

        #forgot password Button
        forgotbtn = Button(frame, text="Forgot Password",command=self.forgot_pass, font=("times new roman", "10", "bold"),borderwidth=0, fg="white",bg="black", activeforeground="white", activebackground="black")
        forgotbtn.place(x=15, y=370, width=120)


    #...............login function.............
    def login(self):

        if self.textuser.get()=="" or self.textpass.get()=="":
            messagebox.showerror("Error","All fields required")
        elif self.textuser.get()=="kappu" and self.textpass.get()=="1234":
            messagebox.showinfo("Success","Welcome.....")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="login")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where email=%s and pass=%s",(
                                                                                    self.textuser.get(),
                                                                                    self.textpass.get()
                                                                                ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username & Password")
            else:
                open_main=messagebox.askyesno("Yes No","Access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()

    #==========reset password==================
    def reset_pass(self):
        if self.combo_security_q.get()=="Select":
            messagebox.showerror("Error","Select the security question",parent=self.root2)
        elif self.security_a_entry.get()=="":
            messagebox.showerror("Error","Please enter the security answer",parent=self.root2)
        elif self.text_newpass.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="login")
            my_cursor = conn.cursor()
            qury=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value1=(self.textuser.get(),self.combo_security_q.get(),self.security_a_entry.get())
            my_cursor.execute(qury,value1)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter the correct answer",parent=self.root2)
            else:
                quer1=("update register set pass=%s where email=%s")
                val=(self.text_newpass.get(),self.textuser.get())
                my_cursor.execute(quer1,val)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset,please login with new password",parent=self.root2)
                self.root2.destroy()





    #............forgot password function............
    def forgot_pass(self):
        if self.textuser.get()=="":
            messagebox.showerror("Error","Please enter the email address to reset password")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="login")
            my_cursor = conn.cursor()
            query=("select * from register where email=%s")
            value=(self.textuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            #print(row)

            if row==None:
                messagebox.showerror("Error","Please the valid username")
            else:
                conn.close()

                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+410+110")

                l=Label(self.root2,text="Forgot Password",font=("times new roman", "15", "bold"),fg="red",bg="white")
                l.place(x=0,y=0,relwidth=1)

                security_q = Label(self.root2, text="Security Question", font=("times new roman", 15, "bold"), bg="white")
                security_q.place(x=50, y=80)

                self.combo_security_q = ttk.Combobox(self.root2,  font=("times new roman", 15, "bold"), state="readonly")
                self.combo_security_q["values"] = ("Select", "Your Birth Place", "Your Favourite Cricketer", "Your Pet name")
                self.combo_security_q.place(x=50, y=110, width=250)
                self.combo_security_q.current(0)

                security_a = Label(self.root2, text="Security Answer", font=("times new roman", 15, "bold"), bg="white")
                security_a.place(x=50, y=150)

                self.security_a_entry = ttk.Entry(self.root2,font=("times new roman", 15, "bold"))
                self.security_a_entry.place(x=50, y=180, width=250)

                new_password = Label(self.root2, text="New Password", font=("times new roman", 15, "bold"), bg="white")
                new_password.place(x=50, y=220)

                self.text_newpass = ttk.Entry(self.root2, font=("times new roman", 15, "bold"))
                self.text_newpass.place(x=50, y=250, width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_pass, font=("times new roman", 15, "bold"), bg="green",fg="white")
                btn.place(x=120,y=320)







    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)


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
        #register button
        img=Image.open(r"C:\Users\HP\Desktop\face recognition system\images\54.png")
        img=img.resize((250,50),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2")
        b1.place(x=50,y=400,width=250)


        #login button
        img1 = Image.open(r"C:\Users\HP\Desktop\face recognition system\images\53.jpg")
        img1 = img1.resize((250, 50), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        b1 = Button(frame,command=self.return_login, image=self.photoimage1, borderwidth=0, cursor="hand2")
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

    def return_login(self):
        self.root.destroy()





if __name__ == "__main__":
    main()
