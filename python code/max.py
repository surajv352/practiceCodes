for s in range(10):
	inputs = input("enter y to continue: ")
	if (inputs != 'y'):
		break
	else:
		x = [int(x) for x in input().split()]
		max = x[0]
		for num in x:
			if num > max:
				max = num
		print(max)
	# elements = list(x)
# for i in range(x):
# 	# elements.append(input())
# 	# print("",end='')