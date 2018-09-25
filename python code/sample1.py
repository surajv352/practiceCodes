n = int(input())
l = r = 0
arr = []

for i in range(n):
	a = list(map(int, input().split()))
	arr.append(a)

for i in range(len(arr)):
	l += arr[i][i]

for i in range(len(arr)):
	r += arr[i][n-i-1]

res = abs(l-r)
print(res)