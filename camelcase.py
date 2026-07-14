def camelcase(s):
    count = 1

    for ch in s:
        if ch.isupper():
            count += 1

    return count
    
if __name__ == '__main__':
    s = input()
    result = camelcase(s)
    print(result)