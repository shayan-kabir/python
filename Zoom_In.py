from tkinter import *

global root
root = Tk()
root.title("Search And Sort")
root.geometry("800x600")
root.configure(bg="#21243B")

global interval
global txt

txt = Label(root, text="this is linear search", font=("TkDefaultFont", 12))
txt.place(x=100, y=200)


def zoom_in():
    new_size = 0
    current_size = txt.cget("font").split()[1]
    print(txt.cget("font").split())
    new_size = int(current_size) + 2
    print(new_size)
    if new_size > 22:
        Zoom_in.place_forget()
        Zoom_out.place(x=400, y=200) 
    txt.config(font=("TkDefaultFont", new_size))

def zoom_out():
    new_size = 0
    current_size = txt.cget("font").split()[1]
    print(txt.cget("font").split())
    new_size = int(current_size) - 2
    print(new_size)
    if new_size < 6:
        Zoom_out.place_forget()
        Zoom_in.place(x=400, y=100)
    txt.config(font=("TkDefaultFont", new_size))



Zoom_in = Button(root, text="+", font=40, command=zoom_in)
Zoom_in.place(x=400, y=100)


Zoom_out = Button(root, text="-", font=40, command=zoom_out)
Zoom_out.place(x=400, y=200)

root.mainloop()




