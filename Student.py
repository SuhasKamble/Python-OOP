class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
        
    def add_students(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def show_students(self):
        for student in self.students:
            print(f"{student.name} {student.age} {student.grade}")

    def get_average(self):
        value = 0 
        for student in self.students:
            value += student.get_grade()

        return value / len(self.students)        

s1 = Student("Suhas", 20, 30)
s2 = Student("Shinchan", 13, 20)
s2 = Student("Kabir", 23, 80)

course = Course("Computer Student", 2)
course.add_students(s1)
course.add_students(s2)
course.show_students()
print(course.get_average())