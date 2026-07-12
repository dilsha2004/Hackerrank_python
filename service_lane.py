def serviceLane(n, cases):
    result = []

    for i, j in cases:
        smallest = width[i]

        for k in range(i, j + 1):
            if width[k] < smallest:
                smallest = width[k]

        result.append(smallest)

    return result

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    t = int(first_multiple_input[1])
    width = list(map(int, input().rstrip().split()))
    cases = []
    for _ in range(t):
        cases.append(list(map(int, input().rstrip().split())))
    result = serviceLane(n, cases)
    print(result)
    