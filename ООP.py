class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def average_rating_student(self):
        student_rate = 0
        len_rate = 0
        for course, rate in self.grades.items():
            student_rate += sum(rate)
            len_rate += len(rate)
        return round(student_rate / len_rate, 1)


    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades_lecturer:
                lecturer.grades_lecturer[course] += [grade]
            else:
                lecturer.grades_lecturer[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.average_rating_student()}' \
              f'\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}' \
              f'\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Не является студентом")
            return
        return self.average_rating_student() < other.average_rating_student()


student = Student('Ruoy', 'Eman', 'your_gender')
student2 = Student('Ruoy2', 'Eman2', 'your_gender2')
student.finished_courses += ['Введение в программирование']
student2.finished_courses += ['Введение в программирование']
student.courses_in_progress += ['Python', "Git"]
student2.courses_in_progress += ['Python', "Git"]
student.grades['Python'] = [8, 7, 10, 5]
student.grades['Git'] = [10, 5, 9]
student2.grades['Python'] = [10, 9, 4]
student2.grades['Git'] = [9, 5, 8]
student_list = [student, student2]

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades_lecturer = {}


class Lecturer(Mentor):
    def average_rating_lecturer(self):
        average_rate = 0
        len_rate = 0
        for course, rate in self.grades_lecturer.items():
            average_rate += sum(rate)
            len_rate += len(rate)
        return round(average_rate / len_rate, 1)


    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.average_rating_lecturer()}'
        return res


    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Не является лектором")
            return
        return self.average_rating_lecturer() > lecturer2.average_rating_lecturer()

lecturer = Lecturer('Some', 'Buddy')
lecturer2 = Lecturer('Some2', 'Buddy2')
lecturer.courses_attached += ['Python', "Git"]
lecturer2.courses_attached += ['Python', "Git"]
lecturer.grades_lecturer['Python'] = [9, 7, 8, 10]
lecturer.grades_lecturer["Git"] = [9, 10, 8]
lecturer2.grades_lecturer['Python'] = [10, 7, 3, 5, 8]
lecturer2.grades_lecturer["Git"] = [9, 7, 8, 2, 10]
lecturer_list = [lecturer, lecturer2]

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res


reviewer = Reviewer('Some', 'Buddy')
reviewer.rate_hw(student, 'Python', 10)
reviewer.rate_hw(student, 'Python', 10)
reviewer.rate_hw(student, 'Python', 10)


print()
print(reviewer)
print()
print(lecturer)
print()
print(student)
print()
print(f"Средняя оценка student = '{student.average_rating_student()}' "
                         f" и  средняя оценка student2 = '{student2.average_rating_student()}'")
print(f"Средняя оценка lecturer = '{lecturer.average_rating_lecturer()}' "
                         f" и  средняя оценка lecturer2 = '{lecturer2.average_rating_lecturer()}'")
print()

# Задание 4

def average_grade_homework(student_list, course_name=''):
    student_rate = 0
    len_rate = 0
    for student in student_list:
        for name_course, rate in student.grades.items():
            if name_course == course_name:
                student_rate += sum(rate)
                len_rate += len(rate)
    print(f"Средня оценка по всем студентам по курсу '{course_name}': {round(student_rate / len_rate, 1)}")

# чтобы посмотреть среднюю оценку по другому курсу, нужно присвоить аргументу функции название этого курса
# ('Python' или 'Git')
average_grade_homework(student_list, course_name='Python')


def average_grade_lecture(lecturer_list, course_name=''):
    lecturer_rate = 0
    len_rate = 0
    for lecturer in lecturer_list:
        for name_course, rate in lecturer.grades_lecturer.items():
            if name_course == course_name:
                lecturer_rate += sum(rate)
                len_rate += len(rate)
    print(f"Средня оценка по всем лекциям по курсу '{course_name}': {round(lecturer_rate / len_rate, 1)}")

# чтобы посмотреть среднюю оценку по другому курсу, нужно присвоить аргументу функции название этого курса
# ('Python' или 'Git')
average_grade_lecture(lecturer_list, course_name = 'Git')

