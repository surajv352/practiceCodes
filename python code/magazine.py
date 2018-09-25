def ransom_note(magazine, ransom):
    d = dict()
    print(d)
    for word in magazine:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    print(d)
    print(d[word])
    for word in ransom:
        if not word in d:
            return False
        if d[word] == 0:
            return False
        d[word] -=1
    print(d)
    return True

m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print("Yes")
else:
    print("No")