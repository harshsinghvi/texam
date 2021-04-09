from tkinter import *
import webbrowser
from client import *
# from sound import *
from AI import *
import re
import time
from urllib.request import urlopen
from requests import get

ip = get('https://api.ipify.org').text
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  # email format
global data, penalties, q, dope
dope = 0
data = {}
penalties = 0
data["sys_info"] = getSystemInfo()


def me(ch):
    s = ''
    lst = []
    dope = False
    for i in range(5):
        x, flag = update()
        if flag == True:
            dope = True
        else:
            dope = False
        lst.append(x)
    a = max(set(lst), key=lst.count)
    if a == 5:
        return s, flag
    elif a == 0:
        return 0, flag
    elif a== 6:
        return 6, flag
    elif a==7:
        return 7, flag
    else:
        return ch[a - 1], flag


# load Question paper from Server
try:
    q = get_questions()
except:
    try:
        q = get_questions()
    except ValueError as val_e:
        print("error", val_e, "occured")


# verify email format
def check(email):
    if (re.search(regex, email)):
        return True
    else:
        return False


def lead():
    webbrowser.open(URL, new=2)


def signUpPage():
    root.destroy()
    global sup
    sup = Tk()
    sup.geometry("626x475+800+0")
    sup.title("-Texam-")
    fname = StringVar()
    uname = StringVar()
    sup_canvas = Canvas(sup, width=720, height=440, bg="white")
    sup_canvas.pack()
    sup_frame = Frame(sup_canvas, bg="white")
    sup_frame.place(relwidth=0.7, relheight=0.8, relx=0.1, rely=0.1)
    heading = Label(sup_frame, text="LOGIN", fg="black", bg="white")
    heading.config(font=('calibri 40'))
    heading.place(relx=0.4, rely=0.1)
    # full name
    flabel = Label(sup_frame, text="Full Name", fg='black', bg='white')
    flabel.place(relx=0.15, rely=0.4)
    fname = Entry(sup_frame, bg='#d3d3d3', fg='black', textvariable=fname)
    fname.config(width=42)
    fname.place(relx=0.31, rely=0.4)
    # email
    ulabel = Label(sup_frame, text="Email ID", fg='black', bg='white')
    ulabel.place(relx=0.15, rely=0.5)
    user = Entry(sup_frame, bg='#d3d3d3', fg='black', textvariable=uname)
    user.config(width=42)
    user.place(relx=0.31, rely=0.5)

    def addUserToDataBase():
        fullname = fname.get()
        email = user.get()
        if (len(fullname) < 4 or not (check(email))):
            error = Label(sup_frame, text="Enter Valid Name & Email!", fg='black', bg='white')
            error.place(relx=0.40, rely=0.7)
        else:
            data["name"] = fullname
            data["email"] = email
            menu()

    # JOIN BUTTON
    sp = Button(sup_frame, text='LOGIN', padx=5, pady=5, width=5, command=addUserToDataBase, bg='royal blue')
    sp.configure(width=15, height=1, activebackground="gray24", relief=FLAT,font='Helvetica 18 bold')
    sp.place(relx=0.38, rely=0.8)


def menu():
    sup.destroy()
    global menu, canvas
    menu = Tk()
    menu.geometry("626x475+800+0")
    menu.title("-Texam-")
    canvas = Canvas(menu, width=626, height=420)
    canvas.grid(column=0, row=1)
    image_url = "https://raw.githubusercontent.com/Garvit9000c/CS100/master/Guide.png"
    image_byt = urlopen(image_url).read()
    photo = PhotoImage(data=image_byt)
    canvas.create_image(0, 0, image=photo, anchor=NW)
    button = Button(menu, text='START', command=easy)
    button.configure(width=46, height=2, activebackground="#33B5E5", bg='gray24', relief=RAISED,
                     font='Helvetica 18 bold')
    button.grid(column=0, row=2)
    menu.mainloop()


def showMark(mark):
    e.destroy()
    cv2.destroyAllWindows()
    cap.release()
    global sh
    sh = Tk()
    sh.title("-RESULT-")
    total = int((mark['total']))
    max = len(q) *4
    per = total * 100/max
    show_canvas = Canvas(sh, width=720, height=440, bg="black")
    show_canvas.pack()
    show_frame = Frame(show_canvas, bg="white")
    show_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
    st = "Your score is " + str(total) + " out of "+str(max)+". i.e " + str(per) + "%"
    mlabel = Label(show_canvas, text=st, fg="black")
    mlabel.place(relx=0.5, rely=0.2, anchor=CENTER)
    sp = Button(show_frame, text='LeaderBoard', padx=5, pady=5, width=5, command=lead, bg='green')
    sp.configure(width=15, height=1, activebackground="#33B5E5", relief=FLAT)
    sp.place(relx=0.40, rely=0.6)


def easy():
    global penalties, dope
    timer = Label(menu)
    timer.place(relx=0.6, rely=0.950, anchor=CENTER)
    for k in range(10, 0, -1):
        timer.configure(text=k)
        canvas.update()
        time.sleep(1)
    menu.destroy()
    global e
    e = Tk()
    e.geometry("626x475+800+0")
    e.title("-Texam-")
    easy_canvas = Canvas(e, width=720, height=440, bg="black")
    easy_canvas.pack()
    easy_frame = Frame(easy_canvas, bg="white")
    easy_frame.place(relwidth=0.9, relheight=0.9, relx=0.05, rely=0.05)
    timer = Label(e)
    timer.place(relx=0.8, rely=0.8, anchor=CENTER)
    ques = Label(easy_frame, text="", font="calibri 12", bg="white")
    ques.place(relx=0.5, rely=0.2, anchor=CENTER)
    var = StringVar()
    a_ = Radiobutton(easy_frame, text='', font="calibri 10", value='', variable=var, bg="white")
    a_.place(relx=0.5, rely=0.42, anchor=CENTER)
    b = Radiobutton(easy_frame, text='', font="calibri 10", value='', variable=var, bg="white")
    b.place(relx=0.5, rely=0.52, anchor=CENTER)
    c = Radiobutton(easy_frame, text='', font="calibri 10", value='', variable=var, bg="white")
    c.place(relx=0.5, rely=0.62, anchor=CENTER)
    d = Radiobutton(easy_frame, text='', font="calibri 10", value='', variable=var, bg="white")
    d.place(relx=0.5, rely=0.72, anchor=CENTER)
    responses = {}
    a = 0
    lim = len(q) - 1
    for i in q:
        responses[i["id"]] = ''
    for k in range(50, 0, -1):
        timer.configure(text=k)
        ch = q[a]["choices"]
        que = q[a]["que"]
        id = q[a]["id"]
        ques.configure(text=que)
        a_.configure(text=ch[0], value=ch[0])
        b.configure(text=ch[1], value=ch[1])
        c.configure(text=ch[2], value=ch[2])
        d.configure(text=ch[3], value=ch[3])
        var.set(responses[id])
        easy_frame.update()
        z, flag = me(ch)
        if z != 0:
            if z == 6:
                if a>0:
                    a -= 1
            elif z == 7:
                if a < lim:
                    a += 1
            else:
                var.set(z)
                responses[id]=z
        easy_frame.update()
        # if f():
        #    dope+=1
        if flag:
            penalties += 1
    else:
        timer.configure(text="Time out!")
        # dope-=3
        # penalties += dope
        data["responses"] = responses
        data["penalties"] = str(penalties)
        try:
            r = post_responses(data)
            showMark(r)
        except:
            try:
                r = post_responses(data)
                showMark(r)
            except ValueError as val_e:
                print("error", val_e, "occured")
    e.mainloop()


def start():
    global root
    root = Tk()
    root.title("-Welcome to Texam-")
    root.geometry("626x475+800+0")
    canvas = Canvas(root, width=626, height=420)
    canvas.grid(column=0, row=1)
    image_url = "https://raw.githubusercontent.com/Garvit9000c/CS100/master/back.png"
    image_byt = urlopen(image_url).read()
    photo = PhotoImage(data=image_byt)
    canvas.create_image(0, 0, image=photo, anchor=NW)
    button = Button(root, text='START', command=signUpPage)
    button.configure(width=46, height=2, activebackground="royal blue", bg='gray24', relief=RAISED,
                     font='Helvetica 18 bold')
    button.grid(column=0, row=2)
    root.mainloop()


if __name__ == '__main__':
    start()