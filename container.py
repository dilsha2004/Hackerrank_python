def organizingContainers(container):
    n = len(container)
    row_sums = sorted(sum(row) for row in container)
    col_sums = sorted(sum(container[r][c] for r in range(n)) for c in range(n))
    
    if row_sums == col_sums:
        return "Possible"
    else:
        return "Impossible"

if __name__ == '__main__':
    q = int(input().strip())
    for q_itr in range(q):
        n = int(input().strip())
        container = []
        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))
        result = organizingContainers(container)
        print(result)

