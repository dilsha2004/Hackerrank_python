def pickingNumbers(a):
    counts = [0] * 100
    for num in a:
        counts[num] += 1
    max_length = 0
    for i in range(99):
        max_length = max(max_length, counts[i] + counts[i+1])
    return max_length

if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    result = pickingNumbers(a)
    print(result)