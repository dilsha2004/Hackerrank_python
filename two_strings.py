def twoStrings(s1, s2):

    if set(s1) & set(s2):
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':

    q = int(input().strip())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)
print(result)
