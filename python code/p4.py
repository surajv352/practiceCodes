#def calculateSquare(n):
 # return n*n*n
x = [int(x) for x in input().split()]
result = list(map(lambda n: n*n*n, x))
print(result)


