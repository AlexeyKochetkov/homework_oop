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
        
    def __str__(self):
        score = []
        for key in self.grades.keys():
            score.append(self.grades[key])
        #print(score)

        score_total=[]
        for sublist in score:
            for item in sublist:
                score_total.append(item)
        #print(score_total)

        courses = []
        for key in self.grades.keys():
            courses.append(key)
        courses = ', '.join(courses)

        finished_courses = ', '.join(self.finished_courses)

        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {mean(score_total)} \
        \nКурсы в процессе изучения: {courses}\nЗавершенные курсы: {finished_courses}'
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

    def __str__(self):
        score = []
        for key in self.grades.keys():
            score.append(self.grades[key])
        #print(score)

        score_total=[]
        for sublist in score:
            for item in sublist:
                score_total.append(item)
        #print(score_total)

        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {mean(score_total)}\n'
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
 
some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python']
some_reviewer.courses_attached += ['Git']
 
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Git', 6)


some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.courses_attached += ['Python']
some_lecturer.courses_attached += ['Git']
 
some_student.rate_lc(some_lecturer, 'Python', 8)
some_student.rate_lc(some_lecturer, 'Python', 9)
some_student.rate_lc(some_lecturer, 'Python', 9)
some_student.rate_lc(some_lecturer, 'Python', 6)
some_student.rate_lc(some_lecturer, 'Git', 10)

print(some_reviewer)
print(some_lecturer)
print(some_student)