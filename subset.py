def nonDivisibleSubset(k, s):
    remainder_counts = [0] * k
    for num in s:
        remainder_counts[num % k] += 1
    
    count = 0
    if remainder_counts[0] > 0:
        count += 1
    if k % 2 == 0 and remainder_counts[k // 2] > 0:
        count += 1
    for r in range(1, k // 2 + 1):
        if r == k - r:
            continue
        count += max(remainder_counts[r], remainder_counts[k - r])
    
    return count
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    s = list(map(int, input().rstrip().split()))
    result = nonDivisibleSubset(k, s)
    print(result)
