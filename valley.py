def countingValleys(steps, path):
    alt = 0
    valley = 0
    
    for step in path:
        if step == 'U':
            alt +=1
            if alt == 0:
                valley += 1
        else:
            alt -=1
    return valley

if __name__ == '__main__':
    steps = int(input().strip())
    path = input()
    result = countingValleys(steps, path)
    print(result)