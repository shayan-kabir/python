from tkinter import *
import math
global root
root = Tk() # Creating an instance
root.title("Search And Sort") # The name of the GUI
root.geometry("800x700") # The size of the GUI
root.configure(bg="#21243B") # Background colour of the GUI
global interval
global variable 
global txt
interval = 0
resultText =StringVar


#Switching Buttons based on the radiobuttons choice (Search)


def switch_to_binary():
    
    SEARCH_linear.place_forget()
    SEARCH_binary.place(x=200,y=400)

def switch_to_linear():
    SEARCH_binary.place_forget()
    SEARCH_linear.place(x=200,y=400)

#Switching Buttons based on the radiobuttons choice (Sort)


def switch_to_selection():
    SORT_selection.place(x=200, y=450)
    SORT_insertion.place_forget()
    SORT_bubble.place_forget()



def switch_to_bubble():
    
    SORT_selection.place_forget()
    SORT_insertion.place_forget()
    SORT_bubble.place(x=200, y=450)


def switch_to_insertion():
    SORT_selection.place_forget()
    SORT_bubble.place_forget()
    SORT_insertion.place(x=200, y=450)
    



#Radiobuttons (Search)
r = IntVar()
r.set("1")
Radiobutton1 = Radiobutton(root, text ="Linear", variable = r, value =int(1), font =20, comman = switch_to_linear)
Radiobutton1.place(x=100,y=100)

Radiobutton1.place_forget()



Radiobutton2 = Radiobutton(root, text ="Binary", variable = r, value =int(2), font =20, command =switch_to_binary)
Radiobutton2.place(x=600,y=100)

Radiobutton2.place_forget()

#Radiobuttons (Sort)
v = IntVar()
v.set("1")

h = IntVar()
h.set("1")

Radiobutton3 = Radiobutton(root, text ="Selection", variable = v, value =int(1), font =20, command = switch_to_selection )

Radiobutton3.place_forget()

Radiobutton4 = Radiobutton(root, text ="Bubble", variable = v, value =int(2), font =20, command =switch_to_bubble)

Radiobutton4.place_forget()

Radiobutton5 = Radiobutton(root, text ="Insertion", variable = v, value =int(3), font =20, command = switch_to_insertion)
Radiobutton5.place(x=500,y=100)

Radiobutton5.place_forget()


Ascending =  Radiobutton(root, text ="Ascending", variable = h, value =1, font =20)
Ascending.place(x=197,y=280)
Ascending.place_forget()

Descending =  Radiobutton(root, text ="Descending", variable = h, value =2, font =20)
Descending.place(x=197,y=330)
Descending.place_forget()


#Entry Widgets
Enter_arr_sort = Entry(root, font =50, fg="dark blue")
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


order_selection = Label(root, text = "Select Order",font =("Arial",30))


order_selection.place_forget()



#Define functions

def click_search():
    global interval
    global variable
    variable = 1
    print(variable)
    if interval ==1:
        #pressing menu 
        SEARCH_linear.place_forget()
        SEARCH_binary.place_forget()
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
        Enter_searchitem.delete(0,100)
        Enter_arr_search.delete(0,100)
        result_label.config(text="")
        clear_search.place_forget()
        search_info.place_forget()
        MainInfo.place(x=725, y =625)
        SearchInfo.place_forget()
        interval = 0
    elif interval == 0:
        #pressing Search
        r.set("1")
        Enter_searchitem.get()==""    # ?
        SEARCH_linear.place(x=200, y=400)
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
        Menu.place(x=20, y=640)
        result_label.place(x=500, y=450)
        clear_search.place(x=722, y=500)
        SearchInfo.place(x=625,y=625)
        MainInfo.place_forget()
        search_info.place_forget()
        main_info.place_forget()
        SearchInfo.place(x=625,y=625)
        interval = 1


def click_sort():
    global interval
    global variable
    variable = 1
    print(variable)
    if interval ==1:
        #pressing menu
        Enter_arr_sort.delete(0,100)
        result_label_sort.place_forget()
        enter_arr.place_forget()
        SORT_selection.place_forget()
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
        result_label.place_forget()
        result_label_sort.config(text="")
        SORT_bubble.place_forget()
        SORT_insertion.place_forget()
        clear_sort.place_forget()
        SortInfo.place_forget()
        MainInfo.place(x=725, y =625)
        sort_info.place_forget()
        search_info.place_forget()
        interval = 0
        
    elif interval == 0:
        #pressing sort
        Enter_arr_sort.get()==""
        v.set("1")
        enter_arr.place(x=100,y=200)
        SORT_selection.place(x=200, y=450)
        sorted_arr.place(x=200, y=400)
        option.place_forget()
        Sort.place_forget()
        Search.place_forget()
        Enter_arr_sort.place(x=400,y=200)
        order_selection.place(x=100,y=300)
        Radiobutton3.place(x=100,y=100)
        Radiobutton4.place(x=350,y=100)
        Radiobutton5.place(x=600,y=100)
        Ascending.place(x=450,y=280)
        Descending.place(x=450,y=340)
        Menu2.place(x=20, y=640)
        sort_label.place(x=0,y=0)
        clear_sort.place(x=722, y=500)
        SortInfo.place(x=655,y=625)
        MainInfo.place_forget()
        main_info.place_forget()
        interval = 1


# Search functionalities 

def linear_search():
    if r.get()==1:
        input_text = Enter_arr_search.get()
        numbers = input_text.split()  # Split the input text using space as the delimiter

        input_text2 = Enter_searchitem.get()
        numbers2 = input_text2.split()

        
        #search_item = int(Enter_searchitem.get())



        if len(numbers) == 0 or len(numbers2) == 0: # Error checking for if users do not input a value
                result_label_sort.config(text="No numbers entered")
                result_label_sort.place(x=400, y=410) 
                return


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

            



    
        
def binary_search():
    
    input_text = Enter_arr_search.get()
    numbers = input_text.split()  # Split the input text using space as the delimiter
    
    Beg = 0
    End = len(numbers)
    Mid = int((Beg + End)/2)

   
    numbers = [int(num) for num in numbers]  # Convert the numbers from strings to integers
    sorted_numbers = sorted(numbers)
    print(sorted_numbers)
    search_item = int(Enter_searchitem.get())  # Get the search item as an integer

    if search_item == numbers[Beg]:
        result_label.config(text=f"Search item found at index: {Beg}")
        return
        
 
    while Beg <= End:
        Mid = (Beg + End) // 2  # Compute the midpoint

        if sorted_numbers[Mid] == search_item:
            result_label.config(text=f"Search item found at index: {Mid}")
            return
        elif sorted_numbers[Mid] < search_item:
            Beg = Mid + 1  # Update the beginning index
        else:
            End = Mid - 1  # Update the ending index

    result_label.config(text="Search item not found")  
   
        
# Sort functionalities


def selection():
    input_text = Enter_arr_sort.get()
    numbers = input_text.split()
    
    try:
        numbers = [int(num) for num in numbers]  # Convert the numbers from strings to integers
        
        if len(numbers) == 0: # Error checking for if users do not input a value
            result_label_sort.config(text="No numbers entered")
            result_label_sort.place(x=400, y=410) 
            return
        
        length = len(numbers)
        i = 1
        for i in range(length):
            if h.get()==1:
                min_index = i
                for j in range(i + 1, length):
                    if numbers[j] < numbers[min_index]:
                        min_index = j
                numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
            elif h.get()==2:
                min_index = i
                for j in range(i + 1, length):
                    if numbers[j] > numbers[min_index]:
                        min_index = j
                numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

        result_label_sort.config(text=f"Sorted Array is: {numbers}")
        result_label_sort.place(x=400, y=410)
    except ValueError:  # Error check for non numeric entries 
        result_label_sort.config(text="Invalid input (non-numeric value entered)")
        result_label_sort.place(x=400, y=410)
     



def bubble():
    input_text = Enter_arr_sort.get()
    numbers = input_text.split()  

    try:
        numbers = [int(num) for num in numbers]  # Convert the numbers from strings to integers
        length = len(numbers)
        
        if len(numbers) == 0: # Error checking for if users do not input a value
            result_label_sort.config(text="No numbers entered")
            result_label_sort.place(x=400, y=410) 
            return
        
        for i in range(length):
            Swapped = False
            for j in range(length-1):
                if h.get()==1:
                    if numbers[j] > numbers[j+1]:
                        Temp = numbers[j]
                        numbers[j] = numbers[j+1]
                        numbers[j+1] = Temp
                        Swapped = True
                        if Swapped == False: 
                            Break
                elif h.get()== 2 :
                    if numbers[j] < numbers[j+1]:
                        Temp = numbers[j]
                        numbers[j] = numbers[j+1]
                        numbers[j+1] = Temp
                        Swapped = True
                        if Swapped == False: 
                            Break

        
        result_label_sort.config(text=f"Sorted Array is: {numbers}")
        result_label_sort.place(x=400, y=410)
    except ValueError:  # Error check for non numeric entries 
        result_label_sort.config(text="Invalid input (non-numeric value entered)")
        result_label_sort.place(x=400, y=410)




def insertion():
    input_text = Enter_arr_sort.get()
    numbers = input_text.split()

    try:
        numbers = [int(num) for num in numbers]  # Convert the numbers from strings to integers
        length = len(numbers)

        if len(numbers) == 0: # Error checking for if users do not input a value
            result_label_sort.config(text="No numbers entered")
            result_label_sort.place(x=400, y=410) 
            return
        
        i = 1

        if h.get()==1:
            for i in range(length):
                print("hello")
                value = numbers[i]
                j = i - 1
                while j>=0 and numbers[j]> value:
                    numbers[j+1] = numbers[j]
                    j = j - 1
                numbers[j+1] = value
        if h.get()==2:
            for i in range(length):
                print("hello")
                value = numbers[i]
                j = i - 1
                while j>=0 and numbers[j]< value:
                    numbers[j+1] = numbers[j]
                    j = j - 1
                numbers[j+1] = value
        


         
        result_label_sort.config(text=f"Sorted Array is: {numbers}")
        result_label_sort.place(x=400, y=410)


    except ValueError:  # Error check for non numeric entries 
        result_label_sort.config(text="Invalid input (non-numeric value entered)")
        result_label_sort.place(x=400, y=410)
        
        


# Clear functionalities

def clear_search():
    result_label.config(text="")
    Enter_searchitem.delete(0,100)
    Enter_arr_search.delete(0,100)
    

def clear_sort():
    result_label_sort.config(text="")
    Enter_arr_sort.delete(0,100)






result_label_sort = Label(root, bg="#21243B", fg="white", font=10)





# Search or Sort option (Main Menu)

Sort = Button(root, text='Sort', fg='black', bg='#e6e6e6', font=('Times', 20), width=15,command = click_sort)
Sort.place(x=130,y=350)

Search = Button(root, text='Search', fg='black', bg='#e6e6e6', font=('Times', 20),command = click_search, width=15)
Search.place(x=400,y=350)

# Different Menu for disparate options

Menu = Button(root, text = "Menu", command = click_search, font =40 )
Menu.place_forget()

Menu2 = Button(root, text = "Menu", command = click_sort, font =40)
Menu2.place_forget()

# Buttons requiring commands (Search)

SEARCH_linear = Button(root, text= "Search with linear", fg='black', bg='Orange', font = ('Aerial',15), command = linear_search)
SEARCH_linear.place(x=200, y=450)
SEARCH_linear.place_forget()

SEARCH_binary = Button(root, text= "Search with binary", fg='black', bg='Orange', font = ('Aerial',15), command = binary_search)
SEARCH_binary.place(x=200,y=450)
SEARCH_binary.place_forget()

# Buttons requiring commands (Sort)


SORT_selection = Button(root, text= "Sort with Selection ", fg='black', bg='Orange', font = ('Aerial',15), command = selection)
SORT_selection.place_forget()

SORT_bubble =  Button(root, text= "Sort with Bubble ", fg='black', bg='Orange', font = ('Aerial',15), command = bubble)
SORT_bubble.place_forget()

SORT_insertion =  Button(root, text= "Sort with Insertion ", fg='black', bg='Orange', font = ('Aerial',15), command = insertion)
SORT_insertion.place_forget()

# Search result Label

result_label = Label(root,bg="#21243B",fg = "white", font =10)
result_label.place(x=500, y=510)
result_label.place_forget()





# Clear buttons

clear_search = Button(root, text= "Clear ", fg='black', bg='light blue', font = 5, command = clear_search)
clear_search.place(x=722, y=500)
clear_search.place_forget()


clear_sort = Button(root, text= "Clear", fg='black', bg='light blue', font = 5,  command = clear_sort )
clear_sort.place(x=722, y=500)
clear_sort.place_forget()



# info labels and its corresponding buttons with functions

variable = 1
def infoMain():
    global variable
    if variable == 1:
        main_info.place(x=150, y = 600)
        variable =0
    elif variable == 0:
        main_info.place_forget()
        variable = 1

def infoSearch():
    global variable
    if variable == 1:
        search_info.place(x=150, y = 600)
        variable =0
    elif variable == 0:
        search_info.place_forget()
        variable = 1

def infoSort():
    global variable
    if variable == 1:
        sort_info.place(x=150, y = 600)
        variable =0
    elif variable == 0:
        sort_info.place_forget()
        variable = 1
    

main_info = Label(root, text = "This is a search and sort application. \n Please select either search and select to use the feature", font = 5)
main_info.place(x=150, y = 600)
main_info.place_forget()

MainInfo = Button(root, text='info',fg='black', bg='blanched almond', font = ('Aerial',20), command = infoMain)
MainInfo.place(x=725,y=625)



SearchInfo = Button(root, text='Search info',fg='black', bg='blanched almond', font = ('Aerial',20), command = infoSearch)
SearchInfo.place(x=625,y=625)
SearchInfo.place_forget()

search_info = Label(root, text = "This is a search stuff", font = 5)




SortInfo = Button(root, text='Sort info',fg='black', bg='blanched almond', font = ('Aerial',20), command = infoSort)
SortInfo.place(x=625,y=625)
SortInfo.place_forget()

sort_info = Label(root, text = "This is a Sort stuff", font = 5)



mainloop()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------






#Selection




#Bubble


         
    
def bubble():
        array = [14, 33, 27, 35, 10]
n = len(array)
i = 0
for i in range(n):
    Swapped = False 
    for j in range(n - 1): 
    #Compare the adjacent elements
        if array[j] > array[j+1]:
            #Swap them 
            more = array[j]
            array[j] = array[j+1]
            array[j+1] = more
            Swapped = True
            #If no number was swapped that means array is sorted now, break the loop 
            if Swapped == False: 
                Break 
print(array)

    
    
def selection():
    input_text = Enter_arr_sort.get()
    numbers = input_text.split()

    numbers = [int(num) for num in numbers]

    
    length = len(numbers)
    i=1
#def selectionSort(array, n):

    if len(numbers) == 0:
        print("no input")
        result_label_sort.config(text="No numbers entered")
        result_label_sort.place(x=400, y=410) 
        return

    try:
        for i in range(length):
            min_index = int(i)
            for j in range(i + 1, length):
                if numbers[j] < numbers[min_index]:
                    min_index = j
            (numbers[i], numbers[min_index]) = (numbers[min_index], numbers[i])

    
        result_label_sort.config(text=f"Sorted Array is: {numbers}")
        result_label_sort.place(x=400, y=410)  

    except ValueError:
        print("error")
        result_label.config(text="Invalid input")

result_label_sort = Label(root, bg="#21243B", fg="white", font=10)
    


    



















