vowels = {"a","b","a"}
print(vowels)

grades ={"inhoe":"A","yesong":"A+","jaewook":"A","hyung-sin":"C"}
new_dict1 = {}
new_dict2 = {}
for key in grades:
    new_dict1.setdefault(grades[key],key)

for key in grades:
    new_dict2[grades[key]] = grades.pop(key,grades[key])
print(new_dict1)
print(new_dict2)