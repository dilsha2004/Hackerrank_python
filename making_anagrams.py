def makingAnagrams(s1, s2):
    letters = set(s1 + s2)

    return sum(
        map(
            lambda ch: abs(s1.count(ch) - s2.count(ch)),
            letters
        )
    )

if __name__ == '__main__':
    s1 = input()
    s2 = input()
    result = makingAnagrams(s1, s2)
    print(result)