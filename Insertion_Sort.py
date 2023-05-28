array = [14, 33, 27, 35, 10]
i = 1
n = len(array)
for i in range(1,n):
    Value = array[i]
    j = i-1
    while j>=0 and array[j]< Value:
        array[j+1] = array[j]
        j = j-1
    array[j + 1] = Value
print(array)

