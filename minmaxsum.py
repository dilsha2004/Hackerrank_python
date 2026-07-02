def miniMaxSum(arr):
    total = sum(arr)
    mini = total - max(arr)
    maxi = total - min(arr)
    print(mini,maxi)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)