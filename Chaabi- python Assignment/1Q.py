def SelectionSort(lst):
    n = len(lst)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst

lst = [5,416,54,21,6135,15,741]
result = SelectionSort(lst)
print("Sorted list after applying selection sort:", result)