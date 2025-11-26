def print_items(a,b):
    for i in range(a): #O(n)  O(a)
        print(i)
    for j in range(b):   #O(n)  )(b)
        print(j)   #O(a+b)    #O(2n) drop constant applied O(n)


"""def print_items(a,b):
    for i in range(a):   #O(a)
        for j in range(b): #O(b)
            print(i,j)  #O(a*b) or O(n^2)"""

