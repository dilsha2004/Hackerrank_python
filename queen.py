def queensAttack(n, k, r_q, c_q, obstacles):
    obstacles = set(map(tuple, obstacles))
    directions = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)]
    total = 0
    
    for dr, dc in directions:
        r, c = r_q, c_q
        while True:
            r, c = r + dr, c + dc
            if r < 1 or r > n or c < 1 or c > n or (r, c) in obstacles:
                break
            total += 1
    
    return total

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    second_multiple_input = input().rstrip().split()
    r_q = int(second_multiple_input[0])
    c_q = int(second_multiple_input[1])
    obstacles = []
    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))
    result = queensAttack(n, k, r_q, c_q, obstacles)
    print(result)
