grades = {"inhoe":"A","yesong":"A+","jaewook":"A","hyung-sin":"C"}

grades_inv={}
for student, grade in grades.items():
    grades_inv.setdefault(grade,[])
    grades_inv[grade].append(student)
print(grades_inv)