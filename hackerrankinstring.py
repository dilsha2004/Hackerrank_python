def hackerrankInString(s):
    word = "hackerrank"
    j = 0

    for ch in s:
        if j < len(word) and ch == word[j]:
            j += 1

    if j == len(word):
        return "YES"
    else:
        return "NO"
        
if __name__ == '__main__':
    q = int(input().strip())
    for q_itr in range(q):
        s = input()
        result = hackerrankInString(s)
        print(result)
