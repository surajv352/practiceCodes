'''x, y = [int(x) for x in input().split()]
lambda x,y: x+y
print(x+y)'''

'''def square(list1):
    list2 = []
    for num in list1:
        list2.append(num**2)
    return list2
res = square([1,2,3,4,5])
print(res)'''

n = [1,2,3,4,5,6,7,8,9,10]
res = set(map(lambda x: x**2,n ))
print(res)
