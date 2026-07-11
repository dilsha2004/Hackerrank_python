def biggerIsGreater(w):
    chars = list(w)
    n = len(chars)
    i = n - 2
    while i >= 0 and chars[i] >= chars[i+1]:
        i -= 1
    
    if i < 0:
        return "no answer"
    
    j = n - 1
    while chars[j] <= chars[i]:
        j -= 1
    
    chars[i], chars[j] = chars[j], chars[i]
    chars[i+1:] = reversed(chars[i+1:])
    return "".join(chars)

if __name__ == '__main__':
    T = int(input().strip())
    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)
        print(result)
