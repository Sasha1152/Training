class A:
    def __getattr__(self, item):
        return f'Class {__class__} has not attribute {item}'

a = A()
print(a.nonexistent_attr)