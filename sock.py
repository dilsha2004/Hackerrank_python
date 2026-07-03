def sockMerchant(n, ar):
    counts = {}
    for color in ar:
        counts[color] = counts.get(color, 0) + 1
    pairs = 0
    for count in counts.values():
        pairs += count // 2
    return pairs

if __name__ == '__main__':
    n = int(input().strip())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)
    print(result)