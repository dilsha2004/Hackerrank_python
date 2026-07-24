def balancedSums(arr):
    total = sum(arr)
    left_sum = 0
    
    for i in range(len(arr)):
        right_sum = total - left_sum - arr[i]
        
        if left_sum == right_sum:
            return "YES"
        
        left_sum += arr[i]
    
    return "NO"

if __name__ == '__main__':
    T = int(input().strip())
    for T_itr in range(T):
        n = int(input().strip())
        arr = list(map(int, input().rstrip().split()))
        result = balancedSums(arr)
        print(result)
        
