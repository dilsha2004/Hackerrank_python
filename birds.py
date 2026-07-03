def migratoryBirds(arr):
    counts = {}
    for bird in arr:
        counts[bird]=counts.get(bird,0)+1
        
        max_count=max(counts.values())
        types = [bird_id for bird_id, count in counts.items()if count == max_count]
        
    return min(types)
        
if __name__ == '__main__':
    arr_count = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = migratoryBirds(arr)
    print(result)