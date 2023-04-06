student_scores = {
    "Person1" : 98,
    "Person2" : 68,
    "Person3" : 78, 
    "Person4" : 96,
    "Person5" : 58,
}

#write a program that creates a dictionary called student_grade from the student_scores dictionary, that has grade 1 for 90+, 2 for 80+ etc.

student_grades = student_scores

for student in student_grades:
    if student_scores[student] >= 90:
        student_grades[student] = 1
    elif student_scores[student] >= 80 and student_scores[student]<90:
        student_grades[student] = 2
    elif student_scores[student] >= 70 and student_scores[student]<80:
        student_grades[student] = 3
    else: student_grades[student] = 4

for student in student_grades:
    print(f"Student: {student}, Grade: {student_grades[student]}")