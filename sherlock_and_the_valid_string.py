def isValid(s):
    letters = set(s)


    counts = list(map(lambda ch: s.count(ch), letters))

    freq = {}
    for c in counts:
        freq[c] = freq.get(c, 0) + 1

    if len(freq) == 1:
        return "YES"

    if len(freq) > 2:
        return "NO"

    f1, f2 = list(freq.keys())

    if (f1 == 1 and freq[f1] == 1) or (f2 == 1 and freq[f2] == 1):
        return "YES"

    if abs(f1 - f2) == 1:
        if (f1 > f2 and freq[f1] == 1) or (f2 > f1 and freq[f2] == 1):
            return "YES"

    return "NO"

if __name__ == '__main__':

    s = input()

    result = isValid(s)
print(result)
