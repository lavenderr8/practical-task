def calculate_average(grades):
    return sum(grades) / len(grades)


def calculate_overall_average(students):
    sums = [sum(student['grades']) for student in students]
    count = sum(len(student['grades']) for student in students)
    total_sum = sum(sums)
    return total_sum / count if count else 0


def get_lowest_student_index(students):
    if not students:
        return None
    averages = [calculate_average(student['grades']) for student in students]
    return averages.index(min(averages))


def print_students_info(students):
    for student in students:
        average = calculate_average(student['grades'])
        status = "Успешный" if average >= 75 else "Отстающий"
        print(f"Студент: {student['name']}",
              f"Средний балл: {average:.2f};",
              f"Статус: {status}",
              sep="\n", end="\n\n")
    print(f"Общий средний балл: {calculate_overall_average(students):.2f}\n")


def add_student(students, name, grades):
    new_student = {"name": name, "grades": grades}
    students.append(new_student)
    print(f"Добавлен новый студент: {new_student}",
          f"Общий средний балл: {calculate_overall_average(students):.2f}",
          sep="\n", end="\n\n")


def remove_student(students, index):
    if 0 <= index < len(students):
        removed = students.pop(index)
        print(f"Удалён самый отстающий студент: {removed['name']}\n")
        print_students_info(students)
    else:
        print("Ошибка: неверный индекс.")


students = [
    {"name": "Catelyn Stark", "grades": [86, 55, 73, 69]},
    {"name": "Daenerys Targaryen", "grades": [79, 88, 90, 92]},
    {"name": "Jorah Mormont", "grades": [50, 99, 91, 91]},
    {"name": "Khal Drogo", "grades": [81, 99, 66, 80]},
    {"name": "Sandor Clegane", "grades": [50, 100, 75, 83]},
    {"name": "Tyrion Lannister", "grades": [84, 63, 92, 97]},
]

print_students_info(students)

add_student(students, "Jon Snow", [85, 94, 95, 96])

lowest_index = get_lowest_student_index(students)
if lowest_index is not None:
    print(f"Самый отстающий студент: {students[lowest_index]['name']}")
    remove_student(students, lowest_index)
