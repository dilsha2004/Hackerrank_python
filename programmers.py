def dayOfProgrammer(year):
    if year == 1918:
        return "26.09.1918"
    if year < 1918:
        is_leap = (year % 4 == 0)
    else:
        is_leap = (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)
    day = "12" if is_leap else "13"
    return f"{day}.09.{year}"

if __name__ == '__main__':
    year = int(input().strip())
    result = dayOfProgrammer(year)
    print(result)