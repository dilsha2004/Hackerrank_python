def cutTheSticks(arr):
    result = []
    sticks = arr[:]
    
    while sticks:
        result.append(len(sticks))
        shortest = min(sticks)
        sticks = [s - shortest for s in sticks if s > shortest]
    
    return result

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = cutTheSticks(arr)
    print(result)