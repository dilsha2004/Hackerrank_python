def icecreamParlor(m, cost):

    seen = {}

    for i in range(len(cost)):
        need = m - cost[i]

        if need in seen:
            return [seen[need] + 1, i + 1]

        seen[cost[i]] = i

if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        m = int(input().strip())

        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)
print(result)
