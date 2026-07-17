def palindromeIndex(s):
    if s == s[::-1]:
        return -1
    for i in range(len(s)):
        newString = s[:i] + s[i+1:]

        if newString == newString[::-1]:
            return i

    return -1
if __name__ == '__main__':
    q = int(input().strip())
    for q_itr in range(q):
        s = input()
        result = palindromeIndex(s)
        print(result)