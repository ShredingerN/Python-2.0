import csv


class NameDescriptor:
    def __get__(self, instance, owner):
        return instance._name

    def __set__(self, instance, value):
        if not value.replace(' ', '').isalpha() or not value.istitle():
            raise ValueError("ФИО должно состоять только из букв и начинаться с заглавной буквы")
        instance._name = value


class Student:
    name = NameDescriptor()

    def __init__(self, name, subjects_file):
        self._name = name
        self._subjects = {}
        self.load_subjects(subjects_file)

    def __str__(self):
        subjects_with_data = [subject for subject, data in self._subjects.items() if
                              data['grades'] or data['test_scores']]
        return f"Студент: {self.name}\nПредметы: {', '.join(subjects_with_data)}"

    # если предметы перечислены в строку через запятую
    # def load_subjects(self, subjects_file):
    #     with open(subjects_file, 'r', encoding='utf-8') as f:
    #         line = f.readline().strip()  # Читаем первую строку и удаляем лишние пробелы
    #         subjects = line.split(",")  # Разделяем предметы по запятой
    #         for subject in subjects:
    #             if subject not in self._subjects:
    #                 self._subjects[subject] = {'grades': [], 'test_scores': []}
    # предметы перечислены в столбец, метод проходит по линиям

    def load_subjects(self, subjects_file):
        with open(subjects_file, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                subject = row[0]
                if subject not in self._subjects:
                    self._subjects[subject] = {'grades': [], 'test_scores': []}

    def add_grade(self, subject, grade):
        if subject not in self._subjects:
            raise ValueError(f"Предмет {subject} не найден")
        if not isinstance(grade, int) or grade < 2 or grade > 5:
            raise ValueError("Оценка должна быть целым числом от 2 до 5")
        self._subjects[subject]['grades'].append(grade)

    def add_test_score(self, subject, test_score):
        if subject not in self._subjects:
            raise ValueError(f"Предмет {subject} не найден")
        if not isinstance(test_score, int) or test_score < 0 or test_score > 100:
            raise ValueError("Результат теста должен быть целым числом от 0 до 100")
        self._subjects[subject]['test_scores'].append(test_score)

    def get_average_test_score(self, subject):
        if subject not in self._subjects:
            raise ValueError(f"Предмет {subject} не найден")
        test_scores = self._subjects[subject]['test_scores']
        if len(test_scores) == 0:
            return 0
        return sum(test_scores) / len(test_scores)

    def get_average_grade(self):
        total_grades = []
        for subject in self._subjects:
            grades = self._subjects[subject]['grades']
            if len(grades) > 0:
                total_grades.extend(grades)
        if len(total_grades) == 0:
            return 0
        return sum(total_grades) / len(total_grades)


# Пример использования:
student = Student("Иван Иванов", "subjects.csv")

student.add_grade("Математика", 4)
student.add_test_score("Математика", 85)

student.add_grade("История", 5)
student.add_test_score("История", 92)

student.add_grade("Литература", 5)
student.add_test_score("Литература", 92)

# student.add_grade("Химия", 5)
# student.add_test_score("Химия", 92)

average_grade = student.get_average_grade()
print(f"Средний балл: {average_grade}")

average_test_score = student.get_average_test_score("Математика")
print(f"Средний результат по тестам по математике: {average_test_score}")

print(student)
