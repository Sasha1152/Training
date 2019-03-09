class Student:
    average_mark = 50

    def __init__(self, mark):
        self.mark = mark

    def get_stepend(self):
        if self.mark > self.average_mark:
            return True
        return False

stud1 = Student(60)
stud2 = Student(50)

print(stud1.get_stepend())
print(stud2.get_stepend())
print(Student.average_mark)
print(stud1.average_mark)
