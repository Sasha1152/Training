class Humans(object):
    def __init__(self, name, surname, age, gender):
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender

    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname

    def get_age(self):
        return self.age

    def get_gender(self):
        return self.gender

user = Humans('Sasha', 'Shmigelskii', '35', 'man')

print(user.get_name())
print(user.get_age())

class Students(Humans):
    def __init__(self, name, surname, age, gender, list_marks):
        super(Students, self).__init__(name, surname, age, gender)
        self.list_marks = list_marks

    def get_average_mark(self):
        return reduce(lambda x, y: x + y, self.list_marks) / len(self.list_marks)

student1 = Students('Alex', 'Bolduin', '65', 'man',
                    [5, 4, 6, 9, 3, 10, 7])
print('the student1 have name ' + str(student1.get_name()))
print ('Average mark for student1 is: ' +
       str(student1.get_average_mark()))

class Teachers(Humans):
    def __init__(self, name, surname, age, gender, group):
        super(Teachers, self).__init__(name, surname, age, group)
        self.group = group

    def get_number_group(self):
        return self.group

teacher1 = Teachers('Mary', 'Popens', '28', 'woman', '1-A')
print('the teacher1 have name ' + str(teacher1.get_name()))
print ('teacher1 is from ' +
       str(teacher1.get_number_group())
       + ' class')

