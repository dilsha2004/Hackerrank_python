def beautifulDays(i, j, k):
    count = 0
    for day in range(i, j+1):
        reverse_day = int(str(day)[::-1])
        if abs(day - reverse_day) % k == 0:
            count += 1
    return count

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    i = int(first_multiple_input[0])
    j = int(first_multiple_input[1])
    k = int(first_multiple_input[2])
    result = beautifulDays(i, j, k)
    print(result)
