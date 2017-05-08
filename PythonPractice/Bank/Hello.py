class currentCustomer:
    def __init__(self, username, password, balance):
        self.username = username
        self.password = password
        self.balance = balance

def login():
    file = open('Customers.txt','r')
    found = False
    lines = file.readlines()
    x = 0
    for line in lines:
        line = line.rstrip('\n')
        if (userName.get() + '' + password.get()) == line:
            found = True
            currentB = lines[x+1]
        x=x+1
    if found:
        destroyWidgets()
        createLoggedIn(currentB)
    else:
        print('Unable to log you in')
    file.close()

def create():
    file = open("Customers.txt","a")
    file.write(userName.get())
    file.write(password.get()+"\n")
    file.write("0\n")
    file.close()

def Clear():
    file = open("Customers.txt","w")
    file.write('')

def destroyWidgets():
    for widget in top.winfo_children():
            widget.destroy()

def createLoggedIn(b):
    money = Text(top)
    money.insert(INSERT, "Balance: ")
    money.insert(END, b)
    money.pack()
    withdraw = tkinter.Button(top, text="Withdraw", command = Withdraw)
    withdraw.pack()

def Withdraw():
    print('Im supposed to withdraw')
    

import tkinter
from tkinter import *
balance = 0
top = tkinter.Tk()
L1 = Label(top, text="User Name")
L1.pack()
userName = Entry(top, bd=5)
userName.pack()
L2 = Label(top, text="Password")
L2.pack()
password = Entry(top, bd=5)
password.pack()

create = tkinter.Button(top, text="Create", command = create)
create.pack()

login = tkinter.Button(top, text="Login", command = login)
login.pack()

clearUsers = tkinter.Button(top, text="Clear Users", command = Clear)
clearUsers.pack()
top.mainloop()
