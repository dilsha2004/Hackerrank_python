def gameOfThrones(s):
    odd = 0

    for ch in set(s):
        if s.count(ch) % 2 != 0:
            odd += 1

    return "YES" if odd <= 1 else "NO"

if __name__ == '__main__':

    s = input()

    result = gameOfThrones(s)
print(result)
