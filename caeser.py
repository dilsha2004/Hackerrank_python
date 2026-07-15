def caesarCipher(s, k):
    k = k % 26
    result = ""

    for ch in s:
        if 'a' <= ch <= 'z':
            ch = chr(ord(ch) + k)
            if ch > 'z':
                ch = chr(ord(ch) - 26)

        elif 'A' <= ch <= 'Z':
            ch = chr(ord(ch) + k)
            if ch > 'Z':
                ch = chr(ord(ch) - 26)

        result += ch

    return result
    
if __name__ == '__main__':
    n = int(input().strip())
    s = input()
    k = int(input().strip())
    result = caesarCipher(s, k)
    print(result)