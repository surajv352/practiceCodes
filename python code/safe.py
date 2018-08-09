x,y = input().split('#')
x = list(x)
y = list(y)
c = 0
print(x,y)
for i in range(len(x)):
	while x[i] != y[i]:
		if x[i] == '9':
			x[i] = '0'
		else:
			if x[i] == '0':
				x[i] = '1'
			elif x[i] == '1':
				x[i] = '2'
			elif x[i] == '2':
				x[i] = '3'
			elif x[i] == '3':
				x[i] = '4'
			elif x[i] == '4':
				x[i] = '5'
			elif x[i] == '5':
				x[i] = '6'
			elif x[i] == '6':
				x[i] = '7'
			elif x[i] == '7':
				x[i] = '8'
			elif x[i] == '8':
				x[i] = '9'
			
			c += 1
res = c//(len(x))
print(res)