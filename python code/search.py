x = int(input("enter no. of items: "))
items = []
for i in range(x):
	items.append(input())

item = input("enter item to be search: ")
if item in items:
	print("item found")
else:
	print("item not found")
for i in range(len(items)):
	if items[i] == item:
		print("match found at position: {}".format(i+1))