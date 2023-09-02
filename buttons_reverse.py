
import tkinter as tk

def reverse_string():
    str_gen= entry.get()[::-1]
    label.config(text=str_gen)



window=tk.Tk()
window.title("task")
window.geometry("300x200")


lbl=tk.Label(window,text="enter")
lbl.grid(row=0,column=0)

entry=tk.Entry(window)

entry.grid(row=0,column=1)


buttton=tk.Button(window,text="Validate",width=10,font=("Arial"),command=reverse_string)
buttton.grid(row=3)
label = tk.Label(window,text="")
label.grid(row=3,column=1)
window.mainloop()
