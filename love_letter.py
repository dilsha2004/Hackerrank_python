def theLoveLetterMystery(s):
    count = 0

    left = 0
    right = len(s) - 1

    while left < right:
        count += abs(ord(s[left]) - ord(s[right]))
        left += 1
        right -= 1

    return count
    
if __name__ == '__main__':
    q = int(input().strip())
    for q_itr in range(q):
        s = input()
        result = theLoveLetterMystery(s)
        print(result)
