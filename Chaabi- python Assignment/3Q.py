def SortListOfDicts(lst, key):
    return sorted(lst, key=lambda x: x[key])

lst = [
    {"fruit": "orange", "color": "orange"},
    {"fruit": "apple", "color": "red"},
    {"fruit": "banana", "color": "yellow"},
    {"fruit": "blueberry", "color": "blue"}
]
 
SortedList1 = SortListOfDicts(lst, "fruit")
print(SortedList1)

SortedList2 = SortListOfDicts(lst, "color")
print(SortedList2)



