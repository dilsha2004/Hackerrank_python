def superReducedString(s):
    stack = []

    for ch in s:
        if stack and stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)

    if stack:
        return "".join(stack)
    else:
        return "Empty String"
        
if __name__ == '__main__':
    s = input()
    result = superReducedString(s)
    print(result)
