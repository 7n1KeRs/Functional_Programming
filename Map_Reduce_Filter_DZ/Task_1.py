from functools import reduce

students = [
    {"name": "Alice", "age": 20, "grades": [85, 90, 88, 92]},
    {"name": "Bob", "age": 22, "grades": [78, 89, 76, 85]},
    {"name": "Charlie", "age": 21, "grades": [92, 95, 88, 94]},
    {"name": "David", "age": 20, "grades": [70, 75, 80, 65]},
    {"name": "Eva", "age": 23, "grades": [88, 92, 85, 90]},
    {"name": "Frank", "age": 22, "grades": [60, 65, 70, 55]},
    {"name": "Grace", "age": 21, "grades": [95, 98, 92, 96]},
    {"name": "Henry", "age": 20, "grades": [82, 84, 88, 80]},
    {"name": "Ivy", "age": 23, "grades": [75, 78, 72, 80]},
    {"name": "Jack", "age": 22, "grades": [90, 85, 88, 92]},
    {"name": "Kate", "age": 21, "grades": [68, 72, 65, 70]},
    {"name": "Leo", "age": 20, "grades": [89, 91, 94, 87]},
    {"name": "Mia", "age": 23, "grades": [93, 96, 90, 95]},
    {"name": "Noah", "age": 22, "grades": [77, 80, 75, 82]},
    {"name": "Olivia", "age": 21, "grades": [85, 88, 82, 90]},
    {"name": "Paul", "age": 20, "grades": [72, 68, 75, 70]},
    {"name": "Quinn", "age": 23, "grades": [91, 89, 94, 92]},
    {"name": "Rose", "age": 22, "grades": [80, 82, 78, 85]},
    {"name": "Sam", "age": 21, "grades": [65, 70, 68, 72]},
    {"name": "Tina", "age": 20, "grades": [87, 90, 85, 89]}
]

filtered_students = list(filter(lambda s: s["age"] == 20, students))
print(f"Студентов возраста 20: {len(filtered_students)}")

student_averages = list(map(
    lambda s: (s["name"], sum(s["grades"]) / len(s["grades"])), 
    students
))

overall_average = reduce(lambda acc, val: acc + val[1], student_averages, 0) / len(student_averages)
print(f"Общий средний балл: {overall_average:.2f}")

best_student = reduce(
    lambda best, current: current if current[1] > best[1] else best,
    student_averages
)
print(f"Лучший студент: {best_student[0]} и ее балл: {best_student[1]:.2f}")
