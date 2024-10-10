from tkinter import *

class MyWindow:
    def __init__(self, win):
        # Common widgets
        self.Label1 = Label(win, fg="Red", text="Calculator", background='black',font=16)
        self.Label1.place(x=150, y=40)

        self.Label2 = Label(win, text="Number 1:",fg="Red",background='black',font=16)
        self.Label2.place(x=50, y=80)
        self.Entry1 = Entry(win, bd=2,font=16)
        self.Entry1.place(x=150, y=80)

        self.Label3 = Label(win, text="Number 2:",fg="Red",background='black',font=16)
        self.Label3.place(x=50, y=120)
        self.Entry2 = Entry(win, bd=2,font=16)
        self.Entry2.place(x=150, y=120)

        self.Label4 = Label(win, text="Result:",fg="Red",background='black',font=16)
        self.Label4.place(x=50, y=160)
        self.Entry3 = Entry(win, bd=2,font=16)
        self.Entry3.place(x=150, y=160)

        self.Button1 = Button(win, fg="Green", text="Add",background='black',font=16 ) #command.add
        self.Button1.place(x=50, y=230)
        self.Button1.bind('<Button-1>',self.add) #alternative

        self.Button2 = Button(win, fg="Green", text="Sub", command=self.subtract,background='black',font=16)
        self.Button2.place(x=140, y=230)

        self.Button3 = Button(win, fg="Green", text="Mul", command=self.multiply,background='black',font=16)
        self.Button3.place(x=230, y=230)

        self.Button4 = Button(win, fg="Green", text="Div", command=self.divide,background='black',font=16)
        self.Button4.place(x=320, y=230)

        self.Button5 = Button(win, fg="Green", text="Clear", command=self.clear, background='black', font=16)
        self.Button5.place(x=180, y=300)

    def add(self,win):
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result = num1 + num2
        self.Entry3.delete(0, END)
        self.Entry3.insert(END, str(result))

    def subtract(self):
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result = num1 - num2
        self.Entry3.delete(0, END)
        self.Entry3.insert(END, str(result))

    def multiply(self):
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result = num1 * num2
        self.Entry3.delete(0, END)
        self.Entry3.insert(END, str(result))

    def divide(self):
        num1 = float(self.Entry1.get())
        num2 = float(self.Entry2.get())
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error"
        self.Entry3.delete(0, END)
        self.Entry3.insert(END, str(result))

    def clear(self):
        self.Entry1.delete(0, END)
        self.Entry2.delete(0, END)
        self.Entry3.delete(0, END)
window = Tk()
MyWin = MyWindow(window)

window.geometry("400x350+10+10")  # Width, height, left, top
window.title("Standard Calculator")
window.configure(bg='White ')
window.mainloop()
