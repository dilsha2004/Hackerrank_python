def surfaceArea(A):
    h = len(A)
    w = len(A[0])
    area = 0

    for i in range(h):
        for j in range(w):
            if A[i][j] > 0:
                area += 2

                if i == 0:
                    area += A[i][j]
                else:
                    area += max(0, A[i][j] - A[i-1][j])

                if i == h - 1:
                    area += A[i][j]
                else:
                    area += max(0, A[i][j] - A[i+1][j])

                if j == 0:
                    area += A[i][j]
                else:
                    area += max(0, A[i][j] - A[i][j-1])

                if j == w - 1:
                    area += A[i][j]
                else:
                    area += max(0, A[i][j] - A[i][j+1])

    return area
    
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    H = int(first_multiple_input[0])
    W = int(first_multiple_input[1])
    A = []
    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))
    result = surfaceArea(A)
    print(result)