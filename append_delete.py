def appendAndDelete(s, t, k):
    common = 0
    min_len = min(len(s), len(t))
    for i in range(min_len):
        if s[i] == t[i]:
            common += 1
        else:
            break
    min_ops = (len(s) - common) + (len(t) - common)
    
    if k >= min_ops:
        if k >= len(s) + len(t):
            return "Yes"
        elif (k - min_ops) % 2 == 0:
            return "Yes"
        else:
            return "No"
    else:
        return "No"

if __name__ == '__main__':
    s = input()
    t = input()
    k = int(input().strip())
    result = appendAndDelete(s, t, k)
    print(result)
