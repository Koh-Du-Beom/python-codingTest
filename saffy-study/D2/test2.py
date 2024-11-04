students = [(10, 1), (20, 2), (15, 3), (8, 4)]
students = sorted(students, key=lambda x : -x[0])

selected_student = students.index()