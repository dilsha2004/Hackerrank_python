def birthdayCakeCandles(candles):
    tallest = max(candles)
    count = candles.count (tallest)
    return count
    

if __name__ == '__main__':
    candles_count = int(input().strip())
    candles = list(map(int, input().rstrip().split()))
    result = birthdayCakeCandles(candles)
    print(result)
    
