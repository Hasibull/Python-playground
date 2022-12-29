
student: dict = {
    'name': 'Hasibul',
    'education': 'B.Sc',
    'age': 24
}

student['height'] = 5.8

print(student)

new_student = student.copy() ## creates different memory location

print(id(new_student))
print(id(student))
