def weightedUniformStrings(s, queries):
    weights = set()

    count = 0
    prev = ""

    for ch in s:
        if ch == prev:
            count += 1
        else:
            count = 1
            prev = ch

        weight = (ord(ch) - ord('a') + 1) * count
        weights.add(weight)

    result = []

    for q in queries:
        if q in weights:
            result.append("Yes")
        else:
            result.append("No")

    return result

if __name__ == '__main__':
    s = input()
    queries_count = int(input().strip())
    queries = []
    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)
    print(result)
