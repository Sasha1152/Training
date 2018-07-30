class User:
    def setName(self, n):
         self.name = n
    def getName(self):
        try:
            return print(self.name)
        except:
             print("No name")

first = User()
second = User()
first.setName("Bob")
first.getName()  # 'Bob'
second.getName()  # 'No name'