def highestValuePalindrome(s, n, k):
    s = list(s)
    changed = [0] * n


    for i in range(n // 2):
        j = n - 1 - i

        if s[i] != s[j]:
            if s[i] > s[j]:
                s[j] = s[i]
            else:
                s[i] = s[j]

            changed[i] = 1
            k -= 1

    if k < 0:
        return "-1"


    for i in range(n // 2):
        j = n - 1 - i

        if s[i] != '9':
            if changed[i] and k >= 1:
                s[i] = s[j] = '9'
                k -= 1
            elif not changed[i] and k >= 2:
                s[i] = s[j] = '9'
                k -= 2


    if n % 2 == 1 and k > 0:
        s[n // 2] = '9'

    return "".join(s)

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = input()

    result = highestValuePalindrome(s, n, k)
print(result)
