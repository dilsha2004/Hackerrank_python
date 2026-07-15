def minimumNumber(n, password):
    digit = False
    lower = False
    upper = False
    special = False

    special_chars = "!@#$%^&*()-+"

    for ch in password:
        if ch.isdigit():
            digit = True
        elif ch.islower():
            lower = True
        elif ch.isupper():
            upper = True
        elif ch in special_chars:
            special = True

    missing = 0

    if not digit:
        missing += 1
    if not lower:
        missing += 1
    if not upper:
        missing += 1
    if not special:
        missing += 1

    return max(missing, 6 - n)
    
if __name__ == '__main__':
    n = int(input().strip())
    password = input()
    answer = minimumNumber(n, password)
    print(answer)