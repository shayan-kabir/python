from tkinter import *
global root
root = Tk() # Creating an instance
root.title("Search And Sort") # The name of the GUI
root.geometry("800x600") # The size of the GUI
root.configure(bg="#21243B") # Background colour of the GUI
global interval
global txt
interval = 0

#Radiobuttons
r= IntVar()
r.set("1")
Radiobutton1 = Radiobutton(root, text ="Linear", variable = r, value =1, font =20)
Radiobutton1.place(x=100,y=100)

Radiobutton1.place_forget()



Radiobutton2 = Radiobutton(root, text ="Binary", variable = r, value =2, font =20)
Radiobutton2.place(x=600,y=100)

Radiobutton2.place_forget()

#Entry Widgets
widget = Entry(root, font =40)
widget.place(x=400,y=200)

widget.place_forget()

widget2 = Entry(root, font =40)
widget2.place(x=400,y=300)

widget2.place_forget()

#Labels
label = Label(root, text='Menu', fg='black', bg='blanched almond', font = ('Aerial bold',40), width=26, height=1).place(x=0,y=0)

option = Label(root, text='Please select one', fg='black', bg='blanched almond', font = ('Aerial',25))
option.place(x=265,y=220)


txt = Label(root, text = "this is linear search", relief = RAISED)

Sort = Button(root, text='Sort', fg='black', bg='#e6e6e6', font=('Times', 20), width=15,)
Sort.place(x=130,y=350)

enter_arr = Label(root, text = "Enter Array",font =60)
enter_arr.place(x=200,y=200)

enter_arr.place_forget()

enter_item = Label(root, text = "Enter Search item",font =60)
enter_item.place(x=185,y=300)

enter_item.place_forget()



def click_search():
    global interval
    if interval ==1:
        txt.place_forget()
        Sort.place(x=130,y=350)
        enter_arr.place_forget()
        option.place(x=265,y=220)
        widget.place_forget()
        widget2.place_forget()
        enter_item.place_forget()
        Radiobutton1.place_forget()
        Radiobutton2.place_forget()
        Search.place(x=400,y=350,)
        interval = 0
    elif interval == 0:
        txt.place(x=350,y=500)
        option.place_forget()
        Sort.place_forget()
        Search.place_forget()
        enter_arr.place(x=200,y=200)
        widget.place(x=400,y=200)
        widget2.place(x=400,y=300)
        enter_item.place(x=197,y=300)
        Radiobutton1.place(x=200,y=100)
        Radiobutton2.place(x=500,y=100)
        interval = 1

Menu = Button(root, text = "Menu", command = click_search)
Menu.place(x=20, y=560)






        

Search = Button(root, text='Search', fg='black', bg='#e6e6e6', font=('Times', 20),command = click_search, width=15)
Search.place(x=400,y=350,)










info = Button(root, text='info',fg='black', bg='blanched almond', font = ('Aerial',20)).place(x=725,y=525)

mainloop()



#fr
