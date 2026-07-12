def howManyGames(p, d, m, s):
    count = 0

    while s >= p:
        s -= p
        count += 1
        p = max(m, p - d)

    return count

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    p = int(first_multiple_input[0])
    d = int(first_multiple_input[1])
    m = int(first_multiple_input[2])
    s = int(first_multiple_input[3])
    result = howManyGames(p, d, m, s)
    print(result)
