def permutationEquation(p):
    result = []
    for x in range(1, len(p)+1):
        a = p.index(x) + 1
        y = p.index(a) + 1
        result.append(y)
    return result
if __name__ == '__main__':
    n = int(input().strip())
    p = list(map(int, input().rstrip().split()))
    result = permutationEquation(p)
    print(result)