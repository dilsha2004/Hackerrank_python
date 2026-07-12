def timeInWords(h, m):
    words = ["zero", "one", "two", "three", "four", "five", "six",
             "seven", "eight", "nine", "ten", "eleven", "twelve",
             "thirteen", "fourteen", "quarter", "sixteen",
             "seventeen", "eighteen", "nineteen", "twenty",
             "twenty one", "twenty two", "twenty three",
             "twenty four", "twenty five", "twenty six",
             "twenty seven", "twenty eight", "twenty nine", "half"]

    if m == 0:
        return words[h] + " o' clock"
    elif m == 15:
        return "quarter past " + words[h]
    elif m == 30:
        return "half past " + words[h]
    elif m == 45:
        return "quarter to " + words[h + 1]
    elif m < 30:
        if m == 1:
            return "one minute past " + words[h]
        return words[m] + " minutes past " + words[h]
    else:
        m = 60 - m
        if m == 1:
            return "one minute to " + words[h + 1]
        return words[m] + " minutes to " + words[h + 1]

if __name__ == '__main__':
    h = int(input().strip())
    m = int(input().strip())
    result = timeInWords(h, m)
    print(result)