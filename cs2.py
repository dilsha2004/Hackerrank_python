def countingSort(arr):
    result = [0] * 100
    
    for value in arr:
        result[value] = result[value] + 1
    
    sorted_arr = []
    for i in range(100):
        count = result[i]
        for j in range(count):
            sorted_arr.append(i)
    
    return sorted_arr
if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = countingSort(arr)
    print(result)