def palindromeIndex(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:


            temp = s[left + 1:right + 1]
            if temp == temp[::-1]:
                return left

    
            temp = s[left:right]
            if temp == temp[::-1]:
                return right

            return -1

        left += 1
        right -= 1

    return -1
if __name__ == '__main__':
    q = int(input().strip())
    for q_itr in range(q):
        s = input()
        result = palindromeIndex(s)
        print(result)