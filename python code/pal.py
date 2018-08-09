n = int(input())
s = 0
n1 = n
while n>0:
    r = n%10
    s = s + r
    n = n//10
print(s)

