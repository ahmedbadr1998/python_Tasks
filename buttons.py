
import tkinter as tk

def myname():
    print("my name is Ahmed")
window=tk.Tk()
window.geometry("500x500")
button_coords = [
    (50, 100),   # Top button
    (100, 150),  # Right button
    (50, 200),   # Bottom button
    (0, 150)     # Left button
]
# some widget
up=tk.Button(window,text="print",width=10,command=myname)
right=tk.Button(window,text="print",width=10,command=myname)
left=tk.Button(window,text="print",width=10,command=myname)
bottom=tk.Button(window,text="print",width=10,command=myname)
# positioning
up.place(x=button_coords[0][0]+150,y=button_coords[0][1]+50)
right.place(x=button_coords[1][0]+150,y=button_coords[1][1]+50)
left.place(x=button_coords[2][0]+150,y=button_coords[2][1]+50)
bottom.place(x=button_coords[3][0]+150,y=button_coords[3][1]+50)

window.mainloop()


