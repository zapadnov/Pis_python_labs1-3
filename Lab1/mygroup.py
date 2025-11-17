groupmates = [
    {
        "name": "Банчук",
        "surname": "Андрей",
        "exams": ["КТП", "ЭЭиС", "Web"],
        "marks": [5, 3, 3]
    },
    {
        "name": "Волков",
        "surname": "Вячеслав",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [3, 3, 3]
    },
    {
        "name": "Кожевникова",
        "surname": "Светлана",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [3, 5, 3]
    },
    {
        "name": "Линчук",
        "surname": "Богдан",
        "exams": ["Русский язык", "ИС", "КТП"],
        "marks": [3, 3, 3]
    },
    {
        "name": "Мамедбеков",
        "surname": "Руслан",
        "exams": ["Алгебра", "ИС", "КТП"],
        "marks": [5, 4, 5]
    }
]
def calc_mean(scores):
    """Простая функция для подсчёта среднего балла по списку оценок."""
    return sum(scores) / len(scores)


def show_students(table):
    """Печатает табличку со студентами и их средними баллами."""

    # шапка таблицы, ширину колонок задаю через форматирование
    header = "{:<12}{:<15}{:<38}{:<18}{}".format(
        "Имя", "Фамилия", "Экзамены", "Оценки", "Средний"
    )
    print(header)
    print("-" * len(header))  # черта под заголовком

    # обрабатываем каждого студента по очереди
    for student in table:
        # exams и marks берём из словаря и приводим к удобному виду
        exams_line = ", ".join(student["exams"])
        marks_line = " ".join(str(mark) for mark in student["marks"])
        mean_value = calc_mean(student["marks"])

        row = "{:<12}{:<15}{:<38}{:<18}{:5.2f}".format(
            student["name"],
            student["surname"],
            exams_line,
            marks_line,
            mean_value
        )
        print(row)


def filter_students_by_avg(students, min_value):
    """
    Собирает тех студентов, у кого средний балл
    строго выше указанного порога min_value.
    """
    filtered = []

    for student in students:
        if calc_mean(student["marks"]) > min_value:
            filtered.append(student)

    return filtered


if __name__ == "__main__":
    try:
        # просим пользователя ввести порог для среднего балла
        border_value = float(input("Введите минимальный средний балл: "))
    except ValueError:
        # если пользователь ввёл текст вместо числа, ловим ошибку
        print("Ошибка ввода: нужно ввести число, например 4.0")
    else:
        # отбираем подходящих по порогу студентов
        result = filter_students_by_avg(groupmates, border_value)

        if result:
            print(f"\nСтуденты с средним баллом выше {border_value}:\n")
            show_students(result)
        else:
            print("Никто не набрал такой средний балл.")