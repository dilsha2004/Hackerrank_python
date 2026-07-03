def gradingStudents(grades):
    result = []
    for g in grades:
        if g < 38:
           result.append(g)
        else:
            multiple = g + (5- g % 5) 
            if multiple - g < 3:
                result.append(multiple)
            else:
                result.append(g)
    return result

if __name__ == '__main__':
    grades_count = int(input().strip())
    grades = []
    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)
    result = gradingStudents(grades)
    print(result)
