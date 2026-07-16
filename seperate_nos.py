def separateNumbers(s):
    n = len(s)

    for i in range(1, n // 2 + 1):
        first = int(s[:i])
        current = first
        new = ""

        while len(new) < n:
            new += str(current)
            current += 1

        if new == s:
            print("YES", first)
            return

    print("NO")
if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
        print(separateNumbers)