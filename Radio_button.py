
import tkinter as tk

def myfun():
    global var
    option=var.get()
    x=ent1.get()
    y=ent2.get()
    x=int(x)
    y=int(y)
    if option==1:
        z=x+y
        res.config(text="the result : "+str(z))
    elif option==2:
        z=x-y 
        res.config(text="the result : "+str(z))   
    



window=tk.Tk()
window.title("arithmatic")
window.geometry("500x500")
# for RadioButton


var=tk.IntVar()
rx=tk.Radiobutton(window,text='SUM',variable=var,value=1)
ry=tk.Radiobutton(window,text='SUB',variable=var,value=2)
rx.place(x=5,y=350)
ry.place(x=5,y=400)

# for button

button=tk.Button(window,text="GET",width=30,command=myfun)
button.place(x=150,y=300)


# for labels

lbl1=tk.Label(window,text="Enter the value of M",font=("arial","15"))
lbl2=tk.Label(window,text="Enter the value of N",font=("arial","15"))
lbl1.grid(row=0,column=0)
lbl2.grid(row=1,column=0)

# for entery
ent1=tk.Entry(window)
ent2=tk.Entry(window)
ent1.grid(row=0,column=1)
ent2.grid(row=1,column=1)

# for label
res=tk.Label(window,text="",font=("Arial","15"))
res.place(x=150,y=150)
window.mainloop()
