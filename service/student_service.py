from model.student import Student

from json import JSONEncoder

class MyEncoder(JSONEncoder):
    def default(self, obj):
        return obj.__dict__

class StudentService():

    def __init__(self):
        self.students=[]
        self.students.append(Student("1222223",
                                     "Carlos Loaiza", 20000, "M", True, "3016052808"))

        self.students.append(Student("34434343",
                                     "Pedro Pérez",
                                     230000, "M", True, "44343434343"))
        self.students.append(Student("34434343",
                                     "Catherine Betancurt",
                                     0, "F", True, "3137844909"))
    def getAllStudents(self):

        return self.students
    def get_percentage_by_gender(self,gender):
        count=0
        for student in self.students:
            if student.gender==gender:
                count+=1
            return count/len(self.students)

    def get_students_by_gender_and_salary(self, gender, salary):
        students_by_gender_and_salary = []
        for student in self.students:
            if student.job and student.gender == gender and student.salary >= salary:
                students_by_gender_and_salary.append(student)
        return students_by_gender_and_salary

    def get_students_between_salaries(self,min_salary, max_salary):
        students_between_salaries=[]
        for student in self.students:
            if student.job and student.salary >= min_salary and student.salary <= max_salary:
                students_between_salaries.append(student)
            return students_between_salaries

    def get_mayor_salaries(self):
        mayor_salaries=[]
        M_student=None
        F_student=None
        for student in self.students:
            if student.job:
                if student.gender=='M' and M_student == None or student.gender=='M' and student.salary > M_student.salary:
                    M_student=student

                if student.gender=='F' and F_student == None or student.gender=='F' and student.salary > F_student.salary:
                    F_student=student
        if M_student!=None:
            mayor_salaries.add(M_student)
        if F_student!=None:
            mayor_salaries.add(F_student)

        return mayor_salaries













