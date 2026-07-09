def repeatedString(s, n):
    full_repeats = n // len(s)
    remainder = n % len(s)
    
    count = s.count('a') * full_repeats
    count += s[:remainder].count('a')
    
    return count

if __name__ == '__main__':
    s = input()
    n = int(input().strip())
    result = repeatedString(s, n)
    print(result)
    
