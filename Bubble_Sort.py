array = [14, 33, 27, 35, 10]
n = len(array)
i = 0
for i in range(n):
    Swapped = False 
    for j in range(n - 1): 
    #Compare the adjacent elements
        if array[j] < array[j+1]:
            #Swap them 
            more = array[j]
            array[j] = array[j+1]
            array[j+1] = more
            Swapped = True
            #If no number was swapped that means array is sorted now, break the loop 
            if Swapped == False: 
                Break 
print(array)




