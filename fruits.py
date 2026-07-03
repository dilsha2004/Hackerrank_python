def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple_count = 0
    orange_count = 0
    
    for d in apples:
        fall = a+d
        if s<=fall<=t:
            apple_count += 1
            
    for d in oranges:
        fall = b+d
        if s<=fall<=t:
            orange_count += 1
            
    print(apple_count)
    print(orange_count)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    s = int(first_multiple_input[0])
    t = int(first_multiple_input[1])
    second_multiple_input = input().rstrip().split()
    a = int(second_multiple_input[0])
    b = int(second_multiple_input[1])
    third_multiple_input = input().rstrip().split()
    m = int(third_multiple_input[0])
    n = int(third_multiple_input[1])
    apples = list(map(int, input().rstrip().split()))
    oranges = list(map(int, input().rstrip().split()))
    countApplesAndOranges(s, t, a, b, apples, oranges)
