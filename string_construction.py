def stringConstruction(s):

    letters = set(s)

    return len(letters)

if __name__ == '__main__':

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = stringConstruction(s)
print(result)
