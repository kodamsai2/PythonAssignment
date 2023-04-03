def SubList(lst, start, end):
    return lst[start:end+1:2]

lst = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
sublist = SubList(lst, 2, 9)
print(sublist)