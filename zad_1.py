class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def is_passed(self):
        return sum(self.marks) / len(self.marks) > 50


student1 = Student("Jan", [50, 60, 70])
student2 = Student("Anna", [30, 40, 50])

print(student1.is_passed())
print(student2.is_passed())



