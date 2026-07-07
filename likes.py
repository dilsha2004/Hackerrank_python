def viralAdvertising(n):
    shared = 5
    cumulative = 0
    
    for day in range(1, n+1):
        liked = shared // 2
        cumulative += liked
        shared = liked * 3
    
    return cumulative
if __name__ == '__main__':
    n = int(input().strip())
    result = viralAdvertising(n)
    print(result)