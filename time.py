def timeConversion(s):
    period = s[-2:]
    hour = int(s[:2])
    rest = s[2:-2]
    
    if period == "AM" and hour == 12:
        hour = 0
    elif period == "PM" and hour != 12:
        hour += 12
    return f"{hour:02d}"+ rest
if __name__ == '__main__':
    s = input()
    result = timeConversion(s)
    print(result)
