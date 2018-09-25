def prime(n):
	l1 = []
	for num in range(2,n):
		for i in range(2,num):
			if (num%i)==0:
				break
		else:
			l1.append(num)
	return l1

def fibonacci(n):
	l2 = [1,1]
	a,b = 1,1
	for i in range(n):
		c = a + b
		l2.append(c)
		a = b
		b = c
	return l2
n = int(input())
p = prime(n)
f = fibonacci(n)
print(f)
s = []
for i in range(len(p)):
	s.append(f[i])
	s.append(p[i])
for i in range(len(p),len(f)):
	s.append(f[i])
print(s)
print(s[int(input())-1])
