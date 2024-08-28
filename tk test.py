from tkinter import *

def on_enter1(event):
    n = int(input1.get())
    label2.grid(column=0,row=1)
    input2.grid(column=1, row=1)
    input2.bind("<Return>", on_enter2)

def on_enter2(event):
    m = int(input2.get())
    for i in range(m):
        label = Label(text=f"Equation {i+1}")
        label.grid(column=0,row=i+2)

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