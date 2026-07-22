def morganAndString(a, b):
    a += "{"
    b += "{"

    i = j = 0
    ans = []

    while i < len(a) - 1 or j < len(b) - 1:
        if a[i:] <= b[j:]:
            ans.append(a[i])
            i += 1
        else:
            ans.append(b[j])
            j += 1

    return "".join(ans)

if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        a = input()

        b = input()

        result = morganAndString(a, b)
print(result)
