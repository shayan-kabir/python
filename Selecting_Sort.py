

array = [2,5,6,1,7]
n = len(array)
i=1
def selectionSort(array, n):
    for i in range(n):
        min = i
        for j in range(i + 1, n):
            if array[j] >  array[min]:
                min = j
        (array[i], array[min]) = (array[min], array[i])
selectionSort(array, n)
print('The array after sorting in Ascending Order by selection sort is:')
print(array)


        
        
    
    
    
    
        
    


    


