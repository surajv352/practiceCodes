x = [int(x) for x in input().split()]
buy_day = [1, 1, 2]
sale_day = [2, 3, 3]
profit = []
avg_profit = []
for i in range(1,len(x)):
	if (x[0] < x[i]):
		t = x[i] - x[0]
		profit.append(t)
		avg_profit.append(t//(sale_day[i-1]-buy_day[i-1]))
	else:
		print("impossible")
	if (x[i] < x[-1]):
		t = x[-1] - x[i]
		profit.append(t)
		avg_profit.append(t//(sale_day[i+1]-buy_day[i+1]))
ap = sorted(avg_profit)
p = sorted(profit)
print(ap[-1],end=' ')
n = avg_profit.index(ap[-1])
print(profit[n])