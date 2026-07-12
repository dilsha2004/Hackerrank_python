def workbook(n, k, arr):
    page = 1
    special = 0

    for problems in arr:
        for problem in range(1, problems + 1):
            if problem == page:
                special += 1

            if problem % k == 0 and problem != problems:
                page += 1

        page += 1

    return special

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    arr = list(map(int, input().rstrip().split()))
    result = workbook(n, k, arr)
    print(result)
