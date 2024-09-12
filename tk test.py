from tkinter import *
import numpy as np

global n
m=0



def on_enter1(event):
    n = int(input1.get())
    label2.grid(column=0,row=1)
    input2.grid(column=1, row=1)
    input2.bind("<Return>", on_enter2)

def on_enter2(event):
    m = int(input2.get())
    n = int(input1.get())
    for i in range(m):
        label = Label(text=f"Equation {i+1}")
        label.grid(column=0,row=i+2)
        for j in range(n+1):
            if (j != n):
                label_x = Label(text=f"x{j + 1}*",width=8)
                label_x.grid(column=1 + (j * 2), row=i + 2)
            if(j==n):
                label_x = Label(text="=", width=8)
                label_x.grid(column=1 + (j * 2), row=i + 2)
            input = Entry(width="10")
            input.grid(column = 2+(j*2),row=i+2)




window = Tk()
window.title("Gauss Elimination")
window.config(padx = 100,pady=60)

label1=Label(text="Enter the number of variables:")
label1.grid(column=0,row=0)

input1 = Entry()
input1.grid(column=1,row=0)
input1.bind("<Return>", on_enter1)

label2=Label(text="Enter the number of equations:")

input2 = Entry()

window.mainloop()