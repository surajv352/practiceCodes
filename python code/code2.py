arr = list(map(int, input().split()))
arr.sort()
mi = ma = 0
minimum = sum((mi + arr[j]) for j in range(0,len(arr)-1))
maximum = sum((ma + arr[k]) for k in range(1,len(arr)))
print(minimum,maximum)
# for i in range(0,len(arr)-1):
# 	mi = mi + arr[i]
# for i in range(1,len(arr)):
# 	ma = ma + arr[i]




#####################################################################
#printing pattern

'''n = int(input())
k = 2*n - (n+1)
print(k)
for i in range(0, n):
	for j in range(0, k):
		print(end=" ")
	k = k - 1
	for j in range(0, i+1):
          print("*", end="")
	print("\r")'''

#####################################################################
 
'''for i in range(0, n): 
    for j in range(0, i+1): 
        print("* ",end="") 
    print("\r")'''