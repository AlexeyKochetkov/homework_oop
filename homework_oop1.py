class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
class Lecturer(Mentor):
    pass

lecturer1 = Lecturer('Name_lecturer1', 'Surname_lecturer1')
print(lecturer1.name)
print(lecturer1.surname)
print(lecturer1.courses_attached)

class Reviewer(Mentor):
    pass

reviewer1 = Reviewer('Name_reviewer1', 'Surname_reviewer1')
print(reviewer1.name)
print(reviewer1.surname)
print(reviewer1.courses_attached)
