"""
This is python GUI made out of tkinter
it is a quiz application

Developed by Akhil Krishna in 2021
"""

from tkinter import *
from time import sleep as s
from tkinter.font import Font
import sqlite3 as sq

mycon = sq.connect('Profile.db')
cursor = mycon.cursor()
cursor.execute('create table if not exists users(first  char(20),last char(20),Age int,Gender int,Score int default 0)')
mycon.commit()


# ===========Front phase==

def front():
    fwin = Tk()
    fwin.geometry("600x800")
    ffnt = Font(family='Arial', size=13, weight='bold')

    def start():
        fwin.destroy()

    g = PhotoImage(file='3.png')
    l = Label(fwin, image=g, height=1400).place(x=-130, y=-250)
    #	log=PhotoImage(file='zz.png')
    #	labf=Label(fwin,image=log,width=355,height=335).place(x=160,y=500)
    learn = Label(fwin, text='   LEARN TO CODE   ', fg='aqua', bg='black', font=ffnt, bd=5, relief='raised', width=15)
    learn.place(x=150, y=890)

    start = Button(fwin, text='START', fg='white', activeforeground='white', activebackground='light green',
                   bg='light green', bd=10, font=ffnt, command=start)
    start.place(x=250, y=600)

    fwin.mainloop()


front()

# ==============Registration=

mode = ''


def chodi():
    global modeL
    loo = Tk()
    loo.geometry("600x800")

    def proceed():
        loo.destroy()

    loo['bg'] = 'black'

    def m():
        global mode
        mode = 'm'
        inf = Label(loo,
                    text="Next slide is a registration part so in that you\n need to enter details for participating in quiz \n\nAs you know replit will not allow onscreen\n keyboard so mobile users cannot enter their \ndetails but those who are having keyboard can \nconnect it to mobile using usb and enter\n but for others there will be separate \nonscreen keyboard ,so that you can click on\n buttons for entering details .After\n proceeding you can start clicking on buttons\n at bottom to fill first column then click \non the button named 'To Next row' to enter\ndetails of next row again click on the same \n button to migrate to next row and fill age\n details,atlast click on either male or female ",
                    width=37, height=18)
        inf.place(x=40, y=600)
        Button(loo, text='I read the above instruction, can proceed', activebackground='blue', activeforeground='white',
               bd=5, relief='solid', bg='blue', fg='white', width=33, command=proceed).place(x=40, y=1210)

    def l():
        global mode
        mode = 'l'
        inf = Label(loo,
                    text="Next slide is a registration form please provide\n valid details as there will be a quiz,then \ncertificate will be provided to you based on the\n details you provide")
        inf.place(x=35, y=600)
        Button(loo, text='I read the above instruction, can proceed', bd=5, relief='solid', bg='blue',
               activebackground='blue', activeforeground='white', fg='white', width=33, command=proceed).place(x=33,
                                                                                                               y=750)

    Label(loo, text='Through which mode did you \nopen this App UI?', bg='black', fg='white',
          font=Font(family='arial', size=10, weight='bold')).place(x=110, y=300)
    Button(loo, text='Mobile', bg='white', command=m).place(x=200, y=500)
    Button(loo, bg='white', text='PC/Lap', command=l).place(x=400, y=500)

    loo.mainloop()


chodi()

noc = 0
name = ''
last = ''


def signup():
    global name, last
    signwin = Tk()
    signwin.geometry("600x800")
    gen = IntVar()

    def submit():
        global name, last
        fn = ntake.get()
        ln = ntake2.get()
        age = ntake3.get()
        x = gen.get()
        if len(age) < 3 and len(age) > 0 and len(fn + ln) > 2 and fn != "" and ln != "" and x != 0:

            name = str(fn)
            last = str(ln)
            cursor.execute('insert into users values("{}","{}","{}",{},{})'.format(fn, ln, age, x, 0))
            mycon.commit()

            signwin.destroy()
        elif x == 0 or ln == '' or fn == '' or age == "":
            inst = Label(signwin, text='*Please fill all informations', fg='red', bg='white')
            inst.place(x=110, y=526)
        else:
            inst = Label(signwin, text="*Please provide correct data", fg='red', bg='white')
            inst.place(x=110, y=526)

    fnt = Font(family='Arial'
               , size=13, weight='bold', underline=0)
    fnt1 = Font(family='arial', size=10, weight='normal', underline=0)

    signwin['bg'] = 'white'
    bg = PhotoImage(file='Logo1.png')
    ls = Label(signwin, image=bg, width=300, height=300).place(x=210, y=50)
    head = Label(signwin, text='Registration Form', fg='grey', font=fnt, bg='white', bd=6, relief='solid', width=20,
                 height=2).place(x=90, y=380)

    name = Label(signwin, text='First Name ', bg='grey', fg='white', font=fnt1, width=10).place(x=115, y=570)
    dot1 = Label(signwin, text=':', font=fnt, bg="white").place(x=335, y=565)
    ntake = Entry(signwin, width=15)
    ntake.place(x=360, y=575)

    name2 = Label(signwin, text=' Last Name ', bg='grey', fg='white', font=fnt1).place(x=115, y=670)
    dot2 = Label(signwin, text=':', font=fnt, bg="white").place(x=335, y=663)
    ntake2 = Entry(signwin, width=15)
    ntake2.place(x=358, y=675)

    Age = Label(signwin, text='      Age         ', bg='grey', fg='white', font=fnt1).place(x=115, y=770)
    dot3 = Label(signwin, text=':', font=fnt, bg="white").place(x=335, y=765)
    ntake3 = Entry(signwin, width=15)
    ntake3.place(x=358, y=775)

    gender = Label(signwin, text='    Gender    ', font=fnt1, bg='grey', fg='white').place(x=115, y=875)
    dot4 = Label(signwin, text=':', font=fnt, bg="white").place(x=335, y=865)
    r1 = Radiobutton(signwin, text='Male', bg='white', value=1, variable=gen).place(x=360, y=875)
    r1 = Radiobutton(signwin, text='Female', bg='white', value=2, variable=gen).place(x=520, y=875)

    sub = Button(signwin, text='SUBMIT', fg='white', bg='black', activebackground='black', activeforeground='white',
                 font=fnt1, command=submit).place(x=280, y=1000)

    signwin.mainloop()


def signupm():
    global noc, name, last
    signwin = Tk()
    signwin.geometry("600x800")
    gen = IntVar()

    def submit():
        global name, last
        fn = ntake.get()
        ln = ntake2.get()
        age = ntake3.get()
        x = gen.get()
        if len(age) < 3 and len(age) > 0 and len(fn + ln) > 2 and x != 0:
            name = str(fn)
            last = str(ln)

            cursor.execute('insert into users values("{}","{}","{}",{},{})'.format(fn, ln, age, x, 0))
            mycon.commit()

            signwin.destroy()
        elif x == 0 or ln == '' or fn == '' or age == '':
            inst = Label(signwin, text='*Please fill all informations', fg='red', bg='white')
            inst.place(x=110, y=526)
        else:
            inst = Label(signwin, text="*Please provide correct data", fg='red', bg='white')
            inst.place(x=110, y=526)

    fnt = Font(family='Arial'
               , size=13, weight='bold', underline=0)
    fnt1 = Font(family='arial', size=10, weight='normal', underline=0)

    signwin['bg'] = 'white'
    bg = PhotoImage(file='Logo1.png')
    ls = Label(signwin, image=bg, width=300, height=300).place(x=210, y=50)
    head = Label(signwin, text='Registration Form', fg='grey', font=fnt, bg='white', bd=6, relief='solid', width=20,
                 height=2).place(x=90, y=380)

    name = Label(signwin, text='First Name ', bg='grey', fg='white', font=fnt1, width=10).place(x=115, y=570)
    dot1 = Label(signwin, text=':', font=fnt, bg="white").place(x=335, y=565)
    ntake = Entry(signwin, width=15, bg='white')
    ntake.place(x=360, y=575)

    name2 = Label(signwin, text=' Last Name ', bg='grey', fg='white', font=fnt1).place(x=115, y=670)
    dot2 = Label(signwin, text=':', font=fnt, bg="white").place(x=335, y=663)
    ntake2 = Entry(signwin, width=15, bg='white')
    ntake2.place(x=358, y=675)

    Age = Label(signwin, text='      Age         ', bg='grey', fg='white', font=fnt1).place(x=115, y=770)
    dot3 = Label(signwin, text=':', font=fnt, bg="white").place(x=335, y=765)
    ntake3 = Entry(signwin, width=15, bg='white')
    ntake3.place(x=358, y=775)

    gender = Label(signwin, text='    Gender    ', font=fnt1, bg='grey', fg='white').place(x=115, y=875)
    dot4 = Label(signwin, text=':', font=fnt, bg="white").place(x=335, y=865)
    r1 = Radiobutton(signwin, text='Male', bg='white', value=1, variable=gen).place(x=360, y=875)
    r1 = Radiobutton(signwin, text='Female', bg='white', value=2, variable=gen).place(x=520, y=875)

    sub = Button(signwin, text='SUBMIT', fg='white', bg='black', font=fnt1, command=submit).place(x=280, y=950)

    def nex():
        global noc
        noc += 1

    def ac():
        if noc == 0:
            ntake.insert(END, 'A')
        elif noc == 2:

            ntake3.insert(END, 'A')
        elif noc == 1:
            ntake2.insert(END, 'A')

    def bc():
        if noc == 0:
            ntake.insert(END, 'B')
        elif noc == 2:

            ntake3.insert(END, 'B')
        elif noc == 1:
            ntake2.insert(END, 'B')

    def cc():
        if noc == 0:
            ntake.insert(END, 'C')
        elif noc == 2:

            ntake3.insert(END, 'C')
        elif noc == 1:
            ntake2.insert(END, 'C')

    def dc():
        if noc == 0:
            ntake.insert(END, 'D')
        elif noc == 2:

            ntake3.insert(END, 'D')
        elif noc == 1:
            ntake2.insert(END, 'D')

    def ec():
        if noc == 0:
            ntake.insert(END, 'E')
        elif noc == 2:

            ntake3.insert(END, 'E')
        elif noc == 1:
            ntake2.insert(END, 'E')

    def fc():
        if noc == 0:
            ntake.insert(END, 'F')
        elif noc == 2:

            ntake3.insert(END, 'F')
        elif noc == 1:
            ntake2.insert(END, 'F')

    def gc():
        if noc == 0:
            ntake.insert(END, 'G')
        elif noc == 2:

            ntake3.insert(END, 'G')
        elif noc == 1:
            ntake2.insert(END, 'G')

    def hc():
        if noc == 0:
            ntake.insert(END, 'H')
        elif noc == 2:

            ntake3.insert(END, 'H')
        elif noc == 1:
            ntake2.insert(END, 'H')

    def ic():
        if noc == 0:
            ntake.insert(END, 'I')
        elif noc == 2:

            ntake3.insert(END, 'I')
        elif noc == 1:
            ntake2.insert(END, 'I')

    def jc():
        if noc == 0:
            ntake.insert(END, 'J')
        elif noc == 2:

            ntake3.insert(END, 'J')
        elif noc == 1:
            ntake2.insert(END, 'J')

    def kc():
        if noc == 0:
            ntake.insert(END, 'K')
        elif noc == 2:

            ntake3.insert(END, 'K')
        elif noc == 1:
            ntake2.insert(END, 'K')

    def lc():
        if noc == 0:
            ntake.insert(END, 'L')
        elif noc == 2:

            ntake3.insert(END, 'L')
        elif noc == 1:
            ntake2.insert(END, 'L')

    def mc():
        if noc == 0:
            ntake.insert(END, 'M')
        elif noc == 2:

            ntake3.insert(END, 'M')
        elif noc == 1:
            ntake2.insert(END, 'M')

    def nc():
        if noc == 0:
            ntake.insert(END, 'N')
        elif noc == 2:

            ntake3.insert(END, 'N')
        elif noc == 1:
            ntake2.insert(END, 'N')

    def oc():
        if noc == 0:
            ntake.insert(END, 'O')
        elif noc == 2:

            ntake3.insert(END, 'O')
        elif noc == 1:
            ntake2.insert(END, 'O')

    def pc():
        if noc == 0:
            ntake.insert(END, 'P')
        elif noc == 2:

            ntake3.insert(END, 'P')
        elif noc == 1:
            ntake2.insert(END, 'P')

    def qc():
        if noc == 0:
            ntake.insert(END, 'Q')
        elif noc == 2:

            ntake3.insert(END, 'Q')
        elif noc == 1:
            ntake2.insert(END, 'Q')

    def rc():
        if noc == 0:
            ntake.insert(END, 'R')
        elif noc == 2:

            ntake3.insert(END, 'R')
        elif noc == 1:
            ntake2.insert(END, 'R')

    def sc():
        if noc == 0:
            ntake.insert(END, 'S')
        elif noc == 2:

            ntake3.insert(END, 'S')
        elif noc == 1:
            ntake2.insert(END, 'S')

    def tc():
        if noc == 0:
            ntake.insert(END, 'T')
        elif noc == 2:

            ntake3.insert(END, 'T')
        elif noc == 1:
            ntake2.insert(END, 'T')

    def uc():
        if noc == 0:
            ntake.insert(END, 'U')
        elif noc == 2:

            ntake3.insert(END, 'U')
        elif noc == 1:
            ntake2.insert(END, 'U')

    def vc():
        if noc == 0:
            ntake.insert(END, 'V')
        elif noc == 2:

            ntake3.insert(END, 'V')
        elif noc == 1:
            ntake2.insert(END, 'V')

    def wc():
        if noc == 0:
            ntake.insert(END, 'W')
        elif noc == 2:

            ntake3.insert(END, 'W')
        elif noc == 1:
            ntake2.insert(END, 'W')

    def xc():
        if noc == 0:
            ntake.insert(END, 'X')
        elif noc == 2:

            ntake3.insert(END, 'X')
        elif noc == 1:
            ntake2.insert(END, 'X')

    def yc():
        if noc == 0:
            ntake.insert(END, 'Y')
        elif noc == 2:

            ntake3.insert(END, 'Y')
        elif noc == 1:
            ntake2.insert(END, 'Y')

    def zc():
        if noc == 0:
            ntake.insert(END, 'Z')
        elif noc == 2:

            ntake3.insert(END, 'Z')
        elif noc == 1:
            ntake2.insert(END, 'Z')

    def c0():
        if noc == 0:
            ntake.insert(END, '0')
        elif noc == 2:

            ntake3.insert(END, '0')
        elif noc == 1:
            ntake2.insert(END, '0')

    def c1():
        if noc == 0:
            ntake.insert(END, '1')
        elif noc == 2:

            ntake3.insert(END, '1')
        elif noc == 1:
            ntake2.insert(END, '1')

    def c2():
        if noc == 0:
            ntake.insert(END, '2')
        elif noc == 2:

            ntake3.insert(END, '2')
        elif noc == 1:
            ntake2.insert(END, '2')

    def c3():
        if noc == 0:
            ntake.insert(END, '3')
        elif noc == 2:

            ntake3.insert(END, '3')
        elif noc == 1:
            ntake2.insert(END, '3')

    def c4():
        if noc == 0:
            ntake.insert(END, '4')
        elif noc == 2:

            ntake3.insert(END, '4')
        elif noc == 1:
            ntake2.insert(END, '4')

    def c5():
        if noc == 0:
            ntake.insert(END, '5')
        elif noc == 2:

            ntake3.insert(END, '5')
        elif noc == 1:
            ntake2.insert(END, '5')

    def c6():
        if noc == 0:
            ntake.insert(END, '6')
        elif noc == 2:

            ntake3.insert(END, '6')
        elif noc == 1:
            ntake2.insert(END, '6')

    def c7():
        if noc == 0:
            ntake.insert(END, '7')
        elif noc == 2:

            ntake3.insert(END, '7')
        elif noc == 1:
            ntake2.insert(END, '7')

    def c8():
        if noc == 0:
            ntake.insert(END, '8')
        elif noc == 2:

            ntake3.insert(END, '8')
        elif noc == 1:
            ntake2.insert(END, '8')

    def c9():
        if noc == 0:
            ntake.insert(END, '9')
        elif noc == 2:

            ntake3.insert(END, '9')
        elif noc == 1:
            ntake2.insert(END, '9')

    def cspace():
        if noc == 0:
            ntake.insert(END, ' ')
        elif noc == 2:

            ntake3.insert(END, ' ')
        elif noc == 1:
            ntake2.insert(END, ' ')

    def cdel():
        if noc == 0:
            ntake.delete(len(ntake.get()) - 1, END)
        elif noc == 2:

            ntake3.delete(len(ntake3.get()) - 1, END)
        elif noc == 1:
            ntake2.delete(len(ntake2.get()) - 1, END)

    z0 = Button(signwin, text='0', command=c0, bd=3).place(x=320, y=1290)
    z1 = Button(signwin, text='1', command=c1, bd=3).place(x=0, y=1050)
    z2 = Button(signwin, text='2', command=c2, bd=3).place(x=80, y=1050)
    z3 = Button(signwin, text='3', command=c3, bd=3).place(x=160, y=1050)
    z4 = Button(signwin, text='4', command=c4, bd=3).place(x=240, y=1050)
    z5 = Button(signwin, text='5', command=c5, bd=3).place(x=320, y=1050)
    z6 = Button(signwin, text='6', command=c6, bd=3).place(x=400, y=1050)
    z7 = Button(signwin, text='7', command=c7, bd=3).place(x=480, y=1050)
    z8 = Button(signwin, text='8', command=c8, bd=3).place(x=560, y=1050)
    z9 = Button(signwin, text='9', command=c9, bd=3).place(x=640, y=1050)
    a = Button(signwin, text='A', command=ac, bd=3).place(x=0, y=1110)
    b = Button(signwin, text='B', command=bc, bd=3).place(x=80, y=1110)
    c = Button(signwin, text='C', command=cc, bd=3).place(x=160, y=1110)
    d = Button(signwin, text='D', command=dc, bd=3).place(x=240, y=1110)
    e = Button(signwin, text='E', command=ec, bd=3).place(x=320, y=1110)
    f = Button(signwin, text='F', command=fc, bd=3).place(x=400, y=1110)
    g = Button(signwin, text='G', command=gc, bd=3).place(x=480, y=1110)
    h = Button(signwin, text='H', command=hc, bd=3).place(x=560, y=1110)
    i = Button(signwin, text='I', command=ic, bd=3).place(x=640, y=1110)
    j = Button(signwin, text='J', command=jc, bd=3).place(x=0, y=1170)
    k = Button(signwin, text='K', command=kc, bd=3).place(x=80, y=1170)
    l = Button(signwin, text='L', command=lc, bd=3).place(x=160, y=1170)
    m = Button(signwin, text='M', command=mc, bd=3).place(x=240, y=1170)
    n = Button(signwin, text='N', command=nc, bd=3).place(x=320, y=1170)
    o = Button(signwin, text='O', command=oc, bd=3).place(x=400, y=1170)
    p = Button(signwin, text='P', command=pc, bd=3).place(x=480, y=1170)
    q = Button(signwin, text='Q', command=qc, bd=3).place(x=560, y=1170)
    r = Button(signwin, text='R', command=rc, bd=3).place(x=640, y=1170)
    s = Button(signwin, text='S', command=sc, bd=3).place(x=0, y=1230)
    t = Button(signwin, text='T', command=tc, bd=3).place(x=80, y=1230)
    u = Button(signwin, text='U', command=uc, bd=3).place(x=160, y=1230)
    v = Button(signwin, text='V', command=vc, bd=3).place(x=240, y=1230)
    w = Button(signwin, text='W', command=wc, bd=3).place(x=320, y=1230)
    x = Button(signwin, text='X', command=xc, bd=3).place(x=400, y=1230)
    y = Button(signwin, text='Y', command=yc, bd=3).place(x=480, y=1230)
    z = Button(signwin, text='Z', command=zc, bd=3).place(x=560, y=1230)
    space = Button(signwin, text='(space button)', bd=3, command=cspace, width=15).place(x=0, y=1290)
    next = Button(signwin, text='To Next Row', activebackground='skyblue', bd=3, bg='blue', fg='white', command=nex,
                  width=15).place(x=400, y=1290)
    dee = Button(signwin, text='Del', command=cdel).place(x=640, y=1230)

    signwin.mainloop()


# signing process

if mode == 'm':
    signupm()
else:
    signup()

# ============Instruction

i = 1


def instruction():
    iwin = Tk()
    iwin.title('AK Module')
    iwin['bg'] = 'white'
    ilab = Label(iwin, text='Instructions for Quiz', bg='#006666', fg='white', height=2, width=20, bd=10,
                 relief='groove', font=Font(family='bold', size=13, weight='bold', underline=0)).place(x=90, y=80)

    def start():
        iwin.destroy()

    def paging():
        global i, instt, page
        if i == 1:
            instt = Label(iwin, width=32, bg='#336600', fg='white', text=inst5 + inst6 + inst7 + inst8, height=18,
                          font=Font(family='arial', size=9, weight='bold')).place(x=43, y=403)
            i = 2
        else:
            page = Button(iwin, bg='#663300', activebackground='#663300', width=11).place(x=243, y=1130)
            instt = Label(iwin, bg='#336600', fg='white', height=18, width=36).place(x=43, y=403)

            butt = Button(iwin, font=Font(family='arial', size=13, weight='bold'), fg='black', text='START QUIZ', bd=10,
                          relief='solid', height=1, width=11, command=start).place(x=180, y=650)

    inst1 = '1.The Quiz will contain total 10 \nquestions completely based on python\n and each has 15 seconds to solve\n'
    inst2 = '\n2.There will be 4 options and just click on \nthe option and there itself you will\n get to know if it is correct or not\n'
    inst3 = "\n3.If your option is correct it will be \ndisplayed in greenish colour otherwise \nthere will be a red colour on your\n option and the correct one will \nbe displayed in green\n"
    inst4 = '\n4.After clicking an option ,you will\n get to know the correct option'
    inst5 = '5.Then click on the next button \nat bottom right to migrate \nto next question\n'
    inst6 = '\n6.At the end you will get to know \nyour score and it will reach \nme for evaluation for the competition\n'
    inst7 = '\n7.Then you will get a certificate just \nscreenshot it \n'
    inst8 = '\n8. Based on your score ,\nResult will be published on the forum'

    photo = PhotoImage(file='inst2.png')

    ins = Label(iwin, image=photo).place(x=10, y=220)
    instt = Label(iwin, width=32, bg='#336600', fg='white', text=inst1 + inst2 + inst3 + inst4, height=18,
                  font=Font(family='arial', size=9, weight='bold')).place(x=43, y=403)
    i = 1

    page = Button(iwin, text='Next Page', bg='grey', fg='white', activebackground='grey', activeforeground='white',
                  bd=2, relief='groove', width=10, command=paging).place(x=247, y=1130)

    iwin.mainloop()


instruction()

# ============Quiz====

score = 0
lques = ['Q1.  Name the function to find \nabsolute value of a number',
         'Q2. Name the module imported to \nuse load method in binary files',
         'Q3. Which of the following is a \nmembership operator', 'Q4. Give the output\n print(5-1*0+2/2)',
         'Q5.The smallest individual unit in a\n program is known as ',
         'Q6. Which of the following is \nnot a sequence in python',
         'Q7. Give the output \nprint(eval("3")==eval(\'3.0\'))',
         'Q8. Identify the Server side script \nfrom the following',
         'Q9. Which of the following is \nan invalid identifier(literal)?',
         'Q10. Which is the first version \nof Python']

opt = [['a. exact()', 'b. absolute()', 'c. abs()', 'd. exrat()', ('red', 'red', 'green', 'red')],
       ['a. json', 'b. bintrack', 'c. loader', 'd. pickle', ('red', 'red', 'red', 'green')],
       ['a. not in', 'b. is', 'c. ==', 'd. or', ('green', 'red', 'red', 'red')],
       ['a. 6.0', 'b. 4 ', 'c. 4.0', 'd. 6', ('green', 'red', 'red', 'red')],
       ['a. Unitos/unit', 'b. Token/Lexical unit', 'c. Literals', 'd. Objects/Inter', ('red', 'green', 'red', 'red')],
       ['a. array', 'b. range ', 'c. tuple', 'd. set', ('red', 'red', 'red', 'green')],
       ['a. False', 'b. True ', 'c. true', 'd. false', ('red', 'green', 'red', 'red')],
       ['a. Javascript', 'b. vbscript ', 'c. JSP', 'd. Sevscripter', ('red', 'red', 'green', 'red')],
       ['a. Good', 'b. _V7ar_ ', 'c. true', 'd. as', ('red', 'red', 'red', 'green')],
       ['a. 0.1.0', 'b. 0.9.0  ', 'c. 0.0.1', 'd. 1.0.1', ('red', 'green', 'red', 'red')]
       ]

t = 15


def quiz():
    global name, t, mycon, cursor, score, lques, opt
    win = Tk()

    def release():

        global score, t, name
        t = 16
        s(0.22)

        '''if len(lques)==9:
            lques.pop(0)
            opt.pop(0)'''

        if len(lques) == 1:
            cursor.execute('update users set score={} where first="{}"'.format(score, name))
            mycon.commit()
            win.destroy()
        else:
            lques.pop(0)
            opt.pop(0)
            o1['activebackground'] = 'black'
            o1['activeforeground'] = 'white'
            o2['activebackground'] = 'black'
            o2['activeforeground'] = 'white'
            o3['activebackground'] = 'black'
            o3['activeforeground'] = 'white'
            o4['activebackground'] = 'black'
            o4['activeforeground'] = 'white'

            o1['bg'] = 'black'
            o2['bg'] = 'black'
            o3['bg'] = 'black'
            o4['bg'] = 'black'
            q()

    # try

    big = PhotoImage(file='try.png')

    lb = Label(win, image=big)
    lb.place(x=0, y=0)

    qfnt = Font(family='arial', size=10, weight='bold', underline=0)

    score = 0

    def o1c():
        global score
        o1['bg'] = c1

        o1['activebackground'] = c1
        if c1 == 'green':
            score += 1
        elif c2 == 'green':
            o2['bg'] = c2
        elif c3 == 'green':
            o3['bg'] = c3
        else:
            o4['bg'] = c4

        scr['text'] = f'Score:{score}'

    def o2c():
        global score
        o2['bg'] = c2
        o2['activebackground'] = c2
        if c2 == 'green':
            score += 1
        elif c1 == 'green':
            o1['bg'] = c1
        elif c3 == 'green':
            o3['bg'] = c3
        else:
            o4['bg'] = c4
        scr['text'] = f'Score:{score}'

    def o3c():

        global score
        o3['bg'] = c3
        o3['activebackground'] = c3
        if c3 == 'green':
            score += 1
        elif c2 == 'green':
            o2['bg'] = c2
        elif c1 == 'green':
            o1['bg'] = c1
        else:
            o4['bg'] = c4

        scr['text'] = f'Score:{score}'

    def o4c():
        global score
        o4['bg'] = c4
        o4['activebackground'] = c4
        if c4 == 'green':
            score += 1
        elif c2 == 'green':
            o2['bg'] = c2
        elif c3 == 'green':
            o3['bg'] = c3
        else:
            o1['bg'] = c1

        scr['text'] = f'Score:{score}'

    scr = Label(win, text='Score:0', width=7, font=qfnt, bg='black', fg='aqua')
    scr['text'] = f'Score:{score}'
    scr.place(x=560, y=100)
    # 4E74AB

    qlab = Label(win, bg='#454AAE', width=29, fg='white', height=4, font=qfnt, bd=8, relief='raised')
    qlab.place(x=30, y=200)

    o1 = Button(win, width=23, font=('bold', 9), bd=3, bg='black', fg='white', command=o1c)
    o2 = Button(win, width=23, font=('bold', 9), bd=3, bg='black', fg='white', command=o2c)
    o3 = Button(win, width=23, font=('bold', 9), bd=3, bg='black', fg='white', command=o3c)
    o4 = Button(win, width=23, font=('bold', 9), bd=3, bg='black', fg='white', command=o4c)

    o1.place(x=95, y=500)
    o2.place(x=95, y=700)
    o3.place(x=95, y=900)
    o4.place(x=95, y=1100)
    o1['activebackground'] = 'black'
    o1['activeforeground'] = 'white'
    o2['activebackground'] = 'black'
    o2['activeforeground'] = 'white'
    o3['activebackground'] = 'black'
    o3['activeforeground'] = 'white'
    o4['activebackground'] = 'black'
    o4['activeforeground'] = 'white'

    def q():
        global c1, c2, c3, c4

        qlab['text'] = lques[0]
        o1['text'] = opt[0][0]
        o2['text'] = opt[0][1]
        o3['text'] = opt[0][2]
        o4['text'] = opt[0][3]
        c1, c2, c3, c4 = opt[0][4]

    q()

    # next=PhotoImage(file='Im/_next4.png')

    if len(lques) > 2:
        sub = Button(win, relief='raised', bd=7, text='NEXT', bg='blue', activebackground='blue',
                     activeforeground='white', fg='white', command=release, font=('helvertica', 9, 'bold')).place(x=550,
                                                                                                                  y=1200)

    def timer():
        global t, lques, opt
        t -= 1
        s = str(t)
        ti['text'] = s
        if t == -1:
            if len(lques) != 1:
                lques.pop(0)
                opt.pop(0)
            else:
                win.destroy()
            o1['activebackground'] = 'black'
            o1['activeforeground'] = 'white'
            o2['activebackground'] = 'black'
            o2['activeforeground'] = 'white'
            o3['activebackground'] = 'black'
            o3['activeforeground'] = 'white'
            o4['activebackground'] = 'black'
            o4['activeforeground'] = 'white'
            o1['bg'] = 'black'
            o2['bg'] = 'black'
            o3['bg'] = 'black'
            o4['bg'] = 'black'

            q()
            t = 16
            s = 16
            timer()

        else:
            ti.after(1000, timer)

    ti = Label(win, text='15', font=('Helvertica', 10, 'bold'), fg='white', bg='#4E74AB', width=4, height=2, bd=8,
               relief='raised')
    ti.place(x=330, y=75)
    timer()

    win.mainloop()


quiz()

name1 = name + ' ' + last
tik = 20


def result():
    global score, name1

    rwin = Tk()

    def c():
        global name1
        rwin.destroy()

        cer = Tk()

        def exiting():
            t = 15
            try:
                def ex():
                    global tik
                    if tik == 0:
                        cer.destroy()
                    tik -= 1
                    tj[
                        'text'] = f'just take a screenshot of the certificate(after that crop it)\nYou will be leaving from this app UI in {tik} seconds'

                    tj.after(1000, ex)

                tj = Label(cer,
                           text='just take a screenshot of the certificate(after that crop it)\nYou will be leaving from this app UI in 20 seconds',
                           fg="blue", font=Font(family='arial', size=7, weight='bold'))
                tj.place(x=15, y=1150)
                ex()




            except:
                pass

        cer.attributes('-alpha', 0.9)
        im2 = PhotoImage(file="cert.png")

        Label(cer, image=im2).place(x=50, y=150)

        n = len(name1)

        if n > 10 and n <= 15:
            n = 70

        elif n > 15 and n <= 20:
            n = 108

        elif n > 20:
            n = 175

        Label(cer, text=name1.upper(), bg='white', fg="red", font=Font(family='arial', size=11, weight='bold')).place(
            x=290 - n, y=600)

        if score >= 8:
            Label(cer, text='A', bg='#F7F5F6', fg="#505050", font=Font(family='arial', size=6)).place(x=425, y=747)

        elif score >= 5:
            Label(cer, text='B', bg='#F7F5F6', fg="#505050", font=Font(family='arial', size=6)).place(x=425, y=747)

        elif score >= 3:
            Label(cer, text='C', bg='#F7F5F6', fg="#505050", font=Font(family='arial', size=6)).place(x=425, y=747)

        elif score >= 1:
            Label(cer, text='D', bg='#F7F5F6', fg="#505050", font=Font(family='arial', size=6)).place(x=425, y=747)

        else:
            Label(cer, text='E', bg='#F7F5F6', fg="#505050", font=Font(family='arial', size=6)).place(x=425, y=747)

        Button(cer, text='EXIT FROM THE APP', width=16, height=2, fg='white', bg='red', font=('arial', 8, 'bold'),
               activebackground='red', activeforeground='white', command=exiting).place(x=190, y=1200)

        cer.mainloop()

    h = PhotoImage(file='res.png')
    Label(rwin, image=h).place(x=0, y=0)
    Label(rwin, text='-RESULT-', fg='skyblue', bg='white',
          font=Font(family='arial', size=25, weight='bold', underline=1)).place(x=170, y=400)

    im = PhotoImage(file='roun.png')

    Label(rwin, image=im, width=450, bd=18, relief='sunken').place(x=130, y=530)
    Label(rwin, width=13, height=7, bg='#F7F5F6').place(x=250, y=640)
    Label(rwin, text='_____', font=Font(family='arial', size=27, weight='bold'), bg='#F7F5F6', fg='blue').place(x=250,
                                                                                                                y=660)

    if score == 10:
        Label(rwin, text=score, font=Font(family='arial', size=27, weight='bold'), bg='#F7F5F6', fg='blue').place(x=300,
                                                                                                                  y=630)

    else:
        Label(rwin, text=score, font=Font(family='arial', size=27, weight='bold'), bg='#F8F8F8', fg='blue').place(x=325,
                                                                                                                  y=630)

    Label(rwin, text='10', font=Font(family='arial', size=27, weight='bold'), bg='#F8F8F8', fg='blue').place(x=300,
                                                                                                             y=800)

    cert = Button(rwin, text='Tap here for your certificate', bg='black', fg='goldenrod', bd=10, relief='solid',
                  command=c).place(x=140, y=1050)
    rwin.mainloop()


result()

mycon.close()