def breakingRecords(scores):
    minimum = scores[0]
    maximum = scores[0]
    min_count = 0
    max_count = 0
    
    for score in scores[1:]:
        if score > maximum:
            maximum = score
            max_count += 1
        elif score < minimum:
            minimum = score
            min_count += 1
            
    return[max_count,min_count]

if __name__ == '__main__':
    n = int(input().strip())
    scores = list(map(int, input().rstrip().split()))
    result = breakingRecords(scores)
    print(result)