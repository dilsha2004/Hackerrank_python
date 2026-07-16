def funnyString(s):
    rev = s[::-1]

    for i in range(len(s) - 1):
        diff1 = abs(ord(s[i]) - ord(s[i + 1]))
        diff2 = abs(ord(rev[i]) - ord(rev[i + 1]))

        if diff1 != diff2:
            return "Not Funny"

    return "Funny"

if __name__ == '__main__':
    q = int(input().strip())
    for q_itr in range(q):
        s = input()
        result = funnyString(s)
        print(result)