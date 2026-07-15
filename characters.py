def alternate(s):
    letters = list(set(s))
    ans = 0

    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            temp = ""

            for ch in s:
                if ch == letters[i] or ch == letters[j]:
                    temp += ch

            ok = True

            for k in range(len(temp) - 1):
                if temp[k] == temp[k + 1]:
                    ok = False
                    break

            if ok:
                ans = max(ans, len(temp))

    return ans

if __name__ == '__main__':

    l = int(input().strip())
    s = input()
    result = alternate(s)
    print(result)
