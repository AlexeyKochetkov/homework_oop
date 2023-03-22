from statistics import mean

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

    def rate_lc(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def avg_grades(self):
        score = []
        avg_score = dict()
        for key in self.grades.keys():
            avg_score[key] = mean(self.grades[key])
            score.append(self.grades[key])

        score_total=[]
        for sublist in score:
            for item in sublist:
                score_total.append(item)

        res = [mean(score_total), avg_score]
        return res
        
    def __str__(self):
        courses = []
        for key in self.grades.keys():
            courses.append(key)
        courses = ', '.join(courses)

        finished_courses = ', '.join(self.finished_courses)

        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.avg_grades()[0]} \
        \nСредняя оценка за домашние задания по курсам: {self.avg_grades()[1]} \
        \nКурсы в процессе изучения: {courses}\nЗавершенные курсы: {finished_courses}\n'
        return res
    
    def __lt__(self, other):
        if not isinstance(other, Student):
            return f'{other} - не является студентом!'
        else:
            if self.avg_grades()[0] > other.avg_grades()[0]:
                res = f'{self.name} {self.surname} - лучший студент с результатом: {self.avg_grades()[0]}'
            elif self.avg_grades()[0] < other.avg_grades()[0]:
                res = f'{other.name} {other.surname} - лучший студент с результатом: {other.avg_grades()[0]}'        
            else:
                res = f'Студенты {self.name} и {other.name} имеют равные результаты: {self.avg_grades()[0]}'
        return res
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def avg_grades(self):
        score = []
        avg_score = dict()
        for key in self.grades.keys():
            avg_score[key] = mean(self.grades[key])
            score.append(self.grades[key])

        score_total=[]
        for sublist in score:
            for item in sublist:
                score_total.append(item)

        res = [mean(score_total), avg_score]
        return res

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.avg_grades()[0]} \
        \nСредняя оценка за лекции по курсам: {self.avg_grades()[1]}\n'
        return res
    
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return f'{other} - не является лектором!'
        else:
            if self.avg_grades()[0] > other.avg_grades()[0]:
                res = f'{self.name} {self.surname} - лучший лектор с результатом: {self.avg_grades()[0]}'
            elif self.avg_grades()[0] < other.avg_grades()[0]:
                res = f'{other.name} {other.surname} - лучший лектор с результатом: {other.avg_grades()[0]}'        
            else:
                res = f'Лекторы {self.name} и {other.name} имеют равные результаты: {self.avg_grades()[0]}'
        return res

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
        res = f'Имя: {self.name}\nФамилия: {self.surname}\n'
        return res
        
some_student = Student('Ruoy', 'Eman', 'gender_student')
some_student.courses_in_progress += ['Python']
some_student.courses_in_progress += ['Git']
some_student.finished_courses += ['Введение в программирование']

some_student2 = Student('Ruoy2', 'Eman2', 'gender_student')
some_student2.courses_in_progress += ['Python']
some_student2.courses_in_progress += ['Git']
some_student2.finished_courses += ['Введение в программирование']
 
some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python']
some_reviewer.courses_attached += ['Git']
 
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Git', 6)

some_reviewer.rate_hw(some_student2, 'Python', 5)
some_reviewer.rate_hw(some_student2, 'Python', 8)
some_reviewer.rate_hw(some_student2, 'Git', 7)
some_reviewer.rate_hw(some_student2, 'Git', 5)


some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.courses_attached += ['Python']
some_lecturer.courses_attached += ['Git']

some_lecturer2 = Lecturer('Some2', 'Buddy2')
some_lecturer2.courses_attached += ['Python']
some_lecturer2.courses_attached += ['Git']
 
some_student.rate_lc(some_lecturer, 'Python', 8)
some_student.rate_lc(some_lecturer, 'Python', 9)
some_student.rate_lc(some_lecturer, 'Python', 9)
some_student.rate_lc(some_lecturer, 'Python', 6)
some_student.rate_lc(some_lecturer, 'Git', 10)

some_student.rate_lc(some_lecturer2, 'Python', 10)
some_student.rate_lc(some_lecturer2, 'Python', 10)
some_student.rate_lc(some_lecturer2, 'Git', 10)

print(some_reviewer)
print(some_lecturer)
print(some_lecturer2)
print(some_student)
print(some_student2)
print(some_student.__lt__(some_student2))
print(some_lecturer.__lt__(some_lecturer2))