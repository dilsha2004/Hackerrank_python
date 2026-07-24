def countingSort(arr):
    result = [0] * 100
    
    for value in arr:
        result[value] = result[value] + 1
    
    return result

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = countingSort(arr)
    print(result)