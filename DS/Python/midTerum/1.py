print("I said \"I\'m studying\"")
students = ["inhoe", "yesong", "jaewook", "yeha", "suun", "nayeon"]
students.insert(2,'hi')
print(students)

digits = set([0, 1, 2, 3, 4, 5])
odds = set([1, 3, 5, 7, 9])
# digits.add(6)
# digits.remove(2)
# digits.clear()
print(digits.issubset(odds))

dict_grades = {"inhoe": "A", "yesong": "A+", "jaewook": "A++"}
print(dict_grades.values())