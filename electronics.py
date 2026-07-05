def getMoneySpent(keyboards, drives, b):
    cost = -1
    for k in keyboards:
        for d in drives:
            total=k+d
            if total<=b and total>cost:
                cost = total
    return cost
if __name__ == '__main__':
    bnm = input().split()
    b = int(bnm[0])
    n = int(bnm[1])
    m = int(bnm[2])
    keyboards = list(map(int, input().rstrip().split()))
    drives = list(map(int, input().rstrip().split()))
    moneySpent = getMoneySpent(keyboards, drives, b)
    print(moneySpent)