from tkinter import *
import time
import webbrowser
from client import *  #backend
import re
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$' #email format
global data,penalties,q
data={}
penalties=0
#load Question paper from Server
try:
    q=get_questions()
except:
       try:
           q=get_questions()
       except ValueError as val_e:
           print("error",val_e,"occured")
#verify email format
def check(email):
    if (re.search(regex, email)):
        return True
    else:
        return False

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
    heading = Label(sup_frame,text="LOGIN",fg="black",bg="white")
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
        if(len(fullname)<4 or not(check(email))):
            error = Label(sup_frame, text="Enter Valid Name & Email!", fg='black', bg='white')
            error.place(relx=0.40,rely=0.7)
        else:
            data["name"] = fullname
            data["email"] = email
            menu()
    #JOIN BUTTON
    sp = Button(sup_frame,text='LOGIN',padx=5,pady=5,width=5,command = addUserToDataBase,bg='green')
    sp.configure(width = 15,height=1, activebackground = "#33B5E5", relief = FLAT)
    sp.place(relx=0.43,rely=0.8)

def menu():
    sup.destroy()
    global menu,canvas
    menu = Tk()
    menu.title("-Texam-")
    canvas = Canvas(menu, width=626, height=420)
    canvas.grid(column=0, row=1)
    img = PhotoImage(file="Guide.png")
    canvas.create_image(0, 0, image=img, anchor=NW)
    button = Button(menu, text='START', command=easy)
    button.configure(width=46, height=2, activebackground="#33B5E5", bg='green', relief=RAISED,font='Helvetica 18 bold')
    button.grid(column=0, row=2)
    menu.mainloop()
def easy():
    timer = Label(menu)
    timer.place(relx=0.6, rely=0.925, anchor=CENTER)
    for k in range(30, 0, -1):
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
    ch = q[0]["choices"]
    que = q[0]["que"]
    id = q[0]["id"]
    responses={}
    ques = Label(easy_frame, text=que, font="calibri 12", bg="white")
    ques.place(relx=0.5, rely=0.2, anchor=CENTER)
    var = StringVar()
    a = Radiobutton(easy_frame, text=ch[0], font="calibri 10", value=ch[0], variable=var, bg="white")
    a.place(relx=0.5, rely=0.42, anchor=CENTER)
    b = Radiobutton(easy_frame, text=ch[1], font="calibri 10", value=ch[1], variable=var, bg="white")
    b.place(relx=0.5, rely=0.52, anchor=CENTER)
    c = Radiobutton(easy_frame, text=ch[2], font="calibri 10", value=ch[2], variable=var, bg="white")
    c.place(relx=0.5, rely=0.62, anchor=CENTER)
    d = Radiobutton(easy_frame, text=ch[3], font="calibri 10", value=ch[3], variable=var, bg="white")
    d.place(relx=0.5, rely=0.72, anchor=CENTER)
    timer = Label(e)
    timer.place(relx=0.8, rely=0.8, anchor=CENTER)
    for k in range(30, 0, -1):
        timer.configure(text=k)
        easy_frame.update()
        time.sleep(1)
    timer.configure(text="Times up!")
    responses[id]=var.get()
    for i in q[1:]:
        ch = i["choices"]
        que = i["que"]
        id = i["id"]
        ques.configure(text=que)
        a.configure(text=ch[0], value=ch[0])
        b.configure(text=ch[1], value=ch[1])
        c.configure(text=ch[2], value=ch[2])
        d.configure(text=ch[3], value=ch[3])
        for k in range(30, 0, -1):
            timer.configure(text=k)
            easy_frame.update()
            time.sleep(1)
        timer.configure(text="Times up!")
        responses[id] = var.get()
    else:
        e.destroy()
        data["responses"]=responses
        data["penalties"]=penalties
        try:
            post_responses(data)
        except:
            try:
                post_responses(data)
            except ValueError as val_e:
                print("error", val_e, "occured")
        webbrowser.open('https://stackapi.vercel.app/', new=2)
    e.mainloop()

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
