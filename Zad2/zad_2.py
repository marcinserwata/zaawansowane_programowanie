from book import Book
from employee import Employee
from library import Library
from order import Order
from student import Student

library1 = Library("Warsaw", "Marszalkowska", "00-001", "8:00-20:00", "123456789")
library2 = Library("Krakow", "Krakowska", "00-002", "9:00-21:00", "987654321")

book1 = Book(library1, "2020-01-01", "John", "Doe", 100)
book2 = Book(library1, "2020-02-01", "Jane", "Doe", 200)
book3 = Book(library1, "2020-03-01", "Jack", "Smith", 300)
book4 = Book(library2, "2020-04-01", "Jill", "Smith", 400)
book5 = Book(library2, "2020-05-01", "Jim", "Brown", 500)

employee1 = Employee("John", "Doe", "2020-01-01", "1990-01-01", "Warsaw", "Marszalkowska", "00-001", "123456789")
employee2 = Employee("Jane", "Doe", "2020-02-01", "1991-01-01", "Krakow", "Krakowska", "00-002", "987654321")
employee3 = Employee("Jack", "Smith", "2020-03-01", "1992-01-01", "Warsaw", "Marszalkowska", "00-001", "123456789")

student1 = Student("Student1", [50, 60, 70])
student2 = Student("Student2", [30, 40, 50])
student3 = Student("Student3", [10, 20, 30])

order1 = Order(employee1, student1, [book1, book2], "2020-01-01")
order2 = Order(employee2, student2, [book3, book4], "2020-02-01")

print(order1)
print(order2)
