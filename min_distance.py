def minimumDistances(a):
    min_dist = len(a) + 1

    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] == a[j]:
                min_dist = min(min_dist, j - i)

    if min_dist == len(a) + 1:
        return -1
    else :
         return min_dist
    

if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    result = minimumDistances(a)
    print(result)