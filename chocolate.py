def chocolateFeast(n, c, m):
    chocolates = n // c
    wrappers = chocolates

    while wrappers >= m:
        free = wrappers // m
        chocolates += free
        wrappers = wrappers % m + free

    return chocolates

if __name__ == '__main__':

    t = int(input().strip())
    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()
        n = int(first_multiple_input[0])
        c = int(first_multiple_input[1])
        m = int(first_multiple_input[2])
        result = chocolateFeast(n, c, m)
        print(result)