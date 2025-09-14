class Student:
    def __init__(self, student_name):
        self.student_name = student_name

class Classroom:
    def __init__(self, class_number):
        self.class_number = class_number
        self.students_list = []
    
    def add_students(self, *args):
        for student in args:
            self.students_list.append(student)
    
    def print_students(self):
        if self.students_list:
            print(f'Студенти в класі під номером {self.class_number}:')
            for num, pupil in enumerate(self.students_list):
                print(f'{num+1}. {pupil.student_name}')
            print(f'\nВсього студентів у класі: {len(self.students_list)}')
        else:
            print(f'Клас під номером {self.class_number} пустий.')

maria = Student('Maria')
petro = Student('Petro')
olena = Student('Olena')

room = Classroom('410')

room.add_students(maria, petro, olena)

room.print_students()