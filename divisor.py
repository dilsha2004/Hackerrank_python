def findDigits(n):
    count = 0
    for digit_char in str(n):
        digit = int(digit_char)
        if digit != 0 and n % digit == 0:
            count += 1
    return count
if __name__ == '__main__':
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        result = findDigits(n)
        print(result)