class stack:
	def __init__(self):
		self.stack = []
	def isEmpty(self):
		return self.stack == []
	def push(self, data):
		self.stack.append(data)
	def pop(self):
		data = self.stack[-1]
		del self.stack[-1]
		return data
	def peek(self):
		return self.stack[-1]
	def sizeStack(self):
		return len(self.stack)
s = stack()
x = [int(x) for x in input().split()]
for i in range(len(x)):
	s.push(x[i])
# s.push(5)
# s.push(6)
# s.push(8)
# s.push(10)
# s.push(36)
# s.push(50)
print(s.stack)
print("popped: {0}".format(s.pop()))
print(s.stack)
print("popped: {0}".format(s.pop()))
print(s.stack)
print("popped: {0}".format(s.pop()))
print(s.stack)