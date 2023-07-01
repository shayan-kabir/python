from tkinter import *
import math
global root
root = Tk() # Creating an instance
root.title("Search And Sort") # The name of the GUI
root.geometry("800x700") # The size of the GUI
root.resizable(False, False)

root.configure(bg="#21243B") # Background colour of the GUI
global interval   # To changes pages (Search and Sort)
global variable  # Radiobuttons for the info 

global index   # To see if search item is found
interval = 0
resultText =StringVar
global toggle
toggle = 0   # Background color




def change_background_color():
    global toggle
    if toggle == 0:
        root.config(bg="light blue")
        toggle = toggle + 1
        return
    if toggle == 1:
        root.config(bg="darkgray")
        toggle = toggle + 1
        return
    if toggle == 2:
        root.config(bg="White")
        toggle = toggle + 1
        return
    if toggle == 3:
        root.config(bg="#21243B")
        toggle = 0
        return
        




colour_button = Button(root, text="Change Color", command=change_background_color)
colour_button.place(x=12, y =75)




#Switching Buttons based on the radiobuttons choice (Search)


def switch_to_binary():
    
    SEARCH_linear.place_forget()
    SEARCH_binary.place(x=200,y=400)

def switch_to_linear():
    SEARCH_binary.place_forget()
    SEARCH_linear.place(x=200,y=400)
    binary_sort.place_forget()

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
r = IntVar()    # Holds integer data (Helps retrieve)
r.set("1")   # Setting the default
Radiobutton1 = Radiobutton(root, text ="Linear", variable = r, value =int(1), font =20, command = switch_to_linear)
Radiobutton1.place(x=100,y=100)

Radiobutton1.place_forget()



Radiobutton2 = Radiobutton(root, text ="Binary", variable = r, value =int(2), font =20, command =switch_to_binary)
Radiobutton2.place(x=600,y=100)

Radiobutton2.place_forget()

#Radiobuttons (Sort)
v = IntVar()
v.set("1")    # Setting the default

h = IntVar()
h.set("1")    # Setting the default

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


#Entry Widgets (In both Search and Sort)
Enter_arr_sort = Entry(root, font =50, fg="dark blue")
Enter_arr_sort.place(x=400,y=200,)

Enter_arr_sort.place_forget()

Enter_arr_search = Entry(root, font =40, fg="dark blue")
Enter_arr_search.place(x=400,y=200)

Enter_arr_search.place_forget()

Enter_searchitem = Entry(root, font =40, fg = "red",)
Enter_searchitem.place(x=400,y=300)

Enter_searchitem.place_forget()

#Labels  (In search and sort)
menu_label = Label(root, text='Menu', fg='black', bg='blanched almond', font = ('Aerial bold',40), width=26, height=1).place(x=0,y=0)

option = Label(root, text='Please select one', fg='black', bg='blanched almond', font = ('Aerial',25))
option.place(x=265,y=220)

search_label = Label(root, text='Searches', fg='black', bg='blanched almond', font = ('Aerial bold',40), width=26, height=1)
search_label.place(x=0,y=0)
search_label.place_forget()

sort_label = Label(root, text='Sorts', fg='black', bg='blanched almond', font = ('Aerial bold',40), width=26, height=1)
sort_label.place(x=0,y=0)
sort_label.place_forget()

sorted_arr =  Label(root, text= "Sorted Array is: ", fg='white', bg='#21243B', font = ('Aerial',15))  

sorted_arr.place_forget()

search = Label(root, text= "Positions of the search item is: ", fg='white', bg='#21243B', font = ('Aerial',15))

search.place_forget()



#Search options


enter_arr = Label(root, text = "Enter Array",font =("Arial",30))


enter_arr.place_forget()

enter_item = Label(root, text = "Enter Search Item",font =("Arial",30))


enter_item.place_forget()


#Sort options

enter_arr2 = Label(root, text = "Enter Array",font =30)


enter_arr2.place_forget()


order_selection = Label(root, text = "Select Order",font =("Arial",30))


order_selection.place_forget()



#Define functions - Transitions of pages

def click_search():
    global interval
    global variable
    variable = 1
    print(variable)
    if interval ==1:     #pressing menu
        Sort.place(x=130,y=350)
        enter_arr.place_forget()
        option.place(x=265,y=220)
        Search.place(x=400,y=350,)
        result_label.place_forget()
        Enter_searchitem.delete(0,100)
        Enter_arr_search.delete(0,100)
        result_label.config(text="")
        MainInfo.place(x=725, y =625)
        clear_search.place_forget()
        search_info.place_forget()
        SEARCH_linear.place_forget()
        SEARCH_binary.place_forget()
        SearchInfo.place_forget()
        result_label_sort.place_forget()
        binary_sort.place_forget()
        Zoom_in_search.place_forget()
        Zoom_out_search.place_forget()
        search_label.place_forget()
        Radiobutton1.place_forget()
        Radiobutton2.place_forget()
        search.place_forget()
        Enter_arr_search.place_forget()
        Enter_searchitem.place_forget()
        enter_item.place_forget()
        Menu.place_forget()
        interval = 0
    elif interval == 0:     #pressing Search
        
        r.set("1")
        Enter_searchitem.get()==""    # ?
        SEARCH_linear.place(x=200, y=400)
        search.place(x=200, y=450)
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
        SearchInfo.place(x=680,y=625)
        MainInfo.place_forget()
        search_info.place_forget()
        main_info.place_forget()
        Zoom_in_main.place_forget()
        Zoom_out_main.place_forget()
        option.place_forget()
        Sort.place_forget()
        Search.place_forget()
        interval = 1


def click_sort():
    global interval
    global variable
    variable = 1
    print(variable)
    if interval ==1:           #pressing menu
        Sort.place(x=130,y=350)
        option.place(x=265,y=220)
        Search.place(x=400,y=350,)
        result_label_sort.config(text="")
        MainInfo.place(x=725, y =625)
        result_label_sort.place_forget()
        enter_arr.place_forget()
        SORT_selection.place_forget()
        sorted_arr.place_forget()
        Radiobutton3.place_forget()
        Radiobutton4.place_forget()
        Radiobutton5.place_forget()
        Ascending.place_forget()
        Descending.place_forget()
        order_selection.place_forget()
        sort_label.place_forget()
        result_label.place_forget()
        SORT_bubble.place_forget()
        SORT_insertion.place_forget()
        clear_sort.place_forget()
        SortInfo.place_forget()
        Menu2.place_forget()
        Enter_arr_sort.place_forget()
        Enter_arr_sort.delete(0,100)
        sort_info.place_forget()
        search_info.place_forget()
        Zoom_in_sort.place_forget()
        Zoom_out_sort.place_forget()
        interval = 0
        
    elif interval == 0:             #pressing sort
        Enter_arr_sort.get()==""
        v.set("1")
        enter_arr.place(x=100,y=200)
        SORT_selection.place(x=200, y=450)
        sorted_arr.place(x=200, y=400)
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
        Zoom_in_main.place_forget()
        Zoom_out_main.place_forget()
        option.place_forget()
        Sort.place_forget()
        Search.place_forget()
        interval = 1


# Search functionalities 

def linear_search():
        input_text = Enter_arr_search.get()
        numbers = input_text.split()  # Split the input text using space as the delimiter

        input_text2 = Enter_searchitem.get()
        



        if len(numbers) == 0 or len(input_text2) == 0: # Error checking for if users do not input a value
                result_label_sort.config(text="No numbers entered")
                result_label_sort.place(x=400, y=410) 
                return


        try:
            result_label_sort.place_forget()

            result_list = []
            position_list = []
    
            numbers = [int(num) for num in numbers]  # Convert the numbers from strings to integers
        
            search_item = int(Enter_searchitem.get())  # Get the search item as an integer

            

        
            index = -1  # If the search item is not found after iterating through the entire array, the value of index remains as -1.
            for i, num in enumerate(numbers):  #enumerate retrieves both the value and the index whilst iterating the list 
                if num == search_item:
                    index = i
                    result_list.append(i)  # Appending/ adding the indexes into the empty array
                    print(result_list)

            for i in result_list:      # Incrementing all the index values by 1 so that it becomes the position   (Does not run if array is empty )
                i = i + 1
                position_list.append(i)       
                print(i)
                print(position_list)

            
            if index != -1:
                result_label.config(text=f"{position_list}")   #f" f strings are used so that different type of data can be used in a sentence
            else:
                result_label.config(text="Search item not found")
        except ValueError:  
            result_label.config(text="Invalid input (non-numeric value \n entered)")

            


    
        
def binary_search():
    input_text = Enter_arr_search.get()
    numbers = input_text.split()  # Split the input text using space as the delimiter

    result_list = []

    input_text2 = Enter_searchitem.get()

    if len(numbers) == 0 or len(input_text2) == 0: # Error checking for if users do not input a value
                result_label_sort.config(text="No numbers entered")
                result_label_sort.place(x=400, y=410) 
                return


    binary_sort.place(x=200,y=360)

    try:
        numbers = [int(num) for num in numbers]  # Convert the numbers from strings to integers
        sorted_numbers = sorted(numbers)    # Numbers are sorted in binary 
        binary_sort.config(text=f"Sorted Array is: {sorted_numbers}") 
        print(sorted_numbers)
        search_item = int(Enter_searchitem.get())  # Get the search item as an integer

        Beg = 0
        End = len(sorted_numbers) - 1

        while Beg <= End:
            Mid = (Beg + End) // 2  # Compute the midpoint, Floor division

            if sorted_numbers[Mid] == search_item:
                result_list.append(Mid)
                left_index = Mid - 1  #Checks left
                right_index = Mid + 1  #Checks right

                while left_index >= Beg and sorted_numbers[left_index] == search_item:
                    result_list.append(left_index)
                    left_index = left_index - 1       # Iterates to the left (decrementing)

                while right_index <= End and sorted_numbers[right_index] == search_item:
                    result_list.append(right_index)
                    right_index = right_index + 1     # Iterates to the right (incrementing)

                break

            elif sorted_numbers[Mid] < search_item:
                Beg = Mid + 1  # Update the beginning index
            elif sorted_numbers[Mid] > search_item:
                End = Mid - 1  # Update the ending index
            else:
                result_label.config(text="Search item not found")
                break

        position_list = []
        for i in result_list:    # Increments the index value in order to output the position
            i = i + 1
            position_list.append(i)
            print(position_list)

        if len(result_list) > 0:
            result_label.config(text=f"{position_list}")
        else:
            result_label.config(text="Search item not found")

    except ValueError:
        result_label.config(text="Invalid input (non-numeric value \n entered)")

 

            
binary_sort = Label(root, bg="#21243B", fg="white", font=10,)
binary_sort.place(x=200,y=360)

        
# Sort functionalities


def selection():
    input_text = Enter_arr_sort.get()
    numbers = input_text.split()
    
    try:
        numbers = [int(num) for num in numbers]  # Convert the numbers entered by users into integers
        
        if len(numbers) == 0:       # Error checking for if users do not input a value at all
            result_label_sort.config(text="No numbers entered")
            result_label_sort.place(x=400, y=400) 
            return
        
        length = len(numbers)
        i = 0
        for i in range(length):
            if h.get()==1:    # If acsending radio button is selected
                min_index = i        # Setting i as  the minimum index 
                for j in range(i + 1, length):   #another variable to compare
                    if numbers[j] < numbers[min_index]:
                        min_index = j         
                numbers[i], numbers[min_index] = numbers[min_index], numbers[i]   # Swaps i and min_index
            elif h.get()==2:    # If descending radio button is selected
                min_index = i
                for j in range(i + 1, length):
                    if numbers[j] > numbers[min_index]:   #Sign change
                        min_index = j
                numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

        result_label_sort.config(text=f" {numbers}")
        result_label_sort.place(x=400, y=400)
    except ValueError:  # Error check for non numeric entries 
        result_label_sort.config(text="Invalid input (non-numeric value \n entered)")
        result_label_sort.place(x=400, y=400)
     



def bubble():
    input_text = Enter_arr_sort.get()
    numbers = input_text.split()  

    try:
        numbers = [int(num) for num in numbers]  # Convert the numbers from strings to integers
        length = len(numbers)
        
        if len(numbers) == 0: # Error checking for if users do not input a value
            result_label_sort.config(text="No numbers entered")
            result_label_sort.place(x=400, y=400) 
            return
        
        for i in range(length):    # Iterates through the entire array, Swap is initialised to false 
            Swapped = False
            for j in range(length-1):
                if h.get()==1:   # If ascending radio button is selected
                    if numbers[j] > numbers[j+1]:
                        Temp = numbers[j]
                        numbers[j] = numbers[j+1]    # Swaps the element in the array through using an auxiliary value 'Temp'
                        numbers[j+1] = Temp
                        Swapped = True
                        if Swapped == False:  
                            Break
                elif h.get()== 2 :      # If descending radio button is selected
                    if numbers[j] < numbers[j+1]:  #Sign change
                        Temp = numbers[j]
                        numbers[j] = numbers[j+1]
                        numbers[j+1] = Temp
                        Swapped = True
                        if Swapped == False: 
                            Break

        
        result_label_sort.config(text=f"{numbers}")
        result_label_sort.place(x=400, y=400)
    except ValueError:  # Error check for non numeric entries 
        result_label_sort.config(text="Invalid input (non-numeric value \n entered)")
        result_label_sort.place(x=400, y=400)




def insertion():
    input_text = Enter_arr_sort.get()
    numbers = input_text.split()

    try:
        numbers = [int(num) for num in numbers]  # Convert the numbers from strings to integers
        length = len(numbers)

        if len(numbers) == 0: # Error checking for if users do not input a value
            result_label_sort.config(text="No numbers entered")
            result_label_sort.place(x=400, y=400) 
            return
        
        i = 1

        if h.get()==1:         # If acsending radio button is selected
            for i in range(length):
                value = numbers[i]   #Assign value 
                j = i - 1      # Index j is before index i 
                while j>=0 and numbers[j]> value:      # Compares the adjacent elements in the array, as long as numbers[j] is greater, the values will swap 
                    numbers[j+1] = numbers[j]
                    j = j - 1  # Keep decrementng to the left 
                numbers[j+1] = value
        if h.get()==2:          # If descending radio button is selected
            for i in range(length):
                value = numbers[i]
                j = i - 1
                while j>=0 and numbers[j]< value:     #Sign change
                    numbers[j+1] = numbers[j]
                    j = j - 1
                numbers[j+1] = value
        


         
        result_label_sort.config(text=f"{numbers}")
        result_label_sort.place(x=400, y=400)


    except ValueError:  # Error check for non numeric entries 
        result_label_sort.config(text="Invalid input (non-numeric value \n entered)")
        result_label_sort.place(x=400, y=400)
        
        
result_label_sort = Label(root, bg="#21243B", fg="white", font=10)    # Label to display outputs for the sort 

# Clear functionalities

def clear_search():
    result_label.config(text="")
    result_label_sort.config(text="")
    Enter_searchitem.delete(0,100)
    Enter_arr_search.delete(0,100)
    binary_sort.place_forget()
    

def clear_sort():
    result_label_sort.config(text="")
    Enter_arr_sort.delete(0,100)


# Clear buttons

clear_search = Button(root, text= "Clear ", fg='black', bg='light blue', font = 5, command = clear_search)
clear_search.place(x=722, y=500)
clear_search.place_forget()


clear_sort = Button(root, text= "Clear", fg='black', bg='light blue', font = 5,  command = clear_sort )
clear_sort.place(x=722, y=500)
clear_sort.place_forget()






# Search or Sort option (Main Menu)

Sort = Button(root, text='Sort', fg='black', bg='#e6e6e6', font=('Times', 20), width=15,command = click_sort)
Sort.place(x=130,y=350)

Search = Button(root, text='Search', fg='black', bg='#e6e6e6', font=('Times', 20),command = click_search, width=15)
Search.place(x=400,y=350)

# Different Menu for disparate options of Search or Sort 

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

result_label = Label(root,bg="#21243B",fg = "white", font =10)          # Label to display outputs for the search 
result_label.place(x=500, y=510)
result_label.place_forget()





# info labels and its corresponding buttons with functions

variable = 1  # allows the info button to toggle 
def infoMain():
    global variable
    if variable == 1:
        main_info.place(y = 550, relx = 0.5, anchor = CENTER)      # Info
        Zoom_in_main.place(x=350, y=660,width= 30,height= 30)       # Zoom in
        Zoom_out_main.place(x=450, y=660, width= 30,height= 30) #Zoom out
        variable =0
    elif variable == 0:
        main_info.place_forget()
        Zoom_in_main.place_forget()
        Zoom_out_main.place_forget()
        variable = 1
        

def infoSearch():
    global variable
    if variable == 1:
        search_info.place(y = 560, relx = 0.5, anchor = CENTER)
        Zoom_in_search.place(x=350, y=660, width= 30,height= 30)
        Zoom_out_search.place(x=450, y=660, width= 30,height= 30)
        variable =0
    elif variable == 0:
        search_info.place_forget()
        Zoom_in_search.place_forget()
        Zoom_out_search.place_forget()
        variable = 1

def infoSort():
    global variable
    if variable == 1:
        sort_info.place(y = 550, relx = 0.5, anchor = CENTER)
        Zoom_in_sort.place(x=350, y=660, width= 30,height= 30)
        Zoom_out_sort.place(x=450, y=660, width= 30,height= 30)
        variable =0
    elif variable == 0:
        sort_info.place_forget()
        variable = 1
        Zoom_in_sort.place_forget()
        Zoom_out_sort.place_forget()
    

# Main menu 


MainInfo = Button(root, text='info',fg='black', bg='blanched almond', font = ('Aerial',20), command = infoMain)
MainInfo.place(x=725,y=625)

main_info = Label(root, text = "This is a search and sort application. \n Please select either search and select to use the features", font=("TkDefaultFont", 12))
main_info.place_forget()

# Search

SearchInfo = Button(root, text='Search info',fg='black', bg='blanched almond', font = ('Aerial',15), command = infoSearch)
SearchInfo.place(x=650,y=625)
SearchInfo.place_forget()

search_info = Label(root, text = "This is the Search feature. Please select either Linear search or Binary search. \n Once selected, make sure to insert integers (seperated by space) into the entries then press the orange button", font=("TkDefaultFont", 9))

# Sort

SortInfo = Button(root, text='Sort info',fg='black', bg='blanched almond', font = ('Aerial',20), command = infoSort)
SortInfo.place(x=625,y=625)
SortInfo.place_forget()

sort_info = Label(root, text = "This is the Sort feature. Please select either Selection, Bubble or Insertion sort. \n Once selected, make sure to insert integers (seperated by space) into the entries then \n select between Ascending or Descending. Then press the orange button", font=("TkDefaultFont", 9))



#Zoom functions (Main Menu)

def zoom_in():
    Zoom_out_main.place(x=450, y=660, width= 30,height= 30) 
    new_size = 0
    current_size = main_info.cget("font").split()[1]  #recieves the size
    new_size = int(current_size) + 1
    print(new_size)
    if new_size > 15:
        Zoom_in_main.place_forget()
        Zoom_out_main.place(x=450, y=660, width= 30,height= 30) 
    main_info.config(font=("TkDefaultFont", new_size))

def zoom_out():
    Zoom_in_main.place(x=350, y=660, width= 30,height= 30)
    new_size = 0
    current_size = main_info.cget("font").split()[1]
    new_size = int(current_size) - 1
    print(new_size)
    if new_size < 12:
        Zoom_out_main.place_forget()
        Zoom_in_main.place(x=350, y=660, width= 30,height= 30) 
    main_info.config(font=("TkDefaultFont", new_size))


Zoom_in_main = Button(root, text="+", font=40, command = zoom_in)
Zoom_in_main.place_forget()

Zoom_out_main = Button(root, text="-", font = 40, command = zoom_out)
Zoom_out_main.place_forget()



#Zoom functions (Search)


def zoom_in_search():
    Zoom_out_search.place(x=450, y=660, width= 30,height= 30) 
    new_size = 0
    current_size = search_info.cget("font").split()[1]     # cget - 'Get configuration' - retrieve the current value of font ("TkDefaultFont", 9)
    new_size = int(current_size) + 1
    if new_size > 10:
        Zoom_in_search.place_forget()
        Zoom_out_search.place(x=450, y=660, width= 30,height= 30) 
    search_info.config(font=("TkDefaultFont", new_size))   # The increase in size is implemented 


def zoom_out_search():
    Zoom_in_search.place(x=350, y=660, width= 30,height= 30)
    new_size = 0
    current_size = search_info.cget("font").split()[1]
    new_size = int(current_size) - 1
    print(new_size)
    if new_size < 10:     # Sign change 
        Zoom_out_search.place_forget()
        Zoom_in_search.place(x=350, y=660, width= 30,height= 30) 
    search_info.config(font=("TkDefaultFont", new_size))

    
Zoom_in_search = Button(root, text="+", font=40, command = zoom_in_search)
Zoom_in_search.place_forget()

Zoom_out_search = Button(root, text="-", font = 40, command = zoom_out_search)
Zoom_out_search.place_forget()

#Zoom functions (Sort)



def zoom_in_sort():
    Zoom_out_sort.place(x=450, y=660, width= 30,height= 30) 
    new_size = 0
    current_size = sort_info.cget("font").split()[1]
    new_size = int(current_size) + 1
    print(new_size)
    if new_size > 11:
        Zoom_in_sort.place_forget()
        Zoom_out_sort.place(x=450, y=660, width= 30,height= 30) 
    sort_info.config(font=("TkDefaultFont", new_size))


def zoom_out_sort():
    Zoom_in_sort.place(x=350, y=660, width= 30,height= 30) 
    new_size = 0
    current_size = sort_info.cget("font").split()[1]
    new_size = int(current_size) - 1
    print(new_size)
    if new_size < 10:
        Zoom_out_sort.place_forget()
        Zoom_in_sort.place(x=350, y=660, width= 30,height= 30) 
    sort_info.config(font=("TkDefaultFont", new_size))



Zoom_in_sort = Button(root, text="+", font=40, command = zoom_in_sort)
Zoom_in_sort.place_forget()

Zoom_out_sort = Button(root, text="-", font = 40, command = zoom_out_sort)
Zoom_out_sort.place_forget()




mainloop()









         
