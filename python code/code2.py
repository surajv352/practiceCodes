l = input()
o = 0
c = 0
s = []
s1 = ''
for i in l:
	if(i=='('):
		o += 1
		s.append(o)

	elif(i==')'):
		if(o==(c+2)):
			s.append(o)
		else:
			c += 1
			s.append(c)
print(str(s))
for i in s:
	s1 += str(i)
print(s1)