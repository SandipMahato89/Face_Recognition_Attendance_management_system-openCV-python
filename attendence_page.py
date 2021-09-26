from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog


mydata=[]
class Attendence:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1250x650+0+0")
        self.root.title("Face Recognition System")

        #========variables===================
        self.var_stud_id=StringVar()
        self.var_stud_name = StringVar()
        self.var_stud_roll = StringVar()
        self.var_stud_sec = StringVar()
        self.var_stud_dep = StringVar()
        self.var_stud_time = StringVar()
        self.var_stud_date = StringVar()
        self.var_stud_attend = StringVar()

        # first image
        img1 = Image.open(r"C:\Users\HP\Desktop\face recognition system\images\34.jpg")
        img1 = img1.resize((625, 130), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lb = Label(self.root, image=self.photoimg1)
        f_lb.place(x=0, y=0, width=625, height=130)

        # second image
        img2 = Image.open(r"C:\Users\HP\Desktop\face recognition system\images\23.jpg")
        img2 = img2.resize((625, 130), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lb = Label(self.root, image=self.photoimg2)
        f_lb.place(x=625, y=0, width=625, height=130)

        img4 = Image.open(r"C:\Users\HP\Desktop\face recognition system\images\10.jpg")
        img4 = img4.resize((1300, 520), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img = Label(self.root, image=self.photoimg4, cursor="hand2")
        bg_img.place(x=0, y=130, width=1300, height=520)

        title_lbl = Label(bg_img, text="ATTENDANCE MANAGEMENT SYSTEM", font=("time new roman", 30, "bold"), bg="yellow",fg="red")
        title_lbl.place(x=0, y=0, width=1300, height=45)

        # MAIN frame
        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=5, y=55, width=1240, height=480)

        # left side lebel frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Attendance Details",font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=600, height=470)

        img_left = Image.open(r"C:\Users\HP\Desktop\face recognition system\images\24.jpg")
        img_left = img_left.resize((590, 80), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        f_lb = Label(Left_frame, image=self.photoimg_left)
        f_lb.place(x=5, y=0, width=590, height=80)

        leftInside_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE)
        leftInside_frame.place(x=10, y=90, width=580, height=450)

        #labels and entry

        # attendance id
        studentId_label = Label(leftInside_frame, text="StudentID:", font=("times new roman", 12, "bold"),bg="white")
        studentId_label.grid(row=0, column=0, padx=2,pady=5 ,sticky=W)

        studentId_entry = ttk.Entry(leftInside_frame,textvariable=self.var_stud_id, width=17,font=("times new roman", 12, "bold"))
        studentId_entry.grid(row=0, column=1, padx=10, sticky=W)

        # studet name
        studentName_label = Label(leftInside_frame, text="Student Name:", font=("times new roman", 12, "bold"),bg="white")
        studentName_label.grid(row=0, column=2, padx=10,pady=5, sticky=W)

        studentName_entry = ttk.Entry(leftInside_frame,textvariable=self.var_stud_name,  width=17,font=("times new roman", 12, "bold"))
        studentName_entry.grid(row=0, column=3, padx=10, sticky=W)

        # Roll Number
        roll_label = Label(leftInside_frame, text="Roll No.:", font=("times new roman", 12, "bold"), bg="white")
        roll_label.grid(row=1, column=0, padx=2, pady=10, sticky=W)

        roll_entry = ttk.Entry(leftInside_frame, textvariable=self.var_stud_roll, width=17,font=("times new roman", 12, "bold"))
        roll_entry.grid(row=1, column=1, padx=10, pady=10, sticky=W)

        # section division
        section_label = Label(leftInside_frame, text="Section:", font=("times new roman", 12, "bold"), bg="white")
        section_label.grid(row=1, column=2, padx=10, pady=10, sticky=W)

        section_entry = ttk.Entry(leftInside_frame, textvariable=self.var_stud_sec, width=17,font=("times new roman", 12, "bold"))
        section_entry.grid(row=1, column=3, padx=10, pady=10, sticky=W)

        # department
        dep_label = Label(leftInside_frame,text="Department", font=("times new roman", 12, "bold"), bg="white")
        dep_label.grid(row=2, column=0, padx=2,pady=10, sticky=W)

        dep_stat=ttk.Entry(leftInside_frame, textvariable=self.var_stud_dep, width=17,font=("times new roman", 12, "bold"))
        dep_stat.grid(row=2, column=1, padx=10,pady=10, sticky=W)

        # Time
        time=Label(leftInside_frame, text="Time", font=("times new roman", 12, "bold"), bg="white")
        time.grid(row=2, column=2, padx=10,pady=10, sticky=W)

        time_entry = ttk.Entry(leftInside_frame, textvariable=self.var_stud_time,width=17, font=("times new roman", 12, "bold"))
        time_entry.grid(row=2, column=3, padx=10, pady=10, sticky=W)

        # Date
        date = Label(leftInside_frame, text="Date", font=("times new roman", 12, "bold"), bg="white")
        date.grid(row=3, column=0, padx=10, pady=10, sticky=W)

        date_entry = ttk.Entry(leftInside_frame,textvariable=self.var_stud_date, width=17, font=("times new roman", 12, "bold"))
        date_entry.grid(row=3, column=1, padx=10, pady=10, sticky=W)

        # Status
        stat_label = Label(leftInside_frame, text="Attendance status", font=("times new roman", 12, "bold"), bg="white")
        stat_label.grid(row=3, column=2, padx=10, pady=10, sticky=W)

        stat_entry = ttk.Entry(leftInside_frame, textvariable=self.var_stud_attend, width=17,font=("times new roman", 12, "bold"))
        stat_entry.grid(row=3, column=3, padx=10, pady=10, sticky=W)

        #Buttons
        btn_frame = Frame(leftInside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=280, width=575, height=35)

        save_btn = Button(btn_frame, text="Import CSV",command=self.importCsv, width=13, font=("times new roman", 11, "bold"),bg="blue", fg="white")
        save_btn.grid(row=0, column=0,padx=5)

        Update_btn = Button(btn_frame, text="Export CSV",command=self.exportCsv, width=13,font=("times new roman", 11, "bold"), bg="blue", fg="white")
        Update_btn.grid(row=0, column=1, padx=10)

        delete_btn = Button(btn_frame, text="Update", width=13,font=("times new roman", 11, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2, padx=10)

        Reset_btn = Button(btn_frame, command=self.reset_data,text="Reset",  width=13,font=("times new roman", 11, "bold"), bg="blue", fg="white")
        Reset_btn.grid(row=0, column=3, padx=10)



        # right side lebel frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance Details",font=("times new roman", 12, "bold"))
        Right_frame.place(x=630, y=10, width=600, height=470)

        # ==============table frame ===============
        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=1, width=590, height=420)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, column=("id","name","roll","sec","department","date","time","attendance"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("id", text="StudentId")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("roll", text="Roll No.")
        self.student_table.heading("sec", text="Section")
        self.student_table.heading("department", text="Department")
        self.student_table.heading("date", text="Date")
        self.student_table.heading("time", text="Time")
        self.student_table.heading("attendance", text="Attendance")


        self.student_table["show"]="headings"

        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("sec", width=100)
        self.student_table.column("department", width=100)
        self.student_table.column("date", width=100)
        self.student_table.column("time", width=100)
        self.student_table.column("attendance", width=100)

        self.student_table.pack(fill=BOTH, expand=1)

        self.student_table.bind("<ButtonRelease>",self.get_cursor)

    #=======================fetch data================

    def fetchData(self,rows):
        self.student_table.delete(*self.student_table.get_children())
        for i in rows:
            self.student_table.insert("",END,values=i)

    #import CSV
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myFile:
            csvread=csv.reader(myFile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)


    #export CSV
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data Found to Export",parent=self.root)
                return False

            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV",filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data Exported to "+os.path.basename(fln)+" successfully...")
        except Exception as es:
            messagebox.showerror("Error", f"Due To :{str(es)}", parent=self.root)
    def get_cursor(self,event=""):
        cursor_row=self.student_table.focus()
        content=self.student_table.item(cursor_row)
        rows=content['values']
        self.var_stud_id.set(rows[0])
        self.var_stud_name.set(rows[1])
        self.var_stud_roll.set(rows[2])
        self.var_stud_sec.set(rows[3])
        self.var_stud_dep.set(rows[4])
        self.var_stud_time.set(rows[5])
        self.var_stud_date.set(rows[6])
        self.var_stud_attend.set(rows[7])

    #========reset button=========
    def reset_data(self):
        self.var_stud_id.set("")
        self.var_stud_name.set("")
        self.var_stud_roll.set("")
        self.var_stud_sec.set("")
        self.var_stud_dep.set("")
        self.var_stud_time.set("")
        self.var_stud_date.set("")
        self.var_stud_attend.set("")

        







if __name__ == "__main__":
    root=Tk()
    obj=Attendence(root)
    root.mainloop()