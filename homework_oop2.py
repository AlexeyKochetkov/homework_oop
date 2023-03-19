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
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

class Reviewer(Mentor):
    
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
student1 = Student('Name_student1', 'Surname_student1', 'gender_student1')
student1.courses_in_progress += ['Python']
 
reviewer1 = Reviewer('Name_reviewer1', 'Surname_reviewer1')
reviewer1.courses_attached += ['Python']
 
reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 10)
 
print(student1.grades)

lecturer1 = Lecturer('Name_lecturer1', 'Surname_lecturer1')
lecturer1.courses_attached += ['Python']
 
student1.rate_lc(lecturer1, 'Python', 8)
student1.rate_lc(lecturer1, 'Python', 9)
student1.rate_lc(lecturer1, 'Python', 9)
student1.rate_lc(lecturer1, 'Python', 6)
 
print(lecturer1.grades)