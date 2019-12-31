class User:
    def set_name(self, n):
         self.name = n

    def get_name(self):
        try:
            return print(self.name)
        except:
             print("No name")

first = User()
second = User()
first.set_name("Bob")
first.get_name()  # 'Bob'
second.get_name()  # 'No name'
