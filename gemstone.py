def gemstones(arr):
    common = set(arr[0])

    for rock in arr[1:]:
        common = common & set(rock)

    return len(common)

if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)
    result = gemstones(arr)
    print(result)
    