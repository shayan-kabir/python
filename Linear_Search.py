array = input("Give me Array: ").split()
print(array)


i = 0
search_item = 15
found_item = False 

while found_item is False and i < len(array):
    if int(array[i]) == search_item:
        found_item = True
        print("in" + str(i))
        break
    else:
        i = i+1
        print("out" + str(i))
            
       
if found_item == True:
    print("The search item is found at index " + str(i) )
else:
    print( "The search item is not found")


    

        
    
