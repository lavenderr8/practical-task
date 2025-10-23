def calculate_average(grades):
    average_value = sum(grades) / len(grades)
    return average_value


def calculate_overall_average(students):
    all_grades = [grade for student in students for grade in student["grades"]]
    return sum(all_grades) / len(all_grades) if all_grades else 0


students = [
    {"name": "Catelyn Stark", "grades": [86, 55, 73, 69]},
    {"name": "Daenerys Targaryen", "grades": [79, 88, 90, 92]},
    {"name": "Jorah Mormont", "grades": [50, 99, 91, 91]},
    {"name": "Khal Drogo", "grades": [81, 99, 66, 80]},
    {"name": "Sandor Clegane", "grades": [50, 100, 75, 83]},
    {"name": "Tyrion Lannister", "grades": [84, 63, 92, 97]},
]

for student in students:
    average = calculate_average(student["grades"])
    status = "Успешный" if average >= 75 else "Отстающий"
    print(f"Студент: {student['name']}", f"Средний балл: {average:.2f};", f"Статус: {status}", sep="\n", end="\n\n")

print(f"Общий средний балл: {calculate_overall_average(students):.2f}\n")

new_student = {"name": "Jon Snow", "grades": [85, 94, 95, 96]}
students.append(new_student)
print(f"Добавлен новый студент: {students[6]}", f"Общий средний балл: {calculate_overall_average(students):.2f}",
      sep="\n")

print(f"\nУдалён студент: {students.pop(0)}", f"Общий средний балл: {calculate_overall_average(students):.2f}",
      sep="\n")
