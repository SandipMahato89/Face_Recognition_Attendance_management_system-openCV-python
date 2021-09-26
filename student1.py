from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1250x650+0+0")
        self.root.title("Face Recognition System")

        #=========variables============
        self.var_Dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_sem = StringVar()
        self.var_id = StringVar()
        self.var_name = StringVar()
        self.var_sec = StringVar()
        self.var_roll = StringVar()
        self.var_gen = StringVar()
        self.var_dob = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_email = StringVar()
        self.var_teacher = StringVar()


        # first image
        img1 = Image.open(r"C:\Users\HP\Desktop\face recognition system\images\9.jpg")
        img1 = img1.resize((500, 130), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lb = Label(self.root, image=self.photoimg1)
        f_lb.place(x=0, y=0, width=500, height=130)

        # second image
        img2 = Image.open(r"C:\Users\HP\Desktop\face recognition system\images\23.jpg")
        img2 = img2.resize((500, 130), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lb = Label(self.root, image=self.photoimg2)
        f_lb.place(x=500, y=0, width=500, height=130)

        # third image
        img3 = Image.open(r"C:\Users\HP\Desktop\face recognition system\images\21.jpg")
        img3 = img3.resize((500, 130), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        f_lb = Label(self.root, image=self.photoimg3)
        f_lb.place(x=1000, y=0, width=350, height=130)

        # background image
        img4 = Image.open(r"C:\Users\HP\Desktop\face recognition system\images\10.jpg")
        img4 = img4.resize((1300, 520), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img = Label(self.root, image=self.photoimg4, cursor="hand2")
        bg_img.place(x=0, y=130, width=1300, height=520)

        title_lbl = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM",font=("time new roman", 30, "bold"), bg="yellow", fg="red")
        title_lbl.place(x=0, y=0, width=1300, height=45)

        #MAIN frame
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=5,y=55,width=1240,height=480)

        #left side lebel frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=600,height=470)

        img_left = Image.open(r"C:\Users\HP\Desktop\face recognition system\images\24.jpg")
        img_left = img_left.resize((590, 80), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        f_lb = Label(Left_frame, image=self.photoimg_left)
        f_lb.place(x=5, y=0, width=590, height=80)

        #current course information
        curr_course_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Student Details",font=("times new roman", 12, "bold"))
        curr_course_frame.place(x=5, y=85, width=585, height=85)

        #department
        dep_label=Label(curr_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=5,sticky=W)

        dep_combo=ttk.Combobox(curr_course_frame,textvariable=self.var_Dep,font=("times new roman",10,"bold"),width=17,state="readonly")
        dep_combo["values"]=("Select Department","CSE","CS-IT","EE","EC","Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=10,sticky=W)

        #course
        course_label = Label(curr_course_frame, text="Course", font=("times new roman", 12, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=25,sticky=W)

        course_combo = ttk.Combobox(curr_course_frame,textvariable=self.var_course, font=("times new roman", 10, "bold"), width=20, state="readonly")
        course_combo["values"] = ("Select Course", "B-Tech", "M-Tech")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, sticky=W)

        #year
        year_label = Label(curr_course_frame, text="Year", font=("times new roman", 12, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=5, sticky=W)

        year_combo = ttk.Combobox(curr_course_frame, textvariable=self.var_year,font=("times new roman", 10, "bold"), width=17, state="readonly")
        year_combo["values"] = ("Select year", "1st", "2nd", "3rd", "4th")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=10,pady=10, sticky=W)

        #semester
        sem_label = Label(curr_course_frame,text="Semester", font=("times new roman", 12, "bold"), bg="white")
        sem_label.grid(row=1, column=2, padx=25, sticky=W)

        sem_combo = ttk.Combobox(curr_course_frame,textvariable=self.var_sem, font=("times new roman", 10, "bold"), width=20, state="readonly")
        sem_combo["values"] = ("Select Semester", "Semester-1", "Semester-2", "Semester-3", "Semester-4","Semester-5","Semester-6","Semester-7","Semester-8")
        sem_combo.current(0)
        sem_combo.grid(row=1, column=3, padx=2, sticky=W)

        # class student information
        class_student_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Class Student Details",font=("times new roman", 12, "bold"))
        class_student_frame.place(x=5, y=170, width=585, height=260)

        #studet id
        studentId_label = Label(class_student_frame, text="StudentID:", font=("times new roman", 12, "bold"), bg="white")
        studentId_label.grid(row=0, column=0, padx=2, sticky=W)

        studentId_entry=ttk.Entry(class_student_frame,textvariable=self.var_id,width=17,font=("times new roman", 12, "bold"))
        studentId_entry.grid(row=0,column=1,padx=10, sticky=W)

        # studet name
        studentName_label = Label(class_student_frame, text="Student Name:", font=("times new roman", 12, "bold"),bg="white")
        studentName_label.grid(row=0, column=2, padx=10, sticky=W)

        studentName_entry = ttk.Entry(class_student_frame,textvariable=self.var_name, width=17, font=("times new roman", 12, "bold"))
        studentName_entry.grid(row=0, column=3, padx=5, sticky=W)

        # section division
        section_label = Label(class_student_frame, text="Section:", font=("times new roman", 12, "bold"),bg="white")
        section_label.grid(row=1, column=0, padx=2,pady=10, sticky=W)

        section_entry = ttk.Entry(class_student_frame,textvariable=self.var_sec, width=17, font=("times new roman", 12, "bold"))
        section_entry.grid(row=1, column=1, padx=10,pady=10, sticky=W)

        # Roll Number
        roll_label = Label(class_student_frame, text="Roll No.:", font=("times new roman", 12, "bold"), bg="white")
        roll_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        roll_entry = ttk.Entry(class_student_frame, textvariable=self.var_roll,width=17, font=("times new roman", 12, "bold"))
        roll_entry.grid(row=1, column=3, padx=5, pady=5, sticky=W)

        # Gender
        gender_label = Label(class_student_frame, text="Gender:", font=("times new roman", 12, "bold"), bg="white")
        gender_label.grid(row=2, column=0, padx=2, pady=5, sticky=W)


        gender_combo = ttk.Combobox(class_student_frame, textvariable=self.var_gen, font=("times new roman", 10, "bold"),width=17, state="readonly")
        gender_combo["values"] = ("M", "F", "Others")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10, pady=5, sticky=W)


        # Date of bdob
        dob_label = Label(class_student_frame,text="DOB:", font=("times new roman", 12, "bold"), bg="white")
        dob_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        dob_entry = ttk.Entry(class_student_frame,textvariable=self.var_dob , width=17, font=("times new roman", 12, "bold"))
        dob_entry.grid(row=2, column=3, padx=5, pady=5, sticky=W)

        # Phone number
        phone_label = Label(class_student_frame, text="Mobile No.:", font=("times new roman", 12, "bold"), bg="white")
        phone_label.grid(row=3, column=0, padx=2, pady=5, sticky=W)

        phone_entry = ttk.Entry(class_student_frame,textvariable=self.var_phone, width=17, font=("times new roman", 12, "bold"))
        phone_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # Address
        address_label = Label(class_student_frame, text="Address:", font=("times new roman", 12, "bold"), bg="white")
        address_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        address_entry = ttk.Entry(class_student_frame,textvariable=self.var_address, width=17, font=("times new roman", 12, "bold"))
        address_entry.grid(row=3, column=3, padx=5, pady=5, sticky=W)

        # Email
        email_label = Label(class_student_frame, text="Email.:", font=("times new roman", 12, "bold"), bg="white")
        email_label.grid(row=4, column=0, padx=2, pady=5, sticky=W)

        email_entry = ttk.Entry(class_student_frame,textvariable=self.var_email, width=17, font=("times new roman", 12, "bold"))
        email_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        # class teacher
        teacher_label = Label(class_student_frame, text="Teacher Name:", font=("times new roman", 12, "bold"), bg="white")
        teacher_label.grid(row=4, column=2, padx=10, pady=5, sticky=W)

        teacher_entry = ttk.Entry(class_student_frame,textvariable=self.var_teacher, width=17, font=("times new roman", 12, "bold"))
        teacher_entry.grid(row=4, column=3, padx=5, pady=5, sticky=W)


        #radio buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame, variable=self.var_radio1,text="Take photo sample",value="Yes")
        radiobtn1.grid(row=5,column=0)


        radiobtn2 = ttk.Radiobutton(class_student_frame, variable=self.var_radio1,text="No photo sample", value="No")
        radiobtn2.grid(row=5, column=1)

        #bbuttons frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=578,height=35)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=5,font=("times new roman", 11, "bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        Update_btn = Button(btn_frame, text="Update",command=self.update_data,width=5, font=("times new roman", 11, "bold"), bg="blue",fg="white")
        Update_btn.grid(row=0, column=1, padx=10)

        delete_btn = Button(btn_frame, text="Delete",command=self.delete_data, width=5, font=("times new roman", 11, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2,padx=10)



        Reset_btn = Button(btn_frame, text="Reset",command=self.reset_data, width=5, font=("times new roman", 11, "bold"), bg="blue", fg="white")
        Reset_btn.grid(row=0, column=3,padx=10)

        takephoto_btn = Button(btn_frame,command=self.generate_dataset, text="Take Photo Sample", width=15, font=("times new roman", 11, "bold"), bg="blue",fg="white")
        takephoto_btn.grid(row=0, column=4, padx=2)

        updatephoto_btn = Button(btn_frame, text="Update Photo Sample", width=15, font=("times new roman", 11, "bold"), bg="blue",fg="white")
        updatephoto_btn.grid(row=0, column=5, padx=2)

        # right side lebel frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details",font=("times new roman", 12, "bold"))
        Right_frame.place(x=630, y=10, width=600, height=470)

        img_right = Image.open(r"C:\Users\HP\Desktop\face recognition system\images\25.jpg")
        img_right = img_right.resize((590, 80), Image.ANTIALIAS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        f_lb = Label(Right_frame, image=self.photoimg_right)
        f_lb.place(x=5, y=0, width=590, height=80)

        #..........Searching System............
        search_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE, text="Search System",font=("times new roman", 12, "bold"))
        search_frame.place(x=5, y=85, width=590, height=50)

        search_label_label = Label(search_frame, text="Search By", font=("times new roman", 12, "bold"),bg="blue",fg="white")
        search_label_label.grid(row=0, column=0, padx=5, sticky=W)

        search_combo = ttk.Combobox(search_frame, font=("times new roman", 10, "bold"), width=15, state="readonly")
        search_combo["values"] = ("Select", "Enrolment Number", "Name")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, sticky=W)

        search_entry = ttk.Entry(search_frame, width=20, font=("times new roman", 11, "bold"))
        search_entry.grid(row=0, column=2, padx=5, sticky=W)

        search_btn = Button(search_frame, text="Search", width=10, font=("times new roman", 10, "bold"), bg="blue",fg="white")
        search_btn.grid(row=0, column=3, padx=5, sticky=W)

        showAll_btn = Button(search_frame, text="Show All", width=10, font=("times new roman", 10, "bold"), bg="blue",fg="white")
        showAll_btn.grid(row=0, column=4, padx=5, sticky=W)

        #==============table frame ===============
        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=140, width=590, height=290)

        scroll_x= ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y= ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame,column=("Dep","Course","year","sem","id","name","sec","roll","gen","dob","phone","address","email","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Dep", text="Department")
        self.student_table.heading("Course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="StudentId")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("sec", text="Section")
        self.student_table.heading("roll", text="Roll No.")
        self.student_table.heading("gen", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="PhotoSampleStatus")
        self.student_table["show"] = "headings"

        self.student_table.column("Dep", width=100)
        self.student_table.column("Course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("sec", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gen", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=100)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()



    def add_data(self):


        if self.var_Dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)

        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                             self.var_Dep.get(),
                                                                                                             self.var_course.get(),
                                                                                                             self.var_year.get(),
                                                                                                             self.var_sem.get(),
                                                                                                             self.var_id.get(),
                                                                                                             self.var_name.get(),
                                                                                                             self.var_sec.get(),
                                                                                                             self.var_roll.get(),
                                                                                                             self.var_gen.get(),
                                                                                                             self.var_dob.get(),
                                                                                                             self.var_phone.get(),
                                                                                                             self.var_address.get(),
                                                                                                             self.var_email.get(),
                                                                                                             self.var_teacher.get(),
                                                                                                             self.var_radio1.get()
                                                                                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)


    # ========fetch data ==============
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="face_recognizer")
        my_cursor = conn.cursor()

        my_cursor.execute("select * from student1")
        data=my_cursor.fetchall()


        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()


    # ======= get cursor==================
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_Dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_id.set(data[4]),
        self.var_name.set(data[5]),
        self.var_sec.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gen.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_phone.set(data[10]),
        self.var_address.set(data[11]),
        self.var_email.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

    #=====update==========
    def update_data(self):
        if self.var_Dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)

        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)

                if Update>0:

                    conn = mysql.connector.connect(host="localhost", username="root", password="1234",database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student1 set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Section=%s,Roll=%s,Gender=%s,DOB=%s,Phone=%s,Address=%s,Email=%s,Teacher=%s,PhotoSample=%s where StudentId=%s",(
                                                                                                                                                                                                                                     self.var_Dep.get(),
                                                                                                                                                                                                                                     self.var_course.get(),
                                                                                                                                                                                                                                     self.var_year.get(),
                                                                                                                                                                                                                                     self.var_sem.get(),
                                                                                                                                                                                                                                     self.var_name.get(),
                                                                                                                                                                                                                                     self.var_sec.get(),
                                                                                                                                                                                                                                     self.var_roll.get(),
                                                                                                                                                                                                                                     self.var_gen.get(),
                                                                                                                                                                                                                                     self.var_dob.get(),
                                                                                                                                                                                                                                     self.var_phone.get(),
                                                                                                                                                                                                                                     self.var_address.get(),
                                                                                                                                                                                                                                     self.var_email.get(),
                                                                                                                                                                                                                                     self.var_teacher.get(),
                                                                                                                                                                                                                                     self.var_radio1.get(),
                                                                                                                                                                                                                                     self.var_id.get()
                                                                                                                                                                                                                                ))

                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Updated Successfully",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
    #========delete Function==========
    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","Student Id required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete student details","Do you want to delete this Student details",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="1234",database="face_recognizer")
                    my_cursor = conn.cursor()
                    sql="delete from student1 where StudentId=%s"
                    val=(self.var_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Student details deleted successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    #=====reset data========
    def reset_data(self):
        self.var_Dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select year")
        self.var_sem.set("Select Semester")
        self.var_id.set("")
        self.var_name.set("")
        self.var_sec.set("")
        self.var_roll.set("")
        self.var_gen.set("M")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_email.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")


    #=========== Generate data or Take photo Samples =============
    def generate_dataset(self):
        if self.var_Dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)

        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="1234",database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student1")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student1 set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Section=%s,Roll=%s,Gender=%s,DOB=%s,Phone=%s,Address=%s,Email=%s,Teacher=%s,PhotoSample=%s where StudentId=%s",(
                                                                                                                                                                                                                    self.var_Dep.get(),
                                                                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                                                                    self.var_sem.get(),
                                                                                                                                                                                                                    self.var_name.get(),
                                                                                                                                                                                                                    self.var_sec.get(),
                                                                                                                                                                                                                    self.var_roll.get(),
                                                                                                                                                                                                                    self.var_gen.get(),
                                                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                                                    self.var_phone.get(),
                                                                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                                                    self.var_teacher.get(),
                                                                                                                                                                                                                    self.var_radio1.get(),
                                                                                                                                                                                                                    self.var_id.get()==id+1
                                                                                                                                                                                                                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                #===============Load predefined data on face frontals from opencv============
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3
                    #minimum Neighbour=5

                    for (x,y,w,h) in  faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed!!!")
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    #.........


if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
