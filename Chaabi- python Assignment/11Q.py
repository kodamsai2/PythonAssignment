def f(x,l=[]):
    for i in range(x):
        l.append(i*i)
    print(l)


f(2)#output: [0, 1]
f(3,[3,2,1])#output: [3, 2, 1, 0, 1, 4]
f(3)# output: [0, 1, 0, 1, 4]

'''
In last function call, list is not provided to it.so,it uses default list.
first function call also not provided the list to it.so, it created the empty list and append 0 and 1 to the list. 
beacuse of this in last function call's output: first 2 values(0 and 1) is present in it
'''