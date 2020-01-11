# https://younglinux.info/oopython/objects.php

class User:
    def set_name(self, n):
        print('setter works!')
        self.name = n

    def get_name(self):
        print('getter works!')
        try:
            return print(self.name)
        except:
             print("No name")

first = User()
second = User()
first.set_name("Bob")
first.m = 5
first.get_name()  # 'Bob'
second.get_name()  # 'No name'
