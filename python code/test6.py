A = int(input())
B = int(input())
C = int(input())
def lcm(x,y):
	if B>C:
		g = B
	else:
		g = C
	while(True):
		if(g%B==0) and (g%C==0):
			lcm = g
			break
		g += 1
	return lcm

t = B*C
r = lcm(B,C)
if A>=t:
	res = A//r
print(res)