from tkinter import *
global root
root = Tk() # Creating an instance
root.title("Search And Sort") # The name of the GUI
root.geometry("800x600") # The size of the GUI
root.configure(bg="#21243B") # Background colour of the GUI
global interval
global txt
interval = 0




#Radiobuttons (Search)
r= IntVar()
r.set("1")
Radiobutton1 = Radiobutton(root, text ="Linear", variable = r, value =1, font =20)
Radiobutton1.place(x=100,y=100)

Radiobutton1.place_forget()



Radiobutton2 = Radiobutton(root, text ="Binary", variable = r, value =2, font =20)
Radiobutton2.place(x=600,y=100)

Radiobutton2.place_forget()

#Radiobuttons (Sort)
V = IntVar()
V.set("1")

Radiobutton3 = Radiobutton(root, text ="Selection", variable = r, value =1, font =20)

Radiobutton3.place_forget()

Radiobutton4 = Radiobutton(root, text ="Bubble", variable = r, value =2, font =20)

Radiobutton4.place_forget()

Radiobutton5 = Radiobutton(root, text ="Insertion", variable = r, value =3, font =20)
Radiobutton5.place(x=500,y=100)

Radiobutton5.place_forget()


Ascending =  Radiobutton(root, text ="Ascending", variable = V, value =1, font =20)
Ascending.place(x=197,y=280)
Ascending.place_forget()

Descending =  Radiobutton(root, text ="Descending", variable = V, value =2, font =20)
Descending.place(x=197,y=330)
Descending.place_forget()


#Entry Widgets
Enter_arr_sort = Entry(root, font =40, fg="dark blue")
Enter_arr_sort.place(x=400,y=200)

Enter_arr_sort.place_forget()

Enter_arr_search = Entry(root, font =40, fg="dark blue")
Enter_arr_search.place(x=400,y=200)

Enter_arr_search.place_forget()

Enter_searchitem = Entry(root, font =40, fg = "red")
Enter_searchitem.place(x=400,y=300)

Enter_searchitem.place_forget()

#Labels
menu_label = Label(root, text='Menu', fg='black', bg='blanched almond', font = ('Aerial bold',40), width=26, height=1).place(x=0,y=0)

option = Label(root, text='Please select one', fg='black', bg='blanched almond', font = ('Aerial',25))
option.place(x=265,y=220)

search_label = Label(root, text='Searches', fg='black', bg='blanched almond', font = ('Aerial bold',40), width=26, height=1)
search_label.place(x=0,y=0)
search_label.place_forget()

sort_label = Label(root, text='Sorts', fg='black', bg='blanched almond', font = ('Aerial bold',40), width=26, height=1)
sort_label.place(x=0,y=0)
sort_label.place_forget()

sorted_arr =  Label(root, text= "Sorted Array is: ", fg='black', bg='blanched almond', font = ('Aerial',15))

sorted_arr.place_forget()

search = Label(root, text= "Position of the search item is: ", fg='black', bg='blanched almond', font = ('Aerial',15))

search.place_forget()



#Search options


enter_arr = Label(root, text = "Enter Array",font =("Arial",30))


enter_arr.place_forget()

enter_item = Label(root, text = "Enter Search Item",font =("Arial",30))


enter_item.place_forget()


#Sort options

enter_arr2 = Label(root, text = "Enter Array",font =80)


enter_arr2.place_forget()


order_selection = Label(root, text = "Select Order",font =80)


order_selection.place_forget()



#Define functions

def click_search():
    global interval
    if interval ==1:
        SEARCH.place_forget()
        search.place_forget()
        Sort.place(x=130,y=350)
        enter_arr.place_forget()
        option.place(x=265,y=220)
        Enter_arr_search.place_forget()
        Enter_searchitem.place_forget()
        enter_item.place_forget()
        Radiobutton1.place_forget()
        Radiobutton2.place_forget()
        Search.place(x=400,y=350,)
        search_label.place_forget()
        Menu.place_forget()
        result_label.place_forget()
        interval = 0
    elif interval == 0:
        SEARCH.place(x=200, y=400)
        search.place(x=200, y=450)
        option.place_forget()
        Sort.place_forget()
        Search.place_forget()
        enter_arr.place(x=100,y=180)
        Enter_arr_search.place(x=500,y=195)
        Enter_searchitem.place(x=500,y=290)
        enter_item.place(x=100,y=280)
        Radiobutton1.place(x=200,y=100)
        Radiobutton2.place(x=500,y=100)
        search_label.place(x=0,y=0)
        Menu.place(x=20, y=540)
        result_label.place(x=300, y=410)
        interval = 1


def click_sort():
    global interval
    if interval ==1:
        enter_arr.place_forget()
        SORT.place_forget()
        sorted_arr.place_forget()
        Sort.place(x=130,y=350)
        Enter_arr_sort.place_forget()
        option.place(x=265,y=220)
        order_selection.place_forget()
        Radiobutton3.place_forget()
        Radiobutton4.place_forget()
        Radiobutton5.place_forget()
        Search.place(x=400,y=350,)
        Ascending.place_forget()
        Descending.place_forget()
        sort_label.place_forget()
        Menu2.place_forget()
        interval = 0
        result_label.place_forget()
    elif interval == 0:
        enter_arr.place(x=200,y=200)
        SORT.place(x=200, y=450)
        sorted_arr.place(x=200, y=400)
        option.place_forget()
        Sort.place_forget()
        Search.place_forget()
        Enter_arr_sort.place(x=400,y=200)
        order_selection.place(x=197,y=300)
        Radiobutton3.place(x=100,y=100)
        Radiobutton4.place(x=350,y=100)
        Radiobutton5.place(x=600,y=100)
        Ascending.place(x=450,y=260)
        Descending.place(x=450,y=320)
        Menu2.place(x=20, y=540)
        sort_label.place(x=0,y=0)
        interval = 1


def linear_search():
    input_text = Enter_arr_search.get()
    numbers = input_text.split()  # Split the input text using space as the delimiter

    try:
    
        numbers = [int(num) for num in numbers]  # Convert the numbers from strings to integers
        
        search_item = int(Enter_searchitem.get())  # Get the search item as an integer
        
        index = -1  #if the search item is not found after iterating through the entire array, the value of index remains as -1.
        for i, num in enumerate(numbers):  #enumerate retrieves both the value and the index whilst iterating the list 
            if num == search_item:
                index = i
                break
        
        if index != -1:
            result_label.config(text=f"Search item found at index: {index}")   #f" f strings are used so that different type of data can be used in a sentence
        else:
            result_label.config(text="Search item not found")
    except ValueError:
        result_label.config(text="Invalid input")



result_label = Label(root,bg="#21243B",fg = "white")
result_label.place(x=400, y=500)
result_label.place_forget()

 

#Search or Sort option

Sort = Button(root, text='Sort', fg='black', bg='#e6e6e6', font=('Times', 20), width=15,command = click_sort )
Sort.place(x=130,y=350)

Search = Button(root, text='Search', fg='black', bg='#e6e6e6', font=('Times', 20),command = click_search, width=15)
Search.place(x=400,y=350)

#Different Menu for disparate options

Menu = Button(root, text = "Menu", command = click_search, font =40 )
Menu.place_forget()

Menu2 = Button(root, text = "Menu", command = click_sort, font =40)
Menu2.place_forget()

#Buttons requiring commands 

SEARCH = Button(root, text= "Search ", fg='black', bg='blanched almond', font = ('Aerial',15), command = linear_search)
SEARCH.place(x=200, y=450)
SEARCH.place_forget()


SORT = Button(root, text= "Sort ", fg='black', bg='blanched almond', font = ('Aerial',15))
SORT.place(x=200, y=450)
SORT.place_forget()




info = Button(root, text='info',fg='black', bg='blanched almond', font = ('Aerial',20)).place(x=725,y=525)

mainloop()




