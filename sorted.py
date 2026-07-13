def almostSorted(arr):
    s = sorted(arr)

    if arr == s:
        print("yes")
        return

    diff = []

    for i in range(len(arr)):
        if arr[i] != s[i]:
            diff.append(i)

    if len(diff) == 2:
        print("yes")
        print("swap", diff[0] + 1, diff[1] + 1)
        return

    l = diff[0]
    r = diff[-1]

    temp = arr[:]
    temp[l:r+1] = temp[l:r+1][::-1]

    if temp == s:
        print("yes")
        print("reverse", l + 1, r + 1)
    else:
        print("no")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)
    print(almostSorted)