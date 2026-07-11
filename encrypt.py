import math

def encryption(s):
    s = s.replace(" ", "")
    L = len(s)
    
    rows = math.floor(math.sqrt(L))
    cols = math.ceil(math.sqrt(L))
    
    
    if rows * cols < L:
        rows += 1
    
    result = []
    for c in range(cols):
        word = ""
        for r in range(rows):
            index = r * cols + c
            if index < L:
                word += s[index]
        result.append(word)
    
    return " ".join(result)

if __name__ == '__main__':
    s = input()
    result = encryption(s)
    print(result)