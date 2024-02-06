M = "Male"
F = "Female"

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.clases_ranks:
                lecturer.clases_ranks[course] += [grade]
            else:
                lecturer.clases_ranks[course] = [grade]
        else:
            return 'Ошибка'
    def get_courses_in_progress(self):
        return ', '.join(self.courses_in_progress)

    def get_finished_courses(self):
        return', '.join(self.finished_courses)
    def get_av_grades(self):
        av_rate = []
        for grade in self.grades.values():
            av_rate.extend(grade)
        if len(av_rate) == 0:
            return 0
        return  sum(av_rate) / len(av_rate)

    def get_course_rank(self,course):
        return sum(n for n in self.grades[course])

    def __str__(self):
       return f'''Имя: {self.name} \nФамилия:{self.surname}
        Средняя оценка за домашние задания:{self.get_av_grades()}
        Курсы в процессе изучения: {self.get_courses_in_progress()}
        Завершенные курсы: {self.get_finished_courses()}'''

    def __eq__(self, other):
        return True if self.get_av_grades() == other.get_av_grades() else False
    def __lt__(self, other):
        return True if self.get_av_grades() < other.get_av_grades() else False
    def __le__(self, other):
        return True if self.get_av_grades() <= other.get_av_grades() else False
class Mentor:
    def __init__(self, name, surname, courses_attached = []):
        self.name = name
        self.surname = surname
        self.courses_attached = courses_attached
class Lecturer (Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.clases_ranks ={}
        self.av_ranks = 0

    def get_av_rank(self):
        n =[]
        for ranks in self.clases_ranks.values():
            n.extend(ranks)
        return sum(n) / len(n) if len(n) != 0 else 0
    def get_course_rank(self, course):
        return sum([n  for n in self.clases_ranks[course]])

    def set_av_rank(self):
        self.average_rank = self.get_av_rank()
        return self.get_av_rank()


    def __str__(self):
        return (f'Имя: {self.name} \nФамилия:{self.surname} \nСредняя оценка за лекции: {self.get_av_rank()}')

    def __eq__(self, other):
        return True if self.get_av_rank() == other.get_av_rank() else False
    def __lt__(self, other):
        return True if self.get_av_rank() < other.get_av_rank() else False
    def __le__(self, other):
        return True if self.get_av_rank() <= other.get_av_rank() else False
class Reviewer (Mentor):
    def rate_hw(self, student, course, grade):
        if not isinstance(student,
                          Student) or course not in self.courses_attached or course not in student.courses_in_progress:
            return 'Ошибка'
        else:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]

    def __str__(self):
        return f'Имя: {self.name} \nФамилия:{self.surname}'

def student_hw_av_garde(students, course):
    result = 0
    for student in students:
        if course in student.courses_in_progress:
            result += student.get_course_rank(course)
    return result / len(students)

def lecturer_hw_av_garde(lecturers, course):
    result =0
    for lecturer in lecturers:
        result += lecturer.get_course_rank(course)
    return result / len(lecturers)

student1 = Student('Vladimir', 'Ogoltsov',  M)
student2 = Student('Daria', 'Belyakova', F)
student1.finished_courses = ['Python']
student1.finished_courses = ['Fuck', 'Python']
student1.courses_in_progress = ['Fuck','Python','rrr']
student2.finished_courses = ['Python']
student2.courses_in_progress = ['Python']
lector2 = Lecturer('Natalia', 'Nakonechna')
lector1 = Lecturer('Anna','Dovgal')
lector1.courses_attached = ['Python','Exel', 'Fuck']
lector2.courses_attached = ['Python','Exel', 'Fuck']

reviewer1 = Reviewer('Don', 'Felipe')
reviewer1.courses_attached = ['Python', 'Exel', 'Fuck']
reviewer1.rate_hw(student1,'Python', 10)
reviewer1.rate_hw(student1,'Python', 9)
reviewer1.rate_hw(student1,'Python', 27)
reviewer1.rate_hw(student1,'Fuck', 100)
reviewer1.rate_hw(student2,'Python', 90)
reviewer1.rate_hw(student1,'Fuck', 45)
reviewer1.rate_hw(student2, 'Exel', 5)
student1.rate_lecturer(lector1,'Python',567)
student1.rate_lecturer(lector1,'Python',333)
student1.rate_lecturer(lector1,'Fuck',567)
student1.rate_lecturer(lector1,'Fuck',567)
student1.rate_lecturer(lector2,'Fuck',45)

# print(student1)
# print(student1.get_courses_in_progress())
# print(student1.get_finished_courses())
# print(student1.grades)
#print("Lector1 clases_ranks",lector1.clases_ranks)
# print('course rank',student1.get_course_rank('Python'))
# print('course rank',student2.get_course_rank('Python'))
# print(lector1)
# print(reviewer1)
# print(student_hw_av_garde([student1, student2], 'Python'))
#print(lector1.get_course_rank('Python'))
#print(lector1.get_course_rank('Python'))
print(lector1.get_av_rank(),lector2.get_av_rank())
print(lector2 == lector1)
print('Lector1',lector1)
print('Lector2', lector2)
print('Lector1',lector1.clases_ranks)
print('Lector2', lector2.clases_ranks)

