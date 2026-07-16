def pangrams(s):
    s = s.lower()
    letters = set()

    for ch in s:
        if 'a' <= ch <= 'z':
            letters.add(ch)

    if len(letters) == 26:
        return "pangram"
    else:
        return "not pangram"
        
if __name__ == '__main__':
    s = input()
    result = pangrams(s)
    print(result)