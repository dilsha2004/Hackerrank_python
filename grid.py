def gridSearch(G, P):
    rows = len(G)
    cols = len(G[0])
    p_rows = len(P)
    p_cols = len(P[0])

    for i in range(rows - p_rows + 1):
        for j in range(cols - p_cols + 1):
            found = True

            for k in range(p_rows):
                if G[i + k][j:j + p_cols] != P[k]:
                    found = False
                    break

            if found:
                return "YES"

    return "NO"
    
if __name__ == '__main__':
    t = int(input().strip())
    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()
        R = int(first_multiple_input[0])
        C = int(first_multiple_input[1])
        G = []
        for _ in range(R):
            G_item = input()
            G.append(G_item)
        second_multiple_input = input().rstrip().split()
        r = int(second_multiple_input[0])
        c = int(second_multiple_input[1])
        P = []
        for _ in range(r):
            P_item = input()
            P.append(P_item)
        result = gridSearch(G, P)
        print(result)