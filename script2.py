from tkinter import *

window=Tk()

def lbs_conversion():
    kilogram=float(e1_value.get())*.45359237
    t1.insert(END,kilogram)
    ounces=float(e1_value.get())*16
    t2.insert(END,ounces)
    grams=float(e1_value.get())*.00220462262185
    t3.insert(END,grams)

b1=Button(window,text="Convert",command=lbs_conversion)
b1.grid(row=0,column=2)

e1_value=StringVar()
e1=Entry(window,textvariable=e1_value)
e1.grid(row=0,column=3)

w1=Label(window, text="Pounds")
w1.grid(row=0,column=4)

w2=Label(window, text="Kg")
w2.grid(row=2,column=2)

w3=Label(window, text="Ounces")
w3.grid(row=2,column=3)

w4=Label(window, text="Grams")
w4.grid(row=2,column=4)

w5=Label(window, text="")
w5.grid(row=1,column=3)

t1=Text(window,height=1,width=30)
t1.grid(row=3,column=2)

t2=Text(window,height=1,width=30)
t2.grid(row=3,column=3)

t3=Text(window,height=1,width=30)
t3.grid(row=3,column=4)

window.mainloop()
