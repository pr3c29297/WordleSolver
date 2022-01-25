from itertools import permutations, combinations
print(list(permutations(['s','c','k','n','e'])))
file = open("words.txt", 'r')
ValidWord = []
for line in file.readlines():
    if (len(line.strip())==5):
        ValidWord.append(line.strip().upper())
file.close()
Term = False
az = list(map(lambda x: chr(x), list(range((ord('A')),(ord('Z')+1)))))
while not Term:
    wrong = []
    order = []
    PossibleAns=[]
    curr = input("capital char in correct order, mark unkown by '_': ")
    wo = input("incorrect order guess, input as string, mark other by '?': ")
    for i, v in enumerate(wo):
        if (v!='?'):
            order.append(v)
    worder = list(wo)
    ng = input("incorrect char guess, input as string, no separator: ")
    for i in ng:
        wrong.append(i)
    count = 0
    pos=[]
    for i, v in enumerate(curr):
        if (v=='_'):
            count+=1
            pos.append(i)
    perm = list(permutations(az, count))
    attemp = list(curr)
    for i in perm:
        newguess = True
        for j in i:
            if (j in wrong):
                newguess = False
        consist = 0
        for j in i:
            if (j in order):
                consist += 1
        if (newguess and consist>=len(order)):
            for j, v in enumerate(pos):
                attemp[v] = i[j]
            check=True
            for i, v in enumerate(attemp):
                if (attemp[i]==worder[i]):
                    check= False
            temp = ''.join(attemp)
            if ((temp in ValidWord) and (check)):
                PossibleAns.append(temp)
    print(PossibleAns)
    if (len(PossibleAns)==1):
        Term = True