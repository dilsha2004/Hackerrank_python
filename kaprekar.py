def kaprekarNumbers(p, q):
    results = []
    for n in range(p, q+1):
        square = n * n
        d = len(str(n))
        square_str = str(square)
        
        r = square_str[-d:]
        l = square_str[:-d] if len(square_str) > d else "0"
        
        if int(l) + int(r) == n:
            results.append(n)
    
    if results:
        print(' '.join(map(str, results)))
    else:
        print("INVALID RANGE")

if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)
    print(kaprekarNumbers)