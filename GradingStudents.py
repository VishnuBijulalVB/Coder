def gradingStudents(grades):
    # Write your code here
    for i in range(grades_count):
        x = grades[i] % 5
        df = 5 - x
        if grades[i] >= 38:
            if df < 3:
                grades[i] = grades[i] + df
    return grades


grades_count = int(input("Enter no of students\n").strip())

grades = []

for _ in range(grades_count):
    grades_item = int(input("Enter marks\n").strip())
    grades.append(grades_item)

result = gradingStudents(grades)
print('\n'.join(map(str, result)))
