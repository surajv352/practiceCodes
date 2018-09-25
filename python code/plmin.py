n = int(input())
arr = list(map(int, input().split()))
p=ne=z=0
for num in arr:
	if num > 0:
		p += 1
	elif num < 0:
		ne += 1
	elif num == 0:
		z += 1
a = p/n
b = ne/n
c = z/n
print('{0:.6f}'.format(a))
print('{0:.6f}'.format(b))
print('{0:.6f}'.format(c))