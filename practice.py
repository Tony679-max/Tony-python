students_scores = [
    ("Yoctan", 85),
    ("Alice", 92),
    ("Sarah", 78),
    ("Omar", 90),
    ("Lina", 88)

]

student = {"name": "Yoctan", "age": 24}
unique_scores = {85, 92, 78, 90, 88}
student_details = ("Yoctan",24)
age = int("30")

print("students and scores:")
for student_name, score in students_scores:
    print(student_name, score)

    print("/nDictionary Yoctan :")
    print(student)

    print("/nScores uniques :")
    print(unique_scores)

    print("/nInformations tuple :")
    print(student_details)

    print("/nAge converti en nombre :")
    print(age)