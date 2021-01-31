import tkinter as tk
from tkinter import *
import random
import time
def verification(email):
    #-----harsh will add-----
    return 1234
def push(List,key):
    #-----harsh will add-----
    pass
def pull(key):
    #----harsh will add-----
    pass
def check(key):
    #-----harsh will add---
    return True
def delete(key):
    #----harsh will add----
    pass
def Join(l):
    sup.destroy()
    global login
    login = Tk()
    login.title("-Texam-")
    
    user_name = StringVar()
    password = StringVar()

    
    login_canvas = Canvas(login,width=720,height=440,bg="white")
    login_canvas.pack()

    login_frame = Frame(login_canvas,bg="white")
    login_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    heading = Label(login_frame,text="Login",fg="black",bg="white")
    heading.config(font=('calibri 40'))
    heading.place(relx=0.4,rely=0.1)

    #email Verification code
    ulabel = Label(login_frame,text="Email Verification code",fg='black',bg='white')
    ulabel.place(relx=0.15,rely=0.4)
    uname = Entry(login_frame,bg='#d3d3d3',fg='black',textvariable = user_name)
    uname.config(width=42)
    uname.place(relx=0.31,rely=0.4)

    #Test code
    plabel = Label(login_frame,text="Test Code",fg='black',bg='white')
    plabel.place(relx=0.15,rely=0.5)
    pas = Entry(login_frame,bg='#d3d3d3',fg='black',show="*",textvariable = password)
    pas.config(width=42)
    pas.place(relx=0.31,rely=0.5)
    email_code=uname.get()
    test_code=pas.get()

   #error = Label(login_frame,text="Wrong Username or Password!",fg='black',bg='white')
   #error.place(relx=0.37,rely=0.7)
    
    #LOGIN BUTTON
    log = Button(login_frame,text='Join Now',padx=5,pady=5,width=5,command=check)
    log.configure(width = 15,height=1, activebackground = "#33B5E5", relief = FLAT,bg="green")
    log.place(relx=0.4,rely=0.6)
    
    login.mainloop()


def Create(l):
    sup.destroy()
    global login
    login = Tk()
    login.title("-Texam-")

    user_name = StringVar()
    password = StringVar()

    login_canvas = Canvas(login, width=720, height=440, bg="white")
    login_canvas.pack()

    login_frame = Frame(login_canvas, bg="white")
    login_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    heading = Label(login_frame, text="Login", fg="black", bg="white")
    heading.config(font=('calibri 40'))
    heading.place(relx=0.4, rely=0.1)

    # email Verification code
    ulabel = Label(login_frame, text="Email Verification code", fg='black', bg='white')
    ulabel.place(relx=0.15, rely=0.4)
    uname = Entry(login_frame, bg='#d3d3d3', fg='black', textvariable=user_name)
    uname.config(width=42)
    uname.place(relx=0.31, rely=0.4)

    # Test code
    plabel = Label(login_frame, text="Test Code", fg='black', bg='white')
    plabel.place(relx=0.15, rely=0.5)
    pas = Entry(login_frame, bg='#d3d3d3', fg='black', show="*", textvariable=password)
    pas.config(width=42)
    pas.place(relx=0.31, rely=0.5)
    email_code = uname.get()
    test_code = pas.get()

    # error = Label(login_frame,text="Wrong Username or Password!",fg='black',bg='white')
    # error.place(relx=0.37,rely=0.7)

    # LOGIN BUTTON
    log = Button(login_frame, text='Login', padx=5, pady=5, width=5, command=check)
    log.configure(width=15, height=1, activebackground="#33B5E5", relief=FLAT, bg="green")
    log.place(relx=0.4, rely=0.6)

    login.mainloop()

def signUpPage():
    root.destroy()
    global sup
    sup = Tk()
    sup.title("-Texam-")
    fname = StringVar()
    uname = StringVar()
    sup_canvas = Canvas(sup,width=720,height=440,bg="white")
    sup_canvas.pack()
    sup_frame = Frame(sup_canvas,bg="white")
    sup_frame.place(relwidth=0.7,relheight=0.8,relx=0.1,rely=0.1)
    heading = Label(sup_frame,text="Login",fg="black",bg="white")
    heading.config(font=('calibri 40'))
    heading.place(relx=0.4,rely=0.1)
    #full name
    flabel = Label(sup_frame,text="Full Name",fg='black',bg='white')
    flabel.place(relx=0.15,rely=0.4)
    fname = Entry(sup_frame,bg='#d3d3d3',fg='black',textvariable = fname)
    fname.config(width=42)
    fname.place(relx=0.31,rely=0.4)
    #email
    ulabel = Label(sup_frame,text="Email ID",fg='black',bg='white')
    ulabel.place(relx=0.15,rely=0.5)
    user = Entry(sup_frame,bg='#d3d3d3',fg='black',textvariable = uname)
    user.config(width=42)
    user.place(relx=0.31,rely=0.5)
    def addUserToDataBase():
        fullname = fname.get()
        email = user.get()
        if len(fullname)<3 or len(email)<3:
            error = Label(login_frame, text="Enter Valid Name & Email!", fg='black', bg='white')
            error.place(relx=0.37,rely=0.7)
        else:
            code = verification(email)
            l=[fullname,email,code]
            Join(l)
    def addUserToDataBase2():
        fullname = fname.get()
        email = user.get()
        l=[fullname,email]
        Create(l)
    #JOIN BUTTON
    sp = Button(sup_frame,text='JOIN TEST',padx=5,pady=5,width=5,command = addUserToDataBase,bg='green')
    sp.configure(width = 15,height=1, activebackground = "#33B5E5", relief = FLAT)
    sp.place(relx=0.45,rely=0.8)
    #CREATE BUTTON
    log = Button(sup_frame,text='CREATE TEST',padx=5,pady=5,width=5,command = addUserToDataBase2,bg="white",fg='blue')
    log.configure(width = 15,height=1, activebackground = "#33B5E5", relief = FLAT)
    log.place(relx=0.45,rely=0.9)
    sup.mainloop()

def menu():
    login.destroy()
    global menu,canvas
    menu = Tk()
    menu.title("-Texam-")
    canvas = Canvas(menu, width=626, height=420)
    canvas.grid(column=0, row=1)
    img = PhotoImage(file="Guide.png")
    canvas.create_image(0, 0, image=img, anchor=NW)
    button = Button(menu, text='START', command=easy)
    button.configure(width=46, height=2, activebackground="#33B5E5", bg='green', relief=RAISED,
                     font='Helvetica 18 bold')
    button.grid(column=0, row=2)
    menu.mainloop()
def easy():
    timer = Label(menu)
    timer.place(relx=0.6, rely=0.925, anchor=CENTER)
    for k in range(60, 0, -1):
        timer.configure(text=k)
        canvas.update()
        time.sleep(1)
    menu.destroy()
    global e
    e = Tk()
    easy_canvas = Canvas(e,width=720,height=440,bg="black")
    easy_canvas.pack()
    easy_frame = Frame(easy_canvas,bg="white")
    easy_frame.place(relwidth=0.9,relheight=0.9,relx=0.05,rely=0.05)

    
    def countDown():
        check = 0
        for k in range(90, 0, -1):
            
            if k == 1:
                check=-1
            timer.configure(text=k)
            easy_frame.update()
            time.sleep(1)
            
        timer.configure(text="Times up!")
        if check==-1:
            calc()
            return (-1)
        else:
            return 0
    global score
    score = 0
    
    easyQ = [
                 [
                     "What will be the output of the following Python code? \nl=[1, 0, 2, 0, 'hello', '', []] \nlist(filter(bool, nl))",
                     "[1, 0, 2, ‘hello’, '', []]",
                     "Error",
                     "[1, 2, ‘hello’]",
                     "[1, 0, 2, 0, ‘hello’, '', []]" 
                 ] ,
                 [
                     "What will be the output of the following Python expression if the value of x is 34? \nprint(“%f”%x)" ,
                    "34.00",
                    "34.000000",
                    "34.0000",
                    "34.00000000"
                     
                 ],
                [
                    "What will be the value of X in the following Python expression? \nX = 2+9*((3*12)-8)/10" ,
                    "30.8",
                    "27.2",
                    "28.4",
                    "30.0"
                ],
                [
                    "Which of these in not a core data type?" ,
                    "Tuples",
                    "Dictionary",
                    "Lists",
                    "Class"
                ],
                [
                    "Which of the following represents the bitwise XOR operator?" ,
                    "&",
                    "!",
                    "^",
                    "|"
                ]
            ]
    answer = [
                "[1, 2, ‘hello’]",
                "34.000000",
                "27.2",
                "Class",
                "^"
             ]
    li = ['',0,1,2,3,4]
    x = random.choice(li[1:])
    
    ques = Label(easy_frame,text =easyQ[x][0],font="calibri 12",bg="white")
    ques.place(relx=0.5,rely=0.2,anchor=CENTER)

    var = StringVar()
    
    a = Radiobutton(easy_frame,text=easyQ[x][1],font="calibri 10",value=easyQ[x][1],variable = var,bg="white")
    a.place(relx=0.5,rely=0.42,anchor=CENTER)

    b = Radiobutton(easy_frame,text=easyQ[x][2],font="calibri 10",value=easyQ[x][2],variable = var,bg="white")
    b.place(relx=0.5,rely=0.52,anchor=CENTER)

    c = Radiobutton(easy_frame,text=easyQ[x][3],font="calibri 10",value=easyQ[x][3],variable = var,bg="white")
    c.place(relx=0.5,rely=0.62,anchor=CENTER) 

    d = Radiobutton(easy_frame,text=easyQ[x][4],font="calibri 10",value=easyQ[x][4],variable = var,bg="white")
    d.place(relx=0.5,rely=0.72,anchor=CENTER) 
    
    li.remove(x)
    
    timer = Label(e)
    timer.place(relx=0.8,rely=0.82,anchor=CENTER)

    def display():
        
        if len(li) == 1:
                e.destroy()
                showMark(score)
        if li:
            x = random.choice(li[1:])
            ques.configure(text =easyQ[x][0])
            
            a.configure(text=easyQ[x][1],value=easyQ[x][1])
      
            b.configure(text=easyQ[x][2],value=easyQ[x][2])
      
            c.configure(text=easyQ[x][3],value=easyQ[x][3])
      
            d.configure(text=easyQ[x][4],value=easyQ[x][4])
            
            li.remove(x)
            print(li)
            y = countDown()
            if y == -1:
                display()

            
    def calc():
        global score
        if (var.get() in answer):
            score+=1
        display()

    y = countDown()
    if y == -1:
        display()
    e.mainloop()
    
    

def showMark(mark):
    global sh
    sh = Tk()
    
    show_canvas = Canvas(sh,width=720,height=440,bg="#101357")
    show_canvas.pack()

    show_frame = Frame(show_canvas,bg="white")
    show_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)
    
    st = "Your score is "+str(mark)
    mlabel = Label(show_canvas,text=st,fg="black")
    mlabel.place(relx=0.5,rely=0.2,anchor=CENTER)
    
    sh.mainloop()
def start():
    global root 
    root = Tk()
    root.title("-Welcome to Texam-")
    canvas = Canvas(root,width = 626,height = 420)
    canvas.grid(column = 0 , row = 1)
    img = PhotoImage(file="back.png")
    canvas.create_image(0,0,image=img,anchor=NW)

    button = Button(root, text='START',command = signUpPage)
    button.configure(width = 46,height=2, activebackground = "#33B5E5", bg ='green', relief = RAISED,font='Helvetica 18 bold')
    button.grid(column = 0 , row = 2)

    root.mainloop()
    
    
if __name__=='__main__':
    start()
