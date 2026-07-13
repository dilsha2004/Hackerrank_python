def stones(n, a, b):
    result = []

    for i in range(n):
        value = (n - 1 - i) * a + i * b
        if value not in result:
            result.append(value)

    return sorted(result)
    
if __name__ == '__main__':
    T = int(input().strip())
    for T_itr in range(T):
        n = int(input().strip())
        a = int(input().strip())
        b = int(input().strip())
        result = stones(n, a, b)
        print(result)