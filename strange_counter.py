def strangeCounter(t):
    value = 3

    while t > value:
        t = t - value
        value = value * 2

    return value - t + 1
    
if __name__ == '__main__':
    t = int(input().strip())
    result = strangeCounter(t)
    print(result)
