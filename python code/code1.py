def findEliminatorXWinner(playerIds):
    s = []
    s1 = []
    for i in range(0,len(playerIds),2):
        s.append(playerIds[i])

    if(len(playerIds)%2==0):
    	for i in range(len(playerIds)-1,0,-2):
    		s.append(playerIds[i])
    else:
    	for i in range(len(playerIds)-2,0,-2):
    		s.append(playerIds[i])

    # for i in s:
    #     s1.append(i)
    return s
playerIds = input().split(',')
res = findEliminatorXWinner(playerIds)
print(res[-1])
