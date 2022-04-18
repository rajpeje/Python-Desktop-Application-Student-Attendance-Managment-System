from tkinter import *
from tkcalendar import *
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from datetime import date,datetime
import tkinter.messagebox as tm
import re
import sqlite3



def main():
    global window1
    window1=Tk()#TKINTER WINDOW

    window1.geometry('1350x730')
    window1.title("Student Attendance Management System")
    window1.resizable(False,False)

    img = PhotoImage(file="login0.png")
    label = Label(window1,image=img,height=730,width=1366)
    label.place(x=0,y=0)

    char='DESKTOP APPLICATION STUDENT ATTENDANCE MANAGEMENT SYSTEM'
    title_label=Label(window1,text='',font=("Cosmic Sans MS",18,"bold"),height=3,width=150,fg='black')
    title_label.place(x=0,y=50)
    title_label=Label(window1,text=char,font=("Cosmic Sans MS",18,"bold"),fg='black')
    title_label.place(x=250,y=80)
    
    admin_button= Button(window1,text='Admin',font=("bold",18),width=15,bg='black',fg='yellow',command=adminlogin)                        
    admin_button.place(x=560,y=350)

    teach_button= Button(window1,text='Teacher',font=("bold",18),width=15,bg='black',fg='yellow',command=teacherlogin)
    teach_button.place(x=560,y=430)

    window1.mainloop()

 
def adminlogin():

    try:
        window3.destroy()
        adminlogin()               
    except:
        try:
            window1.destroy()
            adminlogin()
        except:
            global window2
            window2=Tk()#TKINTER WINDOW
            window2.configure(background="lightblue")#WINDOW BACKGROUND

            window2.geometry('1350x730')
            window2.title("ADMIN LOGIN")
            window2.resizable(False,False)
            
            global uname
            global passw
            global uname_entry
            global pass_entry
            uname = StringVar()
            passw = StringVar()

            teacher_label=Label(window2,anchor=W,text='',font=("bold",13),height=2,width=150,fg='black')
            teacher_label.place(x=0,y=50)

            logout_button= Button(window2,text='HOME',font=("Cosmic Sans MS",15,"bold"),bd=0,height=1,fg='brown',command=close1)                       
            logout_button.place(x=5,y=55)

            uname_label=Label(window2,text="Username",font=("bold",13),fg='blue',bg='lightblue')
            uname_label.place(x=640,y=270)
            uname_entry=Entry(window2,width=20,font=("bold",15),textvariable=uname,bg='pink')
            uname_entry.place(x=570,y=295)

            pass_label=Label(window2,text="Password",font=("bold",13),fg='blue',bg='lightblue')
            pass_label.place(x=640,y=340)
            pass_entry=Entry(window2,width=20,font=("bold",15),textvariable=passw,bg='pink',show='*')
            pass_entry.place(x=570,y=365)

            login_button= Button(window2,text='LOG IN',font=("bold",15),width=15,bg='black',fg='yellow',command=verify1)                        
            login_button.place(x=599,y=425)

def close1():
    window2.destroy()
    main()


def teacherlogin():
    try:
        window5.destroy()
        teacherlogin()
    except:
        try:
            window1.destroy()
            teacherlogin()
        except:    
                
            global window4
            window4=Tk()#TKINTER WINDOW
            window4.configure(background="lightblue")#WINDOW BACKGROUND

            window4.geometry('1350x730')
            window4.title("TEACHER LOGIN")
            window4.resizable(False,False)

            global uname
            global passw
            global uname_entry
            global pass_entry
            uname = StringVar()
            passw = StringVar()

            teacher_label=Label(window4,anchor=W,text='',font=("bold",13),height=2,width=150,fg='black')
            teacher_label.place(x=0,y=50)

            logout_button= Button(window4,text='HOME',font=("Cosmic Sans MS",15,"bold"),bd=0,height=1,fg='brown',command=close2)                       
            logout_button.place(x=5,y=55)
                
            uname_label=Label(window4,text="Username",font=("bold",13),fg='blue',bg='lightblue')
            uname_label.place(x=640,y=270)
            uname_entry=Entry(window4,width=20,font=("bold",15),textvariable=uname,bg='pink')
            uname_entry.place(x=570,y=295)

            pass_label=Label(window4,text="Password",font=("bold",13),fg='blue',bg='lightblue')
            pass_label.place(x=640,y=340)
            pass_entry=Entry(window4,width=20,font=("bold",15),textvariable=passw,bg='pink',show='*')
            pass_entry.place(x=570,y=365)

            login_button= Button(window4,text='LOG IN',font=("bold",15),width=15,bg='black',fg='yellow',command=verify2)                        
            login_button.place(x=599,y=425)

def close2():
    window4.destroy()
    main()

            
 
def verify1():
    user = uname.get()
    pin = passw.get()
    uname_entry.delete(0,"end")
    pass_entry.delete(0,"end")

    if user == 'admin' and pin == 'admin123' :
        success = tm.showinfo("Login Success","You Have Successfully Logged In!\n               Welcome.")
        if success:
            window2.destroy()
            admin()
    else:
        tm.showinfo("Login Failed","Your Username or Password is Incorrect!\n             Please Try Again.")
        
def verify2():
    base=sqlite3.connect('AttendanceManagement_temp.db')
    with base:
        c=base.cursor()
                            
    try:
        user = uname.get()
        pin = passw.get()
        uname_entry.delete(0,"end")
        pass_entry.delete(0,"end")

        c.execute("SELECT Count(*) FROM AM_Teachers WHERE teacher = '"+user+"' AND password = '"+pin+"'")
        row=c.fetchall()

        for x in row:        
            if x[0] == 1:
                success = tm.showinfo("Login Success","You Have Successfully Logged In!\n               Welcome.")
                if success:
                    global temp
                    temp = user
                    window4.destroy()
                    teacher()
                    
            else:
                tm.showinfo("Login Failed","Your Username or Password is Incorrect!\n             Please Try Again.")
    except:
        tm.showinfo("Login Failed","Your Username or Password is Incorrect!\n             Please Try Again.")
    
         

         
def admin():
    try:
        window9.destroy()
        admin()
        
    except:
                
        global window3
        global justice
        justice = 'true'
        window3=Tk() #TKINTER WINDOW

        window3.geometry('1350x730')
        window3.title("Admin")
        window3.resizable(False,False)

        img = PhotoImage(file="login2.png")
        label = Label(window3,image=img,height=730,width=1366)
        label.place(x=0,y=0)

        text1='  ADMIN'
        course_label=Label(window3,anchor=W,text=text1,font=("Cosmic Sans MS",13,"bold"),height=2,width=150,fg='black')
        course_label.place(x=0,y=50)

        logout_button= Button(window3,text='logout',font=("bold",18),bd=0,height=1,fg='gray',command=adminlogin)                       
        logout_button.place(x=1250,y=50)


        teacher_button= Button(window3,text='Add Teacher',font=("bold",18),width=20,bg='black',fg='yellow',command=addteacher)                       
        teacher_button.place(x=540,y=200)

        class_button= Button(window3,text='Add Class',font=("bold",18),width=20,bg='black',fg='yellow',command=addclass_admin)                       
        class_button.place(x=540,y=280)

        stu_button= Button(window3,text='Add Student',font=("bold",18),width=20,bg='black',fg='yellow',command=addstudent_var)
        stu_button.place(x=540,y=360)

        att_button= Button(window3,text='Report Of Attendance',font=("bold",18),width=20,bg='black',fg='yellow',command=report_var)                        
        att_button.place(x=540,y=440)

        window3.mainloop()

def report_var():
    global adminR
    adminR = 'T'
    global version
    version = 'False'
    addstudent()
    
    
def addclass_admin():
    global justice
    justice = 'true'
    window3.destroy()
    addclass()
    

def addteacher():
    try:
        window10.destroy()
        addteacher()
    except:
        try:
            window3.destroy()
            addteacher()
        except:
            global window9
            window9=Tk()#TKINTER WINDOW
            window9.configure(background="lightblue")#WINDOW BACKGROUND

            window9.geometry('1350x730')
            window9.title("ADD TEACHER")
            window9.resizable(False,False)
            

            global tech
            global teacher_entry
            global passw1
            global password_entry
            global conf
            global confirm_entry
            
            tech = StringVar()
            passw1 = StringVar()
            conf = StringVar()
            text1='ADD TEACHER  |                            |'
            teacher_label=Label(window9,anchor=W,text=text1,font=("Cosmic Sans MS",13,"bold"),height=2,width=150,fg='black')
            teacher_label.place(x=0,y=50)
            
            view_button= Button(window9,text='View Teachers',font=("bold",13),bd=0,height=1,fg='black',command=view_teachers)                       
            view_button.place(x=148,y=56)
        
            back_button= Button(window9,text='Exit',font=("bold",18),bd=0,height=1,fg='gray',command=admin)                       
            back_button.place(x=1250,y=50)

            
            teacher_label=Label(window9,text="Teacher Name :",font=("bold",14),fg='gray',bg='lightblue')
            teacher_label.place(x=470,y=240)
            teacher_entry=Entry(window9,width=20,font=("bold",15),textvariable=tech,bg='pink')
            teacher_entry.place(x=630,y=240)
            
            password_label=Label(window9,text="Password :",font=("bold",14),fg='gray',bg='lightblue')
            password_label.place(x=470,y=310)
            password_entry=Entry(window9,width=20,font=("bold",15),textvariable=passw1,bg='pink',show='*')
            password_entry.place(x=630,y=310)

            confirm_label=Label(window9,text="Confirm Password :",font=("bold",13),fg='gray',bg='lightblue')
            confirm_label.place(x=470,y=380)
            confirm_entry=Entry(window9,width=20,font=("bold",15),textvariable=conf,bg='pink',show='*')
            confirm_entry.place(x=630,y=380)

            addteacher_button= Button(window9,text='Add Teacher',font=("bold",15),width=15,bg='black',fg='yellow',command=addteacher_verify)                        
            addteacher_button.place(x=670,y=500)

            window9.mainloop()

def addteacher_verify():
    teach1 = tech.get()
    passw2 = passw1.get()
    conf1 = conf.get()

    reg = '[`+@_!;,."#$%^&*()-<>=?/\|}{~:]'
    pat = re.compile(reg)              
    mat = re.search(pat,teach1)

    if teach1 == '':
        tm.showinfo("ADD TEACHER","Teacher Name Should Not Be Empty!\nPlease Provide Teacher Name")
        teacher_entry.delete(0,"end")       
    elif mat:
        tm.showinfo("ADD TEACHER","Don't Use Any Special Characters in Teacher Name!\n               eg:Raj Peje")
        teacher_entry.delete(0,"end")
                    
    elif passw2 == "":
        tm.showinfo("ADD TEACHER","Password Should Not Be Empty!\nPlease Provide Password")
        confirm_entry.delete(0,"end") 
    else:            
        if passw2 == conf1 :
            teacher_entry.delete(0,"end")
            password_entry.delete(0,"end")
            confirm_entry.delete(0,"end")
            
            base=sqlite3.connect('AttendanceManagement_temp.db')
            with base:
                c=base.cursor()

            c.execute('CREATE TABLE IF NOT EXISTS AM_Teachers (Teacher TEXT,Password TEXT)')
            c.execute("select teacher from AM_Teachers")
            result=c.fetchall()
            teachers=[]
            for i in result:
                teachers.append(i[0])

            if teach1 in teachers:
                tm.showinfo("ADD TEACHER","'"+teach1+"' Teacher Is Already Existed!\n                  Thank You.")
            else:
                c.execute("INSERT INTO AM_Teachers(Teacher,Password) VALUES(?,?)",(teach1,passw2,))
                base.commit()
                tm.showinfo("ADD TEACHER","New Teacher Has Been Added Succesfully!\n                  Thank You.")
                    
        else:
            tm.showinfo("ADD TEACHER","Confirm Password Does Not Match!\n note: Password And Confirm Password Should Be Same" )
        

def view_teachers():
  
    window9.destroy()
    global window10
    window10=Tk()#TKINTER WINDOW
    window10.configure(background="lightblue")#WINDOW BACKGROUND

    window10.geometry('1350x730')
    window10.title("VIEW TEACHERS")
    window10.resizable(False,False)

    course_label=Label(window10,anchor=W,text='View Teachers',font=("Cosmic Sans MS",13,"bold"),height=2,width=150,fg='black')
    course_label.place(x=0,y=50)

    exit_button= Button(window10,text='Exit',font=("bold",18),bd=0,height=1,fg='gray',command=addteacher)                       
    exit_button.place(x=1250,y=50)


    frame = Frame(window10)
    frame.place(x=0,y=100)

    scrollbar = Scrollbar(frame)
    scrollbar.pack( side = RIGHT, fill = Y )

    style = ttk.Style()
    style.theme_use('winnative')

    tree = ttk.Treeview(frame,column=('1','2')  ,show='headings' ,height=28, yscrollcommand = scrollbar.set)
    tree.column("# 1", anchor=CENTER,width=440)
    tree.heading("# 1", text="Teacher")
    tree.column("# 2", anchor=CENTER,width=440)
    tree.heading("# 2", text="Password")
    try:
        base=sqlite3.connect('AttendanceManagement_temp.db')
        with base:
            c=base.cursor()
        
        query="select teacher from AM_Teachers"
        c.execute(query)
        result=c.fetchall()
        zora=[]
        for i in result:
            zora.append(i[0])
            
        query1="select password from AM_Teachers"
        c.execute(query1)
        result1=c.fetchall()
        zora1=[]
        for z in result1:
            zora1.append(z[0])
                    
        for t in range(len(zora)):
            tree.insert('', 'end', text="1", values=(zora[t],zora1[t]))

        tree.pack()
        scrollbar.config( command = tree.yview)
    except:
        tm.showinfo('Teachers','Teachers Dont Exist. Enter Atleast One Teacher')
        





def teacher():
    global justice
    justice='false'
    global close
    close = 'F'
    
    global window5
    
    window5=Tk()#TKINTER WINDOW
##    window5.configure(background="lightblue")#WINDOW BACKGROUND
    window5.geometry('1350x730')
    window5.title("Teacher")
    window5.resizable(False,False)

    img = PhotoImage(file="login1.png")
    label = Label(window5,image=img,height=730,width=1366)
    label.place(x=0,y=0)
    

    text1 = "   "+temp
    teacher_label=Label(window5,anchor=W,text=text1,font=("Cosmic Sans MS",14,"bold"),height=2,width=150,fg='black')
    teacher_label.place(x=0,y=50)

    logout_button= Button(window5,text='logout',font=("bold",18),bd=0,height=1,fg='gray',command=teacherlogin)                       
    logout_button.place(x=1250,y=50)


    class_button= Button(window5,text='Add Class',font=("bold",18),width=20,bg='black',fg='yellow',command=addclass)                        
    class_button.place(x=510,y=250)

    stu_button= Button(window5,text='Add Student',font=("bold",18),width=20,bg='black',fg='yellow',command=addstudent_var)
    stu_button.place(x=510,y=330)

    att_button= Button(window5,text='Take Attendance',font=("bold",18),width=20,bg='black',fg='yellow',command=changeclass)                        
    att_button.place(x=510,y=410)

    report_button= Button(window5,text='Attendance Report',font=("bold",18),width=20,bg='black',fg='yellow',command=report_var)                        
    report_button.place(x=510,y=490)

    window5.mainloop()


def addstudent_var():
    global version
    version = 'False'
    global adminR
    adminR = 'F'
##    add_password1()
    addstudent()
    

def register_class():
    course1=course.get()
    year1=year.get()
    class1=course1+'_'+year1
    string="\\"
    rep=repr(string)

    reg = '[-"@_!#$%^&*().+=<\[>?/|}{~`:\[\]\']'
    pat = re.compile(reg)              
    mat = re.search(pat,course1)

    if course1 == '':
        tm.showinfo("Course","Course Should Not Be Empty!\nPlease Provide Course Name")
        year.set("Select Year")
    elif mat:
        tm.showinfo("Course","Don't Use Any Special Characters!\n               eg:BSCCS")
        course_entry.delete(0,"end")
        year.set("Select Year")
    elif year1 == "Select Year":
        tm.showinfo("Course","Please Select Year.")
    else:
        try:
            base=sqlite3.connect('AttendanceManagement_temp.db')
            with base:
                c=base.cursor()
            c.execute('CREATE TABLE IF NOT EXISTS '+class1+'_students (Student TEXT)')
            base.commit()
            base=sqlite3.connect('AttendanceManagement.db')
            with base:
                c=base.cursor()
            c.execute('CREATE TABLE IF NOT EXISTS '+class1+' (Student TEXT,Date TEXT,Attendance int,Subject Text)')
            success = tm.showinfo("Add Class","Class Has Been Succesfully Created!\n               Thank You.")
            course_entry.delete(0,"end")
            year.set("Select Year")
            
        except:
             tm.showinfo("Course","Don't Use Any Special Characters Or Only Numbers!\n               eg:BSCCS")
             course_entry.delete(0,"end")
             year.set("Select Year")
        
  
def addclass():
    try:          
        window5.destroy()
        addclasss()
    except:
        def caps(event):
            course.set(course.get().upper())
       
        def addclass_ui():
            global window6
            window6=Tk()#TKINTER WINDOW
            window6.configure(background="lightblue")#WINDOW BACKGROUND

            window6.geometry('1350x730')
            window6.title("ADD CLASS")
            window6.resizable(False,False)
            

            global course
            global course_entry
            global year
            
            course = StringVar()
            
            text1 = '  ADD CLASS  |                       '
            teacher_label=Label(window6,anchor=W,text=text1,font=("Cosmic Sans MS",13,"bold"),height=2,width=150,fg='black')
            teacher_label.place(x=0,y=50)

            view2_button= Button(window6,text='View Classes',font=("bold",14),bd=0,height=1,fg='gray',command=view_classes)                       
            view2_button.place(x=125,y=53)
            if justice == 'false':
                view2_button.config(text='')
                view2_button['state'] = DISABLED

            back_button= Button(window6,text='Exit',font=("bold",18),bd=0,height=1,fg='gray',command=exit1)                       
            back_button.place(x=1250,y=50)


                        
            course_label=Label(window6,text="Course :",font=("bold",13),fg='gray',bg='lightblue')
            course_label.place(x=500,y=270)
            course_entry=Entry(window6,width=20,font=("bold",15),textvariable=course,bg='pink')
            course_entry.place(x=570,y=270)
            course_entry.bind("<KeyRelease>",caps)

            year_label=Label(window6,text="Year :",font=("bold",13),fg='gray',bg='lightblue')
            year_label.place(x=503,y=340)
            year = StringVar(window6)
            year.set("Select Year")
            popupMenu = OptionMenu(window6,year,'FirstYear','SecondYear','ThirdYear','FourthYear')
            popupMenu.place(x=570,y=340)

            addclass_button= Button(window6,text='Add Class',font=("bold",15),width=15,bg='black',fg='yellow',command=register_class)                        
            addclass_button.place(x=620,y=425)

            window6.mainloop()
        addclass_ui()

def exit1():
    try:
        window6.destroy()
        if justice == 'true':
            admin()
        else:
            teacher()
    except:
        window12.destroy()
        addclass()
        

def view_classes():
    
    window6.destroy()
    global window12
    window12=Tk()#TKINTER WINDOW
    window12.configure(background="lightblue")#WINDOW BACKGROUND

    window12.geometry('1350x730')
    window12.title("VIEW CLASSESS")
    window12.resizable(False,False)

    course_label=Label(window12,anchor=W,text='View Classes',font=("Cosmic Sans MS",13,"bold"),height=2,width=150,fg='black')
    course_label.place(x=0,y=50)

    exit_button= Button(window12,text='Exit',font=("bold",18),bd=0,height=1,fg='gray',command=exit1)                       
    exit_button.place(x=1250,y=50)


    frame = Frame(window12)
    frame.place(x=30,y=100)

    scrollbar = Scrollbar(frame)
    scrollbar.pack( side = RIGHT, fill = Y )

    style = ttk.Style()
    style.theme_use('winnative')

    tree = ttk.Treeview(frame,column=('1')  ,show='headings' ,height=28, yscrollcommand = scrollbar.set)
    tree.column("# 1", width=400)
    tree.heading("# 1", text="Teacher")

    base=sqlite3.connect('AttendanceManagement.db')
    with base:
        c=base.cursor()
     
    query1="SELECT name FROM sqlite_master WHERE type='table'"
    c.execute(query1)
    result1=c.fetchall()
    for classes in result1:
        tree.insert('', 'end', text="1", values=(classes[0]))  

    tree.pack()
    scrollbar.config( command = tree.yview)
    
    

def addstudent():
    def caps0(event):
        course0.set(course0.get().upper())

    def addclass_ui2():
        global window7
        window7=Toplevel()#TKINTER WINDOW
        window7.configure(background="lightblue")

        window7.geometry('550x350')
        window7.resizable(False,False)
        window7.title("ADD STUDENT")
        
        if version == 'True':
            window7.title("ADD CLASS")


        global course0
        global course_entry1
        global year1

        course0 = StringVar()
        

        course_label=Label(window7,text="Course :",font=("bold",13),fg='blue',bg='lightblue')
        course_label.place(x=130,y=100)
        course_entry1=Entry(window7,width=20,font=("bold",15),textvariable=course0)
        course_entry1.place(x=200,y=100)
        course_entry1.bind("<KeyRelease>",caps0)

        year_label=Label(window7,text="Year :",font=("bold",13),fg='blue',bg='lightblue')
        year_label.place(x=130,y=150)
        year1 = StringVar(window7)
        year1.set("Select Year")
        popupMenu = OptionMenu(window7,year1,'FirstYear','SecondYear','ThirdYear','FourthYear')
        popupMenu.place(x=200,y=150)

        enterclass_button= Button(window7,text='Enter Class',font=("bold",15),width=15,bg='black',fg='yellow',command=addstudent_verify)                        
        enterclass_button.place(x=200,y=200)
        
        window7.grab_set()
        window7.mainloop()
    
    addclass_ui2()


def add_password1():
##    def dash():
    global window3
    window3 = Toplevel()
    window3.configure(background="lightblue")#WINDOW BACKGROUND

    window3.geometry('550x350')
    window3.resizable(False,False)
    window3.title("Security")
##    def done():
##        print(passw.get(),passw2.get())

    def backW():
        pass_label.config(text='Enter Password')
        
##        print(passw.get())
        addpass.config(textvariable=passw)
        addpass.delete(0,"end")
##        print(passw.get()) 

        conf_button.config(text='Next',command=nextW)
        b_button.config(bd=0,bg='lightblue',fg='lightblue',command='')

        
    def nextW():
##        global passw2
        pass_label.config(text='Confirm Password')
        
##        print(passw.get())
        addpass.config(textvariable=passw2)
        addpass.delete(0,"end")
##        print(passw.get())

        conf_button.config(text='Confirm',command=encrypt_password)
        b_button.config(text='Previous',bd=2,bg='black',fg='yellow',command=backW)
        b_button['state'] = NORMAL


    global passw
    global passw2
    ##    global uname_entry
    global addpass
    ##    uname = StringVar()
    passw = StringVar()
    passw2 = StringVar()


    ##    teacher_label=Label(window1,anchor=W,text='',font=("bold",13),height=2,width=150,fg='black')
    ##    teacher_label.place(x=0,y=50)

    ##    logout_button= Button(window1,text='HOME',font=("Cosmic Sans MS",15,"bold"),bd=0,height=1,fg='brown',command=close1)                       
    ##    logout_button.place(x=5,y=55)

    pass_label=Label(window3,text="Enter Password",font=("bold",13),fg='blue',bg='lightblue')
    pass_label.place(x=30,y=90)
    addpass=Entry(window3,width=20,font=("bold",20),textvariable=passw,bg='pink',show='*')
    addpass.place(x=30,y=120)

    conf_button= Button(window3,text='Next',font=("bold",15),width=10,bg='black',fg='yellow',command=nextW)
    conf_button.place(x=400,y=220)

    b_button= Button(window3,text='',font=("bold",15),width=10,bd=0,bg='lightblue',fg='lightblue',command='')
    b_button.place(x=30,y=220)
    b_button['state'] = DISABLED

    window3.grab_set()
    window3.mainloop()

    
def addstudent_verify():
    course1=course0.get()
    year2=year1.get()
    class1=course1+'_'+year2

    reg = '[-"@_!#$%^&*().+=<\[>?/|}{~`:\[\]\']'
##    reg = '[0123456789.]'
    pat = re.compile(reg)              
    mat = re.search(pat,course1)

    if course1 == '':
        tm.showinfo("Course","Course Should Not Be Empty!\nPlease Provide Course Name")
        year1.set("Select Year")
        
        window7.focus()
##    elif not mat:
##        tm.showinfo("Course","Don't Use Any Special Characters!\n               eg:BSCCS")
##        course_entry1.delete(0,"end")
##        year1.set("Select Year")
##        window7.focus()
    elif year2 == "Select Year":
        tm.showinfo("Course","Please Select Year.")
        window7.focus()
    else:
        base=sqlite3.connect('AttendanceManagement.db')
        with base:
            c=base.cursor()
            
        c.execute("SELECT name FROM sqlite_master WHERE type='table'")
        result=c.fetchall()
        tables=[]
        for i in result:
            tables.append(i[0])
       
        if class1 in tables:
            window7.destroy()
            try:
                try:
                    window5.destroy()
                    if version == 'True':
                        take_attendance()
                    elif adminR == 'T':
                        attendance_report()
                    else:
                        addstudent_main()
                except:
                    window3.destroy()
                    if adminR == 'T':
                        attendance_report()
                    else:
                        addstudent_main()
            except:
                window13.destroy()
                take_attendance()
  
        else:
            tm.showinfo("Class","'"+class1+"' Class is Don't Exist!")
            course_entry1.delete(0,"end")
            year1.set("Select Year")            
            window7.focus()
                           
def addstudent_main():
    try:
        window11.destroy()
        addstudent_main()
    except:
        course1=course0.get()
        year2=year1.get()
    
        global window8
        window8=Tk()#TKINTER WINDOW
        window8.configure(background="lightblue")

        window8.geometry('1350x730')
        window8.resizable(False,False)
        window8.title("ADD STUDENT")

        global fname
        global mname
        global lname
        global fname_entry
        global mname_entry
        global lname_entry
        fname = StringVar()
        mname = StringVar()
        lname = StringVar()
        
        text1 = course1+' '+year2
        title_label=Label(window8,anchor=CENTER,text=text1,font=("Cosmic Sans MS",13,"bold"),height=1,width=50,fg='black')
        title_label.place(x=420,y=12)

        text2 = '  ADD STUDENT  |                       '
        teacher_label=Label(window8,anchor=W,text=text2,font=("Cosmic Sans MS",13,"bold"),height=2,width=150,fg='black')
        teacher_label.place(x=0,y=50)

        view3_button= Button(window8,text='View Students',font=("bold",14),bd=0,height=1,fg='gray',command=view_students)                       
        view3_button.place(x=155,y=53)
    
        back_button= Button(window8,text='Exit',font=("bold",18),bd=0,height=1,fg='gray',command=exit2)                       
        back_button.place(x=1250,y=50)



        fname_label=Label(window8,text="STUDENT NAME:",font=("bold",13),fg='gray',bg='lightblue')#LABEL FOR FIRST NAME
        fname_label.place(x=470,y=270)
        fname_entry=Entry(window8,width=20,font=("bold",15),textvariable=fname,bg='pink')#ENTRY BOX FOR FIRST NAME
        fname_entry.place(x=625,y=270)


        mname_label=Label(window8,text="FATHER'S NAME:",font=("bold",13),fg='gray',bg='lightblue')#LABEL FOR MIDDLE NAME
        mname_label.place(x=470,y=340)
        mname_entry=Entry(window8,width=20,font=("bold",15),textvariable=mname,bg='pink')#ENTRY BOX FOR MIDDLE NAME
        mname_entry.place(x=625,y=340)

        
        lname_label=Label(window8,text="SURNAME NAME:",font=("bold",13),fg='gray',bg='lightblue')#LABEL FOR MIDDLE NAME
        lname_label.place(x=470,y=410)
        lname_entry=Entry(window8,width=20,font=("bold",15),textvariable=lname,bg='pink')#ENTRY BOX FOR MIDDLE NAME
        lname_entry.place(x=625,y=410)

        
        addstud_button= Button(window8,font=("bold",15),width=15,bg='black',fg='yellow',text='Add Student',command=addstu_main)#BUTTON FOR  LOGIN
        addstud_button.place(x=590,y=500)

def view_students():
    course3=course0.get()
    year3=year1.get()
    class3=course3+'_'+year3
    
    window8.destroy()
    global window11
    window11=Tk()#TKINTER WINDOW
    window11.configure(background="lightblue")#WINDOW BACKGROUND

    window11.geometry('1350x730')
    window11.title("VIEW STUDENTS")
    window11.resizable(False,False)

    course_label=Label(window11,anchor=W,text='View Students',font=("Cosmic Sans MS",13,"bold"),height=2,width=150,fg='black')
    course_label.place(x=0,y=50)

    exit_button= Button(window11,text='Exit',font=("bold",18),bd=0,height=1,fg='gray',command=addstudent_main)                       
    exit_button.place(x=1250,y=50)


    frame = Frame(window11)
    frame.place(x=30,y=100)

    scrollbar = Scrollbar(frame)
    scrollbar.pack( side = RIGHT, fill = Y )

    style = ttk.Style()
    style.theme_use('winnative')

    tree = ttk.Treeview(frame,column=('1','2')  ,show='headings' ,height=28, yscrollcommand = scrollbar.set)
    tree.column("# 1",anchor=CENTER, width=40)
    tree.heading("# 1", text="NO.")
    tree.column("# 2", width=440)
    tree.heading("# 2", text="Students")

    base=sqlite3.connect('AttendanceManagement_temp.db')
    with base:
        c=base.cursor()
  
        
    query="select student from "+class3+"_students"
    c.execute(query)
    result1=c.fetchall()
    stud=[]
    for students in result1:
        stud.append(students[0])
        
    query1="SELECT Count(*) FROM "+class3+"_students"
    c.execute(query1)
    result=c.fetchall()
    for i in result:
        None
    for num in range(0,i[0]):
        tree.insert('', 'end', text="1", values=(num+1,stud[num]))

    tree.pack()
    scrollbar.config( command = tree.yview)


def exit2():
    window8.destroy()
    if justice == 'true':
        admin()
    else:
        teacher()

def addstu_main():
    course1=course0.get()
    year2=year1.get()
    class1=course1+'_'+year2
    fn = fname.get()
    mn = mname.get()
    ln = lname.get()
    stu_name = fn+" "+mn+" "+ln


    reg = '[-"@_!#$%^&*().+=<\[>?/|}{~`:\[\]0123456789]'
    pat = re.compile(reg)              
    mat = re.search(pat,fn)
    mat2 = re.search(pat,mn)
    mat3 = re.search(pat,ln)

 
    if fn == '' or ln == '':
        tm.showinfo("ADD STUDENT","Name Should Not Be Empty!\nPlease Provide Student Name")
    elif mat or mat2 or mat3:
        tm.showinfo("ADD STUDENT","Don't Use Any Special Characters or Numbers!")
    else:
        if mn == '':
            stu_name = fn+" "+ln

        base=sqlite3.connect('AttendanceManagement_temp.db')
        with base:
            c=base.cursor()
    
        c.execute("INSERT INTO "+class1+"_students (Student) VALUES(?)",(stu_name,)) 
        base.commit()
        fname_entry.delete(0,"end")
        mname_entry.delete(0,"end")
        lname_entry.delete(0,"end")        
        tm.showinfo("ADD STUDENT","'"+stu_name+"' added successfully to the class '"+class1+"'" )
    


def changeclass():
    global version
    version = 'True'
    addstudent()

                           
def exit3():
    window13.destroy()
    teacher()

def take_attendance():

    global class1
    course1=course0.get()
    year2=year1.get()
    class1=course1+'_'+year2
    
    global window13
    global row
    global close
    close = 'T'
    
    
    window13=Tk()#TKINTER WINDOW
    window13.configure(background="lightblue")#WINDOW BACKGROUND

    window13.geometry('1359x730')
    window13.title("Take Attendance")
    window13.resizable(False,False)

    frame= Frame(window13,bg='lightblue')
    frame.pack(fill=BOTH, expand=1)

    text1 = course1+' '+year2
    title_label=Label(frame,anchor=CENTER,text=text1,font=("Cosmic Sans MS",13,"bold"),height=1,width=50,fg='black')
    title_label.place(x=420,y=12)

    text2 = 'Take Attendance  |                                |'
    teacher_label=Label(frame,anchor=W,text=text2,font=("Cosmic Sans MS",13,"bold"),height=2,width=150,fg='black')
    teacher_label.place(x=0,y=50)

    report_button= Button(frame,text='Attendance Report',font=("Cosmic Sans MS",13,"bold"),bd=0,height=1,fg='gray',command=Treport)                       
    report_button.place(x=148,y=57)

    addsub_button= Button(frame,text='Add Subject',font=("Cosmic Sans MS",13,"bold"),bd=0,height=1,fg='gray',command=add_subject)                       
    addsub_button.place(x=315,y=57)

    text3 = '|                             |'
    change_label=Label(frame,anchor=W,text=text3,font=("Cosmic Sans MS",13,"bold"),height=2,width=150,fg='black')
    change_label.place(x=1090,y=50)
    change_button= Button(frame,text='Change Class',font=("Cosmic Sans MS",13,"bold"),bd=0,height=1,fg='gray',command=changeclass)                       
    change_button.place(x=1110,y=57)

    back_button= Button(frame,text='Exit',font=("bold",18),bd=0,height=1,fg='gray',command=exit3)                       
    back_button.place(x=1250,y=50)

 
    #create canvas
    canvas = Canvas(frame,height=525,width=1318)
    canvas.place(x=10,y=110)#pack(fill=BOTH, expand=1)
    
    #add scrollbar to the canvas
    myscrollbar= ttk.Scrollbar(frame, orient=VERTICAL,command=canvas.yview)
    myscrollbar.pack(side=RIGHT, fill=Y)

    #configure canvas
    canvas.configure(yscrollcommand=myscrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    #create second frame
    frame2 = Frame(canvas)

    #add new frame to a window in canvas
    canvas.create_window((0,0), window=frame2, anchor="nw")
    
    
    
    base=sqlite3.connect('AttendanceManagement_temp.db')
    with base:
        c=base.cursor()
  
    row = c.execute('select Count(*) from '+class1+'_students')
    for row in c:
        None   

    global myentry
    myentry = []
    
    for x in range(row[0]):
        global v
        v = StringVar() 
        v.set(None)
        male=Radiobutton(frame2, text='Present', variable=v,padx=10, value="1")
        male.grid(row=x,column=3)
        v.set(None)
        female=Radiobutton(frame2, text='Absent', variable=v,padx=10, value="0")
        female.grid(row=x,column=4)
        
        myentry.append(v)
                     
        
    button = Button(frame,text="Submit",font=("bold",15),width=15,bg='black',fg='yellow',command=attendance_capture)
    button.place(x=570,y=650)
    
    label1 = Label(frame2,text='',bg='lightpink',height=row[0]*4,width=3)
    label1.place(x=4,y=0)
    for i in range(row[0]):
        label0 = Label(frame2,text=i+1,bg='lightpink')
        label0.grid(row=i,column=0, pady=15, padx=10)
   
    last = c.execute('select student from '+class1+'_students')
    
    global lal
    lal=[]
    i=0
    for z in last:
        lal.append(z)
        for j in range(row[0]):
            
            label = Label(frame2,text=z[0])
            label.grid(row=i,column=1, pady=15, padx=10)
         
        i=i+1

            
    global cal
    cal_label = Label(frame,text="Pick Date",font=("Cosmic Sans MS",10,"bold"),fg='gray')
    cal_label.place(x=860,y=130)
    cal = DateEntry(frame, heighth=15,width=18,date_pattern="dd/mm/yyyy")
    cal.place(x=860,y=150)

    global subject
    subject = StringVar()
    subject_label = Label(frame,text="Subject",font=("Cosmic Sans MS",10,"bold"),fg='gray')
    subject_label.place(x=860,y=190)

    c.execute('CREATE TABLE IF NOT EXISTS '+class1+'_subject (Subject TEXT)')
    query="select Subject from "+class1+"_subject"
    c.execute(query)
    result2=c.fetchall()
    temp=[]
    temp1=[]
    for subject2 in result2:
            temp.append(subject2[0])
            temp1.append(subject2[0])        
    temp1.append('Select Subject')
    width1 = len(max(temp1,key=len))
    subject.set("Select Subject")
    global atleast
    try:
        atleast = 'False'
        subjectMenu = OptionMenu(frame,subject,*temp)#OPTIONMENU
    except:
        atleast = 'True'
        subjectMenu = OptionMenu(frame,subject,'Select Subject')
        tm.showinfo('Subject','Please Add Subject Atleast One!')
    subjectMenu.config(width = width1-2)
    subjectMenu.place(x=860,y=210)


    window13.mainloop()


def attendance_capture():
    
    ondate = cal.get_date().strftime("%Y/%m/%d")
    sub = subject.get()

    end=[]
    i = 0
    for entries in myentry:
        en=entries.get()
        if sub == 'Select Subject':
            if atleast == 'True':
                tm.showinfo('Subject','Please Add Subject Atleast One!')
            else:
                tm.showinfo("Subject","Subject Should Be Selected!" )  #Subject Should Not Be Empty!\nPlease Provide Subject Name")
                break
        elif en == 'None':
            radio=lal[i]
            tm.showinfo("Attendance","Student '"+radio[0]+"' You Doesn't Mark Any Attendance")
            break
        else:
            end.append(en)
            i=i+1
    
    if i == row[0]:
        try:
            base=sqlite3.connect('AttendanceManagement.db')
            with base:
                c=base.cursor()
            
            for num in range(0,row[0]):
                radio=lal[num]
                c.execute("INSERT INTO "+class1+" (Student,Date,Attendance,Subject) VALUES(?,?,?,?)",(radio[0],ondate,end[num],sub,))
                base.commit()
            success = tm.showinfo("Attendance","Attendance Have Been Marked Successfully!")
            if success:
                window13.destroy()
                take_attendance()
        except:
            tm.showinfo("Subject","Don't Use Any Special Characters!\n               eg:DBMS")


def add_subject():
    global window15
    window15=Toplevel()#TKINTER WINDOW
    window15.configure(background="lightblue")

    window15.geometry('550x350')
    window15.resizable(False,False)
    window15.title("ADD SUBJECT")
    
    global subject
    global subject_entry1
    subject = StringVar()
    

    course_label=Label(window15,text="Subject:",font=("Cosmic Sans MS",14,"bold"),fg='gray',bg='lightblue')
    course_label.place(x=158,y=100)
    subject_entry1=Entry(window15,width=15,font=("bold",15),textvariable=subject)
    subject_entry1.place(x=160,y=130)
    
    enterclass_button= Button(window15,text='ADD',font=("bold",13),width=9,bg='black',fg='yellow',command=sub_verify)                        
    enterclass_button.place(x=280,y=180)
    
    window15.grab_set()
    window15.mainloop()


def sub_verify():
    sub = subject.get()
    reg = '["@!#$%^&*()+=<\[>?/|}{~`:\[\]]'
    pat = re.compile(reg)              
    mat = re.search(pat,sub)

    base=sqlite3.connect('AttendanceManagement_temp.db')
    with base:
        c=base.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS '+class1+'_subject (Subject TEXT)')
    query = "select * from "+class1+"_subject where Subject = '"+sub+"'"
    c.execute(query)
    result=c.fetchall()
    subject1=[]
    for subject2 in result:
            subject1.append(subject2[0])

    if sub == '':
        tm.showinfo('Subject','Subject Should Not Be Empty!\nPlease Provide Subject Name')
    elif mat:
        tm.showinfo('Subject','Subject Should Not Have This Special Characters')
    elif len(subject1) == 0:
        c.execute("INSERT INTO "+class1+"_subject (Subject) VALUES(?)",(sub,))
        base.commit()
        success = tm.showinfo('Subject','Subject Has Been Added Succesfully!')
        if success:
            window15.destroy()
            window13.destroy()
            take_attendance()
        
    elif subject1[0] == sub:
        tm.showinfo('Subject',"'"+sub+"' Subject is Already Exist")
    else:
        c.execute("INSERT INTO "+class1+"_subject (Subject) VALUES(?)",(sub,))
        base.commit()
        success = tm.showinfo('Subject','Subject Has Been Added Succesfully!')
        if success:
            window15.destroy()
            window13.destroy()
            take_attendance()


    
def exit4():
    window14.destroy()
    if justice == 'true':
        admin()
    else:
        if close == 'T':
            take_attendance()
        else:
            teacher()

def Treport():
    window13.destroy()
    attendance_report()
    
def attendance_report():
    def view_report():

        sub = subject1.get()

        if sub == 'Select Subject' :
            tm.showinfo('Add Subject','Subject Should Be Selected!')
        else:

            for item in tree.get_children():
                tree.delete(item)

                
            from2=cal0.get_date().strftime("%Y/%m/%d")
            to2=cal01.get_date().strftime("%Y/%m/%d")

            from1=datetime.strptime(cal1.get(),"%d/%m/%Y")#.strftime("%Y,%m,%d")
            to=datetime.strptime(cal2.get(),"%d/%m/%Y")#.strftime("%Y,%m,%d")
            dt=(to-from1).days+1
                   
            base=sqlite3.connect('AttendanceManagement_temp.db')
            with base:
                c=base.cursor()
                
            query="select student from "+class1+"_students"
            c.execute(query)
            result1=c.fetchall()
            zora1=[]
            num=0
            for classes in result1:
                    zora1.append(classes[0])
                    base=sqlite3.connect('AttendanceManagement.db')
                    with base:
                        c=base.cursor()
                    if sub == 'NONE':
                        query="select Attendance from "+class1+" where Date BETWEEN '"+from2+"' And '"+to2+"' AND Student in ('"+classes[0]+"')" #AND Subject in('"+sub+"')"
                    else:
                        query="select Attendance from "+class1+" where Date BETWEEN '"+from2+"' And '"+to2+"' AND Student in ('"+classes[0]+"') AND Subject in('"+sub+"')"
                    
                         
                    c.execute(query)
                    result=c.fetchall()
                    zora=[]
                    for i in result:
                        zora.append(i[0])
                    total=0
                    for ele in range(0, len(zora)):
                        total = total + zora[ele]
                     
                    # printing total value
                    total1=total*100
                    total2=total1/dt
                    perc = "{:.2f}".format(total2)+'%'
                    tree.insert('', 'end', text="1", values=(num+1,classes[0],total,perc))
                    num = num+1
                    base.commit()

    
    global class1
    course1=course0.get()
    year2=year1.get()
    class1=course1+'_'+year2
    global window14
    global row


    window14=Tk()#TKINTER WINDOW
    window14.configure(background="lightblue")#WINDOW BACKGROUND

    window14.geometry('1350x730')
    window14.title("Attendance Report")
    window14.resizable(False,False)

    text1 = course1+' '+year2
    title_label=Label(window14,anchor=CENTER,text=text1,font=("Cosmic Sans MS",13,"bold"),height=1,width=50,fg='black')
    title_label.place(x=420,y=12)



    text2 = ''#Take Attendance  |                            |'
    take_label=Label(window14,anchor='nw',text=text2,font=("Cosmic Sans MS",14),height=6,width=150,fg='black')
    take_label.place(x=0,y=50)

    text3 = 'Attendance Report'#Take Attendance  |                            |'
    attend_label=Label(window14,anchor=W,text=text3,font=("Cosmic Sans MS",14,"bold"),height=6,width=15,fg='black',bg='lightpink')
    attend_label.place(x=0,y=50)


    global subject1
    subject1 = StringVar()
    subject_label = Label(window14,text="Subject :",font=("Cosmic Sans MS",13,"bold"),fg='gray')
    subject_label.place(x=418,y=66)
    base=sqlite3.connect('AttendanceManagement_temp.db')
    with base:
        c=base.cursor()   
    query="select Subject from "+class1+"_subject"
    c.execute(query)
    result2=c.fetchall()
    temp=[]
    temp1=[]
    for subject in result2:
            temp.append(subject[0])
            temp1.append(subject[0])        
    temp1.append('Select Subject')
    temp.append('NONE')
    width1 = len(max(temp1,key=len))
    subject1.set("Select Subject") 
    subjectMenu = OptionMenu(window14,subject1,*temp)#OPTIONMENU
    subjectMenu.config(width = width1-2)
    subjectMenu.place(x=420,y=90)


    global cal1
    global cal2
    cal1 = StringVar()
    cal2 = StringVar()
    cal_label=Label(window14,text='From :',font=("Cosmic Sans MS",13,"bold"),fg='gray')
    cal_label.place(x=680,y=66)
    cal0 = DateEntry(window14,width=13,selectmode='day',date_pattern="d/m/yyyy",textvariable=cal1)#,background='darkblue',foreground='white', borderwidth=2)
    cal0.place(x=680,y=90)

    cal_label=Label(window14,text='To :',font=("Cosmic Sans MS",13,"bold"),fg='gray')
    cal_label.place(x=930,y=66)
    cal01 = DateEntry(window14,width=13,selectmode='day',date_pattern="d/m/yyyy",textvariable=cal2)#,background='darkblue',foreground='white', borderwidth=2)
    cal01.place(x=930,y=90)


    report_button= Button(window14,text='View Attendance Report',font=("bold",13),width=20,bg='black',fg='yellow',command=view_report)                       
    report_button.place(x=590,y=145)

    attend_label=Label(window14,anchor=W,text='',font=("Cosmic Sans MS",14,"bold"),height=6,width=6,fg='black',bg='lightpink')
    attend_label.place(x=1270,y=50)
    back_button= Button(window14,text='Exit',font=("bold",19),bd=0,height=1,bg='lightpink',fg='black',command=exit4)                       
    back_button.place(x=1278,y=95)

    frame = Frame(window14)
    frame.place(x=200,y=195)

    scrollbar = Scrollbar(frame)
    scrollbar.pack( side = RIGHT, fill = Y )

    style = ttk.Style()
    style.theme_use('winnative')

    tree = ttk.Treeview(frame,column=('1','2','3','4')  ,show='headings' ,height=24, yscrollcommand = scrollbar.set)
    tree.column("# 1",anchor=CENTER, width=40)
    tree.heading("# 1", text="NO.")
    tree.column("# 2", width=300)
    tree.heading("# 2", text="Students Name")
    tree.column("# 3", width=300)
    tree.heading("# 3", text="Attended Days")
    tree.column("# 4", width=300)
    tree.heading("# 4", text="Attendance Percentage")

    tree.pack()
    scrollbar.config( command = tree.yview)
    window14.mainloop()



if __name__ == '__main__':
    main()
