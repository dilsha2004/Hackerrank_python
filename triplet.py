def beautifulTriplets(d, arr):
    count = 0
    numbers = set(arr)

    for num in arr:
        if num + d in numbers and num + 2 * d in numbers:
            count += 1

    return count

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    d = int(first_multiple_input[1])
    arr = list(map(int, input().rstrip().split()))
    result = beautifulTriplets(d, arr)
    print(result)