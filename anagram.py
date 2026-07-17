def anagram(s):
    if len(s) % 2 != 0:
        return -1

    mid = len(s) // 2
    first = s[:mid]
    second = s[mid:]

    freq = {}


    for ch in first:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1


    for ch in second:
        if ch in freq and freq[ch] > 0:
            freq[ch] -= 1

    changes = 0


    for value in freq.values():
        changes += value

    return changes
    
if __name__ == '__main__':
    q = int(input().strip())
    for q_itr in range(q):
        s = input()
        result = anagram(s)
        print(result)