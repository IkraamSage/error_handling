from tkinter import *
from tkinter import messagebox
# initializing the gui
window = Tk()
window.config(bg="red")
window.title("Trip")
window.geometry("300x300")

# making lbl placement
lblamount = Label(window, text="Please enter amount in your account:", bg="red")
lblamount.place(x=20, y=50)
txtamount = Entry(window)
txtamount.place(x=60, y=80)

# giving a function for the trip


def qualify():
    try:
        money = float(txtamount.get())
        if money < 3000:
            messagebox.showerror("Insufficient funds", "Please deposit more funds for this excursion.")
            txtamount.delete(0, END)
        else:
            messagebox.showinfo("Accepted", "Congratulations. You qualify to go to Malaysia")
            txtamount.delete(0, END)
    except ValueError:
        messagebox.showerror("Invalid", "Please put in an amount in numbers.")
        txtamount.delete(0, END)


enter = Button(window, text="Check qualification", bg="white", command=qualify)
enter.place(x=60, y=120)

# defining clear button


def clear():
    txtamount.delete(0, END)


def close():
    window.destroy()


clear_btn = Button(window, text="Clear", bg="white", command=clear)
clear_btn.place(x=60, y=180)

exit_btn = Button(window, text="Exit", bg="white", command=close)
exit_btn.place(x=160, y=180)

window.mainloop()
