from functools import reduce


A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
#output of A0 : {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

A1 = range(10)
#output of A1 : range(0, 10)-> 0 to 9

A2 = sorted([i for i in A1 if i in A0])
#output of A2 : []

A3 = sorted([A0[s] for s in A0])
#output of A3 : [1, 2, 3, 4, 5]

A4 = [i for i in A1 if i in A3]
#output of A4 : [1, 2, 3, 4, 5]

A5 = {i:i*i for i in A1}
#output of A5 : {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

A6 = [[i,i*i] for i in A1]
#output of A6 : [[0, 0], [1, 1], [2, 4], [3, 9], [4, 16], [5, 25], [6, 36], [7, 49], [8, 64], [9, 81]]

A7 = reduce(lambda x,y: x+y, [10,23, -45, 33])
# inorder work reduce funtion we need to import it from functools module
#output of A7 : 21

A8 = map(lambda x: x*2, [1,2,3,4])
#output of A8 : address of map object

A9 = filter(lambda x: len(x) >3, [“I” , “want”, “to”, “learn”, “python”])
#ideally which string as more than length 3 those strings are return as list.
# output of A9 : ["want", "learn", "python"] 
