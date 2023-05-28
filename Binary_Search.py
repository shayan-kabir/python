import math

array = [5, 1, 11, 23, 43, 11, 87]
sorted_array = sorted(array)

print(array)
print(sorted_array)

search_item = 11
Beg = 0
End = len(sorted_array) - 1
Mid = math.floor((Beg + End) / 2)

result_list = []

while Beg <= End:
    if sorted_array[Mid] == search_item:
        result_list.append(Mid)
        # Continue searching for other occurrences
        Beg= Mid - 1
        End = Mid + 1
        while Beg>= Beg and sorted_array[Beg] == search_item:
            result_list.append(Beg)
            Beg-= 1
        while End <= End and sorted_array[End] == search_item:
            result_list.append(End)
            End += 1
        break
    elif sorted_array[Mid] < search_item:
        Beg = Mid + 1
    else:
        End = Mid - 1

    Mid = math.floor((Beg + End) / 2)

if result_list:
    print("The search item is found at indexes:", result_list)
else:
    print("The search item is not found in the array.")
