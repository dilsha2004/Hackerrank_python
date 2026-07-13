def larrysArray(A):
    inv = 0

    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if A[i] > A[j]:
                inv += 1

    if inv % 2 == 0:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        A = list(map(int, input().rstrip().split()))
        result = larrysArray(A)
        print(result)