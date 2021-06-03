from tkinter import *
from tkinter import messagebox


# initializing the gui
root = Tk()
root.title('Login')
root.geometry('400x200')
root.config(bg='red')

# giving the labels
lb1 = Label(root, text="Username", bg='red')
lb1.place(x=10, y=10)
lb2 = Label(root, text="Password", bg='red')
lb2.place(x=10, y=50)


# giving the entries
entry1 = Entry(root)
entry1.place(x=160, y=10)
entry2 = Entry(root)
entry2.place(x=160, y=50)


user_pass = {'ikraam': 'sage', 'naeemah': 'davis', 'brent': 'johnson',
             'yamkhela': 'bread'}

# giving the exit button a function


def delete():
    entry1.delete(0, 'end')
    entry2.delete(0, 'end')
# giving the login a function


def login():
    if entry1.get() in user_pass:
        if entry2.get() == user_pass[entry1.get()]:
            root.destroy()
            import trip
        else:
            messagebox.showerror(message="Username and password does not match")
    else:
        messagebox.showerror(message="Username does not exist")


# giving buttons placement and commands
btn1 = Button(root, text="Verify", command=login)
btn1.place(x=50, y=150)
btn1.config(bg='yellow')
btn2 = Button(root, text="Clear", command=delete)
btn2.place(x=150, y=150)
btn2.config(bg='yellow')
btn3 = Button(root, text="Exit", command="exit")
btn3.place(x=250, y=150)
btn3.config(bg='yellow')


root.mainloop()
