a = input()
b = input()
c = input()
s,s1,s2 = '','',''
for i in a:
	if (i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
		i = '$'
		s += i
	else:
		s += i
print(s)
for i in b:
	if (i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
		i = '#'
		s1 += i
	else:
		s1 += i
for i in c:
	x = i.upper()
	s2 += x
res = s + s1 + s2
print(res)	
