def equalizeArray(arr):
    counts = {}
    for num in arr:
        counts[num] = counts.get(num, 0) + 1
    
    max_count = max(counts.values())
    return len(arr) - max_count

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = equalizeArray(arr)
    print(result)
