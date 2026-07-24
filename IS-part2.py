def insertionSort2(n, arr):
    for i in range(1, n):
        e = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] > e:
            arr[j+1] = arr[j]
            j = j - 1
        
        arr[j+1] = e
        
        print(' '.join(map(str, arr)))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
    print(insertionSort2)