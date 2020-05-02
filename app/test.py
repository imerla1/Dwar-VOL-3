from tkinter import *
from functools import partial


OPTIONS = [
"Farm",
"Fight",
"New Super Udar",
"profession craft"
]  # etc

def validateLogin(username, password):
	print("Username:", username.get())
	print("Password.get", password.get())
	print(variable.get())
# PanedWindow
tkWindow = Tk()  
tkWindow.geometry('250x150')  
tkWindow.title('Dwar Login Form')

# username label and text entry box
usernameLabel = Label(tkWindow, text="dwar email").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)  

# password label and password entry box
passwordLabel = Label(tkWindow,text="Password").grid(row=1, column=0)  
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)  
# Game Mode
passwordLabel = Label(tkWindow,text="Game Mode").grid(row=2, column=0) 
variable = StringVar(tkWindow)
variable.set(OPTIONS[0]) # Default Value For Dropdwon
w = OptionMenu(tkWindow, variable, *OPTIONS).grid(row=2, column=1)


validateLogin = partial(validateLogin, username, password)

# login button
loginButton = Button(tkWindow, text="Login", command=validateLogin).grid(row=5, column=1)  

tkWindow.mainloop()
