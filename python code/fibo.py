def fibo(a):
	c = 1
	x = 0
	while(a!=0):
		if (c%2==0):
			a = a//2
			c += 1
			x += 1
		else:
			a = a - 1
			c += 1
			x += 1
	return x
a = int(input())
res = fibo(a)
print(res)