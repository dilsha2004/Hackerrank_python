def missingNumbers(arr, brr):

    count1 = {}
    count2 = {}

    for num in arr:
        if num in count1:
            count1[num] += 1
        else:
            count1[num] = 1

    for num in brr:
        if num in count2:
            count2[num] += 1
        else:
            count2[num] = 1

    result = []

    for num in sorted(count2):
        if num not in count1 or count1[num] != count2[num]:
            result.append(num)

    return result

if __name__ == '__main__':

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)
print(result)
